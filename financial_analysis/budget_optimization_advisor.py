"""
Budget Optimization Advisor
Simple working implementation for portfolio demonstration
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any
import json
from datetime import datetime
import pandas as pd


@dataclass
class BudgetCategory:
    """Budget category with allocation and performance metrics."""
    name: str
    current_allocation: float
    proposed_allocation: float
    roi: float = 0.0
    priority_score: float = 5.0
    cost_type: str = "variable"  # "fixed", "variable", "discretionary"


@dataclass
class OptimizationResult:
    """Budget optimization analysis result."""
    total_budget: float
    categories: List[BudgetCategory]
    savings_identified: float
    reallocation_amount: float
    efficiency_gain: float
    recommendations: List[str] = field(default_factory=list)


class BudgetOptimizationAdvisor:
    """Optimize budget allocation across categories for maximum ROI."""
    
    def __init__(self):
        self.min_allocation_threshold = 0.01  # Minimum 1% allocation
        self.max_reallocation = 0.15  # Maximum 15% reallocation from any category
    
    def calculate_efficiency_score(self, category: BudgetCategory) -> float:
        """Calculate efficiency score for a budget category."""
        # Combine ROI and priority with weighted formula
        roi_component = min(10, max(0, category.roi * 2))  # Scale ROI to 0-10
        priority_component = category.priority_score
        
        # Weight ROI more heavily for variable costs
        if category.cost_type == "variable":
            efficiency_score = (roi_component * 0.7) + (priority_component * 0.3)
        elif category.cost_type == "discretionary":
            efficiency_score = (roi_component * 0.8) + (priority_component * 0.2)
        else:  # fixed costs
            efficiency_score = (roi_component * 0.4) + (priority_component * 0.6)
        
        return efficiency_score
    
    def identify_optimization_opportunities(self, categories: List[BudgetCategory]) -> Dict[str, List[str]]:
        """Identify specific optimization opportunities."""
        opportunities = {
            'high_roi_underfunded': [],
            'low_roi_overfunded': [],
            'cost_reduction': [],
            'reallocation': []
        }
        
        # Calculate efficiency scores
        for category in categories:
            efficiency = self.calculate_efficiency_score(category)
            
            if efficiency >= 8 and category.current_allocation < 0.10:
                opportunities['high_roi_underfunded'].append(category.name)
            elif efficiency <= 4 and category.current_allocation > 0.05:
                opportunities['low_roi_overfunded'].append(category.name)
            
            if category.cost_type == "discretionary" and category.roi < 1.0:
                opportunities['cost_reduction'].append(category.name)
            
            if efficiency >= 7 and category.cost_type in ["variable", "discretionary"]:
                opportunities['reallocation'].append(f"Increase {category.name}")
        
        return opportunities
    
    def optimize_allocation(self, categories: List[BudgetCategory], 
                          total_budget: float) -> OptimizationResult:
        """Optimize budget allocation across categories."""
        
        # Calculate current efficiency scores
        for category in categories:
            category.efficiency_score = self.calculate_efficiency_score(category)
        
        # Sort by efficiency score (descending)
        sorted_categories = sorted(categories, 
                                 key=lambda x: x.efficiency_score, reverse=True)
        
        # Calculate optimization
        total_savings = 0
        reallocation_pool = 0
        
        for category in sorted_categories:
            current_amount = category.current_allocation * total_budget
            
            # Reduce allocation for low-efficiency categories
            if category.efficiency_score < 5 and category.cost_type != "fixed":
                reduction_pct = min(0.10, (5 - category.efficiency_score) / 20)
                reduction_amount = current_amount * reduction_pct
                category.proposed_allocation = category.current_allocation - (reduction_amount / total_budget)
                reallocation_pool += reduction_amount
                
            # Increase allocation for high-efficiency categories
            elif category.efficiency_score > 7 and category.cost_type in ["variable", "discretionary"]:
                # Can receive from reallocation pool
                category.proposed_allocation = category.current_allocation  # Will be adjusted below
            else:
                category.proposed_allocation = category.current_allocation
        
        # Redistribute the reallocation pool to high-efficiency categories
        high_efficiency_categories = [c for c in sorted_categories 
                                    if c.efficiency_score > 7 and 
                                    c.cost_type in ["variable", "discretionary"]]
        
        if high_efficiency_categories and reallocation_pool > 0:
            # Distribute proportionally based on efficiency scores
            total_efficiency = sum(c.efficiency_score for c in high_efficiency_categories)
            
            for category in high_efficiency_categories:
                allocation_increase = (category.efficiency_score / total_efficiency) * reallocation_pool
                category.proposed_allocation += allocation_increase / total_budget
        
        # Generate recommendations
        recommendations = self._generate_recommendations(categories, total_budget)
        
        # Calculate metrics
        efficiency_gain = self._calculate_efficiency_gain(categories)
        
        return OptimizationResult(
            total_budget=total_budget,
            categories=categories,
            savings_identified=total_savings,
            reallocation_amount=reallocation_pool,
            efficiency_gain=efficiency_gain,
            recommendations=recommendations
        )
    
    def _generate_recommendations(self, categories: List[BudgetCategory], 
                                total_budget: float) -> List[str]:
        """Generate specific optimization recommendations."""
        recommendations = []
        
        for category in categories:
            current_amount = category.current_allocation * total_budget
            proposed_amount = category.proposed_allocation * total_budget
            change = proposed_amount - current_amount
            
            if abs(change) > total_budget * 0.01:  # Only report changes > 1%
                if change > 0:
                    recommendations.append(
                        f"Increase {category.name} budget by ${change:,.0f} "
                        f"({change/current_amount*100:+.1f}%) due to high ROI of {category.roi:.1f}x"
                    )
                else:
                    recommendations.append(
                        f"Reduce {category.name} budget by ${-change:,.0f} "
                        f"({change/current_amount*100:.1f}%) due to low efficiency score"
                    )
        
        # Add strategic recommendations
        opportunities = self.identify_optimization_opportunities(categories)
        
        if opportunities['high_roi_underfunded']:
            recommendations.append(
                f"Consider additional investment in high-ROI areas: "
                f"{', '.join(opportunities['high_roi_underfunded'])}"
            )
        
        if opportunities['cost_reduction']:
            recommendations.append(
                f"Review cost structure for potential reductions: "
                f"{', '.join(opportunities['cost_reduction'])}"
            )
        
        return recommendations
    
    def _calculate_efficiency_gain(self, categories: List[BudgetCategory]) -> float:
        """Calculate overall efficiency gain from optimization."""
        current_weighted_roi = sum(c.current_allocation * c.roi for c in categories)
        proposed_weighted_roi = sum(c.proposed_allocation * c.roi for c in categories)
        
        if current_weighted_roi > 0:
            return (proposed_weighted_roi - current_weighted_roi) / current_weighted_roi * 100
        return 0.0
    
    def create_budget_dashboard(self, result: OptimizationResult) -> pd.DataFrame:
        """Create budget comparison dashboard."""
        data = []
        
        for category in result.categories:
            current_amount = category.current_allocation * result.total_budget
            proposed_amount = category.proposed_allocation * result.total_budget
            change = proposed_amount - current_amount
            
            data.append({
                'Category': category.name,
                'Current_Allocation_$': current_amount,
                'Current_Allocation_%': category.current_allocation * 100,
                'Proposed_Allocation_$': proposed_amount,
                'Proposed_Allocation_%': category.proposed_allocation * 100,
                'Change_$': change,
                'Change_%': (change / current_amount * 100) if current_amount > 0 else 0,
                'ROI': category.roi,
                'Priority_Score': category.priority_score,
                'Efficiency_Score': getattr(category, 'efficiency_score', 0),
                'Cost_Type': category.cost_type
            })
        
        return pd.DataFrame(data)
    
    def export_analysis(self, result: OptimizationResult, filename: str = None) -> str:
        """Export optimization analysis to JSON."""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"budget_optimization_{timestamp}.json"
        
        # Convert to serializable format
        export_data = {
            'analysis_date': datetime.now().isoformat(),
            'total_budget': result.total_budget,
            'optimization_summary': {
                'savings_identified': result.savings_identified,
                'reallocation_amount': result.reallocation_amount,
                'efficiency_gain_pct': result.efficiency_gain
            },
            'categories': [
                {
                    'name': cat.name,
                    'current_allocation_pct': cat.current_allocation * 100,
                    'proposed_allocation_pct': cat.proposed_allocation * 100,
                    'current_amount': cat.current_allocation * result.total_budget,
                    'proposed_amount': cat.proposed_allocation * result.total_budget,
                    'roi': cat.roi,
                    'priority_score': cat.priority_score,
                    'cost_type': cat.cost_type,
                    'efficiency_score': getattr(cat, 'efficiency_score', 0)
                } for cat in result.categories
            ],
            'recommendations': result.recommendations
        }
        
        with open(filename, 'w') as f:
            json.dump(export_data, f, indent=2)
        
        return filename


def demo_usage():
    """Demonstrate the budget optimization advisor."""
    print("💰 Budget Optimization Advisor Demo")
    print("=" * 50)
    
    # Initialize advisor
    advisor = BudgetOptimizationAdvisor()
    
    # Sample budget categories for a tech company
    categories = [
        BudgetCategory(
            name="Sales & Marketing",
            current_allocation=0.30,
            proposed_allocation=0.30,
            roi=2.5,
            priority_score=8.0,
            cost_type="variable"
        ),
        BudgetCategory(
            name="Product Development",
            current_allocation=0.25,
            proposed_allocation=0.25,
            roi=4.2,
            priority_score=9.0,
            cost_type="variable"
        ),
        BudgetCategory(
            name="Operations",
            current_allocation=0.20,
            proposed_allocation=0.20,
            roi=1.8,
            priority_score=7.0,
            cost_type="fixed"
        ),
        BudgetCategory(
            name="Customer Success",
            current_allocation=0.10,
            proposed_allocation=0.10,
            roi=3.1,
            priority_score=8.5,
            cost_type="variable"
        ),
        BudgetCategory(
            name="Administrative",
            current_allocation=0.10,
            proposed_allocation=0.10,
            roi=0.5,
            priority_score=4.0,
            cost_type="fixed"
        ),
        BudgetCategory(
            name="Training & Development",
            current_allocation=0.05,
            proposed_allocation=0.05,
            roi=3.8,
            priority_score=6.5,
            cost_type="discretionary"
        )
    ]
    
    total_budget = 1_000_000  # $1M total budget
    
    # Perform optimization
    result = advisor.optimize_allocation(categories, total_budget)
    
    # Display results
    print(f"\n📊 Budget Optimization Results")
    print(f"Total Budget: ${result.total_budget:,.0f}")
    print(f"Efficiency Gain: {result.efficiency_gain:.1f}%")
    print(f"Reallocation Amount: ${result.reallocation_amount:,.0f}")
    
    print(f"\n📈 Category Analysis:")
    for category in sorted(result.categories, key=lambda x: x.proposed_allocation, reverse=True):
        current_amount = category.current_allocation * total_budget
        proposed_amount = category.proposed_allocation * total_budget
        change = proposed_amount - current_amount
        efficiency = getattr(category, 'efficiency_score', 0)
        
        print(f"\n  {category.name}:")
        print(f"    Current:  ${current_amount:8,.0f} ({category.current_allocation*100:5.1f}%)")
        print(f"    Proposed: ${proposed_amount:8,.0f} ({category.proposed_allocation*100:5.1f}%)")
        print(f"    Change:   ${change:8,.0f} ({change/current_amount*100:+5.1f}%)" if current_amount > 0 else "    Change:        $0 (  0.0%)")
        print(f"    ROI: {category.roi:.1f}x | Priority: {category.priority_score:.1f} | Efficiency: {efficiency:.1f}")
    
    if result.recommendations:
        print(f"\n💡 Optimization Recommendations:")
        for i, rec in enumerate(result.recommendations, 1):
            print(f"  {i}. {rec}")
    
    # Create and display dashboard
    try:
        dashboard = advisor.create_budget_dashboard(result)
        print(f"\n📋 Budget Dashboard:")
        print(dashboard.to_string(index=False, float_format='%.1f'))
    except ImportError:
        print(f"\n📋 Budget Dashboard: (pandas not available for display)")
    
    # Export analysis
    filename = advisor.export_analysis(result)
    print(f"\n📄 Analysis exported to: {filename}")


if __name__ == "__main__":
    demo_usage()