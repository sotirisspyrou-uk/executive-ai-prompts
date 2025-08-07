"""
Cost-Benefit Assessment Tool
Simple working implementation for portfolio demonstration
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Tuple
import json
from datetime import datetime
import math


@dataclass
class CostItem:
    """Individual cost item with timing and category."""
    description: str
    amount: float
    timing_months: int = 0  # When cost occurs (0 = immediate)
    category: str = "operational"  # operational, capital, one_time
    recurring: bool = False


@dataclass
class BenefitItem:
    """Individual benefit item with timing and confidence."""
    description: str
    amount: float
    timing_months: int = 6  # When benefit starts
    category: str = "revenue"  # revenue, cost_savings, productivity
    recurring: bool = True
    confidence: float = 0.8  # 0-1 confidence level


@dataclass
class CostBenefitResult:
    """Cost-benefit analysis result."""
    total_costs: float
    total_benefits: float
    net_benefit: float
    benefit_cost_ratio: float
    roi_percentage: float
    payback_months: int
    npv: float
    irr: float
    risk_adjusted_npv: float
    recommendation: str
    cost_breakdown: Dict[str, float] = field(default_factory=dict)
    benefit_breakdown: Dict[str, float] = field(default_factory=dict)
    sensitivity_analysis: Dict[str, float] = field(default_factory=dict)


class CostBenefitAssessor:
    """Comprehensive cost-benefit analysis tool."""
    
    def __init__(self, discount_rate: float = 0.10, analysis_period_years: int = 3):
        self.discount_rate = discount_rate
        self.analysis_period_months = analysis_period_years * 12
        self.monthly_discount_rate = discount_rate / 12
    
    def calculate_present_value(self, future_value: float, months: int) -> float:
        """Calculate present value of future cash flow."""
        if months <= 0:
            return future_value
        return future_value / (1 + self.monthly_discount_rate) ** months
    
    def analyze_costs(self, costs: List[CostItem]) -> Dict[str, Any]:
        """Analyze and categorize all costs."""
        cost_analysis = {
            'total_pv': 0.0,
            'by_category': {},
            'by_timing': {},
            'cash_flow': [0.0] * self.analysis_period_months
        }
        
        for cost in costs:
            # Calculate present value
            if cost.recurring:
                # For recurring costs, calculate NPV of annuity
                pv = 0.0
                for month in range(cost.timing_months, self.analysis_period_months, 1):
                    pv += self.calculate_present_value(cost.amount, month)
            else:
                pv = self.calculate_present_value(cost.amount, cost.timing_months)
            
            cost_analysis['total_pv'] += pv
            
            # Categorize costs
            if cost.category not in cost_analysis['by_category']:
                cost_analysis['by_category'][cost.category] = 0.0
            cost_analysis['by_category'][cost.category] += pv
            
            # Track cash flow timing
            if cost.timing_months < len(cost_analysis['cash_flow']):
                if cost.recurring:
                    for month in range(cost.timing_months, self.analysis_period_months, 1):
                        if month < len(cost_analysis['cash_flow']):
                            cost_analysis['cash_flow'][month] -= cost.amount
                else:
                    cost_analysis['cash_flow'][cost.timing_months] -= cost.amount
        
        return cost_analysis
    
    def analyze_benefits(self, benefits: List[BenefitItem]) -> Dict[str, Any]:
        """Analyze and categorize all benefits."""
        benefit_analysis = {
            'total_pv': 0.0,
            'risk_adjusted_pv': 0.0,
            'by_category': {},
            'by_timing': {},
            'cash_flow': [0.0] * self.analysis_period_months
        }
        
        for benefit in benefits:
            # Calculate present value
            if benefit.recurring:
                pv = 0.0
                for month in range(benefit.timing_months, self.analysis_period_months, 1):
                    pv += self.calculate_present_value(benefit.amount, month)
            else:
                pv = self.calculate_present_value(benefit.amount, benefit.timing_months)
            
            risk_adjusted_pv = pv * benefit.confidence
            
            benefit_analysis['total_pv'] += pv
            benefit_analysis['risk_adjusted_pv'] += risk_adjusted_pv
            
            # Categorize benefits
            if benefit.category not in benefit_analysis['by_category']:
                benefit_analysis['by_category'][benefit.category] = 0.0
            benefit_analysis['by_category'][benefit.category] += pv
            
            # Track cash flow timing
            if benefit.timing_months < len(benefit_analysis['cash_flow']):
                if benefit.recurring:
                    for month in range(benefit.timing_months, self.analysis_period_months, 1):
                        if month < len(benefit_analysis['cash_flow']):
                            benefit_analysis['cash_flow'][month] += benefit.amount
                else:
                    benefit_analysis['cash_flow'][benefit.timing_months] += benefit.amount
        
        return benefit_analysis
    
    def calculate_payback_period(self, cost_cash_flow: List[float], 
                               benefit_cash_flow: List[float]) -> int:
        """Calculate payback period in months."""
        cumulative_net_flow = 0.0
        
        for month in range(len(cost_cash_flow)):
            net_flow = benefit_cash_flow[month] + cost_cash_flow[month]  # costs are negative
            cumulative_net_flow += net_flow
            
            if cumulative_net_flow > 0:
                return month + 1
        
        return -1  # No payback within analysis period
    
    def calculate_irr(self, cost_cash_flow: List[float], 
                     benefit_cash_flow: List[float]) -> float:
        """Calculate Internal Rate of Return (simplified)."""
        # Combine cash flows
        net_cash_flows = []
        for i in range(len(cost_cash_flow)):
            net_cash_flows.append(cost_cash_flow[i] + benefit_cash_flow[i])
        
        if not net_cash_flows or net_cash_flows[0] >= 0:
            return 0.0  # No initial investment
        
        # Simple IRR approximation using Newton's method
        # For demo purposes, using simplified calculation
        total_costs = abs(sum(cf for cf in net_cash_flows if cf < 0))
        total_benefits = sum(cf for cf in net_cash_flows if cf > 0)
        
        if total_costs == 0:
            return 0.0
        
        # Approximate IRR based on average return
        average_monthly_return = total_benefits / len([cf for cf in net_cash_flows if cf > 0]) if any(cf > 0 for cf in net_cash_flows) else 0
        approximate_irr = (average_monthly_return / total_costs) * 12 * 100
        
        return min(100.0, max(-50.0, approximate_irr))  # Cap at reasonable range
    
    def perform_sensitivity_analysis(self, costs: List[CostItem], 
                                   benefits: List[BenefitItem]) -> Dict[str, float]:
        """Perform sensitivity analysis on key variables."""
        base_result = self.assess_project(costs, benefits)
        base_npv = base_result.npv
        
        sensitivity = {}
        
        # Test cost increase
        costs_high = [CostItem(c.description, c.amount * 1.2, c.timing_months, 
                              c.category, c.recurring) for c in costs]
        result_costs_high = self.assess_project(costs_high, benefits)
        sensitivity['costs_+20%'] = (result_costs_high.npv - base_npv) / base_npv * 100 if base_npv != 0 else 0
        
        # Test benefit decrease
        benefits_low = [BenefitItem(b.description, b.amount * 0.8, b.timing_months,
                                   b.category, b.recurring, b.confidence) for b in benefits]
        result_benefits_low = self.assess_project(costs, benefits_low)
        sensitivity['benefits_-20%'] = (result_benefits_low.npv - base_npv) / base_npv * 100 if base_npv != 0 else 0
        
        # Test delayed benefits
        benefits_delayed = [BenefitItem(b.description, b.amount, b.timing_months + 3,
                                       b.category, b.recurring, b.confidence) for b in benefits]
        result_delayed = self.assess_project(costs, benefits_delayed)
        sensitivity['benefits_delayed_3mo'] = (result_delayed.npv - base_npv) / base_npv * 100 if base_npv != 0 else 0
        
        return sensitivity
    
    def assess_project(self, costs: List[CostItem], benefits: List[BenefitItem]) -> CostBenefitResult:
        """Perform comprehensive cost-benefit analysis."""
        
        # Analyze costs and benefits
        cost_analysis = self.analyze_costs(costs)
        benefit_analysis = self.analyze_benefits(benefits)
        
        # Calculate key metrics
        total_costs = cost_analysis['total_pv']
        total_benefits = benefit_analysis['total_pv']
        risk_adjusted_benefits = benefit_analysis['risk_adjusted_pv']
        
        net_benefit = total_benefits - total_costs
        risk_adjusted_npv = risk_adjusted_benefits - total_costs
        
        # Calculate ratios and percentages
        benefit_cost_ratio = total_benefits / total_costs if total_costs > 0 else float('inf')
        roi_percentage = (net_benefit / total_costs) * 100 if total_costs > 0 else 0.0
        
        # Calculate payback period
        payback_months = self.calculate_payback_period(
            cost_analysis['cash_flow'], 
            benefit_analysis['cash_flow']
        )
        
        # Calculate IRR
        irr = self.calculate_irr(
            cost_analysis['cash_flow'],
            benefit_analysis['cash_flow']
        )
        
        # Perform sensitivity analysis
        sensitivity = self.perform_sensitivity_analysis(costs, benefits)
        
        # Generate recommendation
        recommendation = self._generate_recommendation(
            benefit_cost_ratio, roi_percentage, payback_months, risk_adjusted_npv
        )
        
        return CostBenefitResult(
            total_costs=total_costs,
            total_benefits=total_benefits,
            net_benefit=net_benefit,
            benefit_cost_ratio=benefit_cost_ratio,
            roi_percentage=roi_percentage,
            payback_months=payback_months,
            npv=net_benefit,
            irr=irr,
            risk_adjusted_npv=risk_adjusted_npv,
            recommendation=recommendation,
            cost_breakdown=cost_analysis['by_category'],
            benefit_breakdown=benefit_analysis['by_category'],
            sensitivity_analysis=sensitivity
        )
    
    def _generate_recommendation(self, bcr: float, roi: float, 
                               payback: int, risk_adj_npv: float) -> str:
        """Generate investment recommendation based on metrics."""
        
        if risk_adj_npv <= 0:
            return "REJECT - Negative risk-adjusted NPV"
        elif bcr < 1.0:
            return "REJECT - Costs exceed benefits"
        elif roi > 50 and payback <= 12 and bcr > 2.0:
            return "STRONG APPROVE - Excellent returns with quick payback"
        elif roi > 25 and payback <= 24 and bcr > 1.5:
            return "APPROVE - Good investment with acceptable risk"
        elif roi > 15 and payback <= 36:
            return "CONDITIONAL APPROVE - Moderate returns, monitor closely"
        else:
            return "REVIEW REQUIRED - Marginal investment case"
    
    def export_analysis(self, result: CostBenefitResult, project_name: str = "Project") -> str:
        """Export analysis to JSON file."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"cost_benefit_{project_name.lower().replace(' ', '_')}_{timestamp}.json"
        
        export_data = {
            'project_name': project_name,
            'analysis_date': datetime.now().isoformat(),
            'analysis_parameters': {
                'discount_rate': self.discount_rate,
                'analysis_period_months': self.analysis_period_months
            },
            'financial_metrics': {
                'total_costs': result.total_costs,
                'total_benefits': result.total_benefits,
                'net_benefit': result.net_benefit,
                'benefit_cost_ratio': result.benefit_cost_ratio,
                'roi_percentage': result.roi_percentage,
                'payback_months': result.payback_months,
                'npv': result.npv,
                'irr': result.irr,
                'risk_adjusted_npv': result.risk_adjusted_npv
            },
            'breakdown': {
                'costs_by_category': result.cost_breakdown,
                'benefits_by_category': result.benefit_breakdown
            },
            'sensitivity_analysis': result.sensitivity_analysis,
            'recommendation': result.recommendation
        }
        
        with open(filename, 'w') as f:
            json.dump(export_data, f, indent=2)
        
        return filename


def demo_usage():
    """Demonstrate the cost-benefit assessor."""
    print("📊 Cost-Benefit Assessment Tool Demo")
    print("=" * 50)
    
    # Initialize assessor (10% discount rate, 3-year analysis)
    assessor = CostBenefitAssessor(discount_rate=0.10, analysis_period_years=3)
    
    # Define project costs
    costs = [
        CostItem("Software Licensing", 50000, 0, "capital", False),
        CostItem("Implementation Services", 80000, 1, "one_time", False),
        CostItem("Training & Change Management", 25000, 2, "one_time", False),
        CostItem("Monthly Maintenance", 3000, 3, "operational", True),
        CostItem("Additional Staff", 8000, 3, "operational", True),
    ]
    
    # Define project benefits
    benefits = [
        BenefitItem("Process Automation Savings", 15000, 6, "cost_savings", True, 0.9),
        BenefitItem("Improved Productivity", 12000, 4, "productivity", True, 0.8),
        BenefitItem("Reduced Error Costs", 5000, 8, "cost_savings", True, 0.85),
        BenefitItem("New Revenue Opportunities", 20000, 12, "revenue", True, 0.7),
        BenefitItem("Compliance Cost Avoidance", 30000, 6, "cost_savings", False, 0.95),
    ]
    
    # Perform analysis
    result = assessor.assess_project(costs, benefits)
    
    # Display results
    print(f"\n💰 Financial Analysis Results")
    print(f"Total Costs (PV):      ${result.total_costs:,.0f}")
    print(f"Total Benefits (PV):   ${result.total_benefits:,.0f}")
    print(f"Net Benefit (NPV):     ${result.net_benefit:,.0f}")
    print(f"Risk-Adjusted NPV:     ${result.risk_adjusted_npv:,.0f}")
    
    print(f"\n📈 Key Metrics")
    print(f"Benefit-Cost Ratio:    {result.benefit_cost_ratio:.2f}")
    print(f"ROI:                   {result.roi_percentage:.1f}%")
    print(f"IRR:                   {result.irr:.1f}%")
    print(f"Payback Period:        {result.payback_months} months" if result.payback_months > 0 else "Payback Period:        Beyond analysis period")
    
    print(f"\n🎯 Recommendation: {result.recommendation}")
    
    # Cost breakdown
    if result.cost_breakdown:
        print(f"\n💸 Cost Breakdown:")
        for category, amount in result.cost_breakdown.items():
            percentage = (amount / result.total_costs) * 100
            print(f"  {category.title():20} ${amount:8,.0f} ({percentage:4.1f}%)")
    
    # Benefit breakdown
    if result.benefit_breakdown:
        print(f"\n💵 Benefit Breakdown:")
        for category, amount in result.benefit_breakdown.items():
            percentage = (amount / result.total_benefits) * 100
            print(f"  {category.title():20} ${amount:8,.0f} ({percentage:4.1f}%)")
    
    # Sensitivity analysis
    if result.sensitivity_analysis:
        print(f"\n🔍 Sensitivity Analysis (NPV Impact):")
        for scenario, impact in result.sensitivity_analysis.items():
            print(f"  {scenario:20} {impact:+6.1f}%")
    
    # Export analysis
    filename = assessor.export_analysis(result, "Digital Transformation Project")
    print(f"\n📄 Analysis exported to: {filename}")


if __name__ == "__main__":
    demo_usage()