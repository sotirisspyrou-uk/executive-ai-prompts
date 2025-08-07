"""
Acquisition Due Diligence Analyzer
Simple working implementation for portfolio demonstration
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any
import json
from datetime import datetime


@dataclass
class FinancialMetrics:
    """Financial performance metrics for target company."""
    revenue_3yr_cagr: float = 0.0
    ebitda_margin: float = 0.0
    debt_to_equity: float = 0.0
    current_ratio: float = 0.0
    roe: float = 0.0
    free_cash_flow_margin: float = 0.0


@dataclass
class DueDiligenceReport:
    """Due diligence analysis report."""
    target_company: str
    deal_value: float
    financial_score: float = 0.0
    strategic_score: float = 0.0
    risk_score: float = 0.0
    overall_recommendation: str = ""
    key_findings: List[str] = field(default_factory=list)
    red_flags: List[str] = field(default_factory=list)
    synergies: List[str] = field(default_factory=list)


class AcquisitionDueDiligenceAnalyzer:
    """Analyze acquisition targets with financial and strategic assessment."""
    
    def __init__(self):
        self.weight_financial = 0.4
        self.weight_strategic = 0.35
        self.weight_risk = 0.25
    
    def analyze_financial_metrics(self, metrics: FinancialMetrics) -> Dict[str, Any]:
        """Analyze financial performance and return scoring."""
        scores = {
            'revenue_growth': min(10, max(0, metrics.revenue_3yr_cagr * 2)),
            'profitability': min(10, max(0, metrics.ebitda_margin * 0.5)),
            'liquidity': min(10, max(0, metrics.current_ratio * 5)),
            'leverage': min(10, max(0, 10 - (metrics.debt_to_equity * 2))),
            'efficiency': min(10, max(0, metrics.roe * 0.5)),
            'cash_generation': min(10, max(0, metrics.free_cash_flow_margin * 0.4))
        }
        
        financial_score = sum(scores.values()) / len(scores)
        
        return {
            'overall_score': financial_score,
            'component_scores': scores,
            'strengths': [k for k, v in scores.items() if v >= 7],
            'concerns': [k for k, v in scores.items() if v < 5]
        }
    
    def assess_strategic_fit(self, strategic_factors: Dict[str, float]) -> Dict[str, Any]:
        """Assess strategic alignment and synergy potential."""
        default_factors = {
            'market_expansion': 5.0,
            'product_synergies': 5.0,
            'cost_synergies': 5.0,
            'technology_capabilities': 5.0,
            'customer_base_overlap': 5.0,
            'cultural_alignment': 5.0
        }
        
        # Use provided factors or defaults
        factors = {**default_factors, **strategic_factors}
        strategic_score = sum(factors.values()) / len(factors)
        
        return {
            'overall_score': strategic_score,
            'synergy_potential': [k for k, v in factors.items() if v >= 7],
            'integration_challenges': [k for k, v in factors.items() if v < 5]
        }
    
    def evaluate_risks(self, risk_factors: Dict[str, float]) -> Dict[str, Any]:
        """Evaluate acquisition risks and red flags."""
        default_risks = {
            'integration_complexity': 5.0,
            'regulatory_hurdles': 5.0,
            'customer_retention': 5.0,
            'key_person_dependency': 5.0,
            'technology_obsolescence': 5.0,
            'market_competition': 5.0
        }
        
        risks = {**default_risks, **risk_factors}
        # Higher risk scores are worse, so invert for overall scoring
        risk_score = 10 - (sum(risks.values()) / len(risks))
        
        return {
            'overall_score': risk_score,
            'high_risks': [k for k, v in risks.items() if v >= 8],
            'moderate_risks': [k for k, v in risks.items() if v >= 6 and v < 8],
            'manageable_risks': [k for k, v in risks.items() if v < 6]
        }
    
    def calculate_valuation_range(self, metrics: FinancialMetrics, 
                                 revenue: float, ebitda: float) -> Dict[str, float]:
        """Calculate valuation range using multiple methods."""
        # Simple valuation multiples (industry averages)
        revenue_multiple_low = 2.0
        revenue_multiple_high = 4.0
        ebitda_multiple_low = 8.0
        ebitda_multiple_high = 12.0
        
        # DCF approximation based on cash flow
        dcf_value = ebitda * metrics.free_cash_flow_margin * 8  # 8x FCF multiple
        
        return {
            'revenue_based_low': revenue * revenue_multiple_low,
            'revenue_based_high': revenue * revenue_multiple_high,
            'ebitda_based_low': ebitda * ebitda_multiple_low,
            'ebitda_based_high': ebitda * ebitda_multiple_high,
            'dcf_estimate': dcf_value,
            'recommended_range_low': min(ebitda * ebitda_multiple_low, dcf_value * 0.9),
            'recommended_range_high': max(ebitda * ebitda_multiple_high, dcf_value * 1.1)
        }
    
    def generate_comprehensive_report(self, 
                                    target_company: str,
                                    deal_value: float,
                                    financial_metrics: FinancialMetrics,
                                    strategic_factors: Dict[str, float] = None,
                                    risk_factors: Dict[str, float] = None,
                                    revenue: float = 100.0,
                                    ebitda: float = 20.0) -> DueDiligenceReport:
        """Generate comprehensive due diligence report."""
        
        # Analyze each component
        financial_analysis = self.analyze_financial_metrics(financial_metrics)
        strategic_analysis = self.assess_strategic_fit(strategic_factors or {})
        risk_analysis = self.evaluate_risks(risk_factors or {})
        valuation = self.calculate_valuation_range(financial_metrics, revenue, ebitda)
        
        # Calculate overall scores
        overall_score = (
            financial_analysis['overall_score'] * self.weight_financial +
            strategic_analysis['overall_score'] * self.weight_strategic +
            risk_analysis['overall_score'] * self.weight_risk
        )
        
        # Generate recommendation
        if overall_score >= 8.0 and deal_value <= valuation['recommended_range_high']:
            recommendation = "STRONG BUY - Excellent strategic fit with attractive valuation"
        elif overall_score >= 6.5 and deal_value <= valuation['recommended_range_high']:
            recommendation = "BUY - Good opportunity with manageable risks"
        elif overall_score >= 5.0:
            recommendation = "CONDITIONAL - Proceed with caution, negotiate better terms"
        else:
            recommendation = "PASS - Too many risks and concerns"
        
        # Compile findings
        key_findings = []
        if financial_analysis['strengths']:
            key_findings.append(f"Financial strengths: {', '.join(financial_analysis['strengths'])}")
        if strategic_analysis['synergy_potential']:
            key_findings.append(f"Synergy opportunities: {', '.join(strategic_analysis['synergy_potential'])}")
        
        red_flags = []
        if financial_analysis['concerns']:
            red_flags.extend([f"Financial concern: {concern}" for concern in financial_analysis['concerns']])
        if risk_analysis['high_risks']:
            red_flags.extend([f"High risk: {risk}" for risk in risk_analysis['high_risks']])
        
        synergies = strategic_analysis['synergy_potential']
        
        return DueDiligenceReport(
            target_company=target_company,
            deal_value=deal_value,
            financial_score=financial_analysis['overall_score'],
            strategic_score=strategic_analysis['overall_score'],
            risk_score=risk_analysis['overall_score'],
            overall_recommendation=recommendation,
            key_findings=key_findings,
            red_flags=red_flags,
            synergies=synergies
        )
    
    def export_report(self, report: DueDiligenceReport, filename: str = None) -> str:
        """Export report to JSON format."""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"due_diligence_{report.target_company}_{timestamp}.json"
        
        report_dict = {
            'target_company': report.target_company,
            'deal_value': report.deal_value,
            'analysis_date': datetime.now().isoformat(),
            'scores': {
                'financial': report.financial_score,
                'strategic': report.strategic_score,
                'risk': report.risk_score,
                'overall': (report.financial_score + report.strategic_score + report.risk_score) / 3
            },
            'recommendation': report.overall_recommendation,
            'key_findings': report.key_findings,
            'red_flags': report.red_flags,
            'synergies': report.synergies
        }
        
        with open(filename, 'w') as f:
            json.dump(report_dict, f, indent=2)
        
        return filename


def demo_usage():
    """Demonstrate the acquisition due diligence analyzer."""
    print("🏢 Acquisition Due Diligence Analyzer Demo")
    print("=" * 50)
    
    # Initialize analyzer
    analyzer = AcquisitionDueDiligenceAnalyzer()
    
    # Sample target company metrics
    target_metrics = FinancialMetrics(
        revenue_3yr_cagr=15.2,  # 15.2% revenue growth
        ebitda_margin=22.5,      # 22.5% EBITDA margin
        debt_to_equity=1.2,      # 1.2x debt-to-equity
        current_ratio=2.1,       # 2.1x current ratio
        roe=18.5,                # 18.5% ROE
        free_cash_flow_margin=12.0  # 12% FCF margin
    )
    
    # Strategic factors (1-10 scale)
    strategic_factors = {
        'market_expansion': 8.5,
        'product_synergies': 7.0,
        'cost_synergies': 6.5,
        'technology_capabilities': 9.0,
        'customer_base_overlap': 4.0,
        'cultural_alignment': 7.5
    }
    
    # Risk factors (1-10 scale, higher = more risky)
    risk_factors = {
        'integration_complexity': 6.0,
        'regulatory_hurdles': 3.0,
        'customer_retention': 5.0,
        'key_person_dependency': 7.5,
        'technology_obsolescence': 4.0,
        'market_competition': 6.5
    }
    
    # Generate comprehensive report
    report = analyzer.generate_comprehensive_report(
        target_company="TechCorp Solutions",
        deal_value=250.0,  # $250M deal
        financial_metrics=target_metrics,
        strategic_factors=strategic_factors,
        risk_factors=risk_factors,
        revenue=100.0,     # $100M revenue
        ebitda=22.5        # $22.5M EBITDA
    )
    
    # Display results
    print(f"\n📊 Analysis Results for {report.target_company}")
    print(f"Deal Value: ${report.deal_value}M")
    print(f"\n🎯 Scores:")
    print(f"  Financial Score: {report.financial_score:.1f}/10")
    print(f"  Strategic Score: {report.strategic_score:.1f}/10")
    print(f"  Risk Score: {report.risk_score:.1f}/10")
    
    print(f"\n✅ Recommendation: {report.overall_recommendation}")
    
    if report.key_findings:
        print(f"\n🔍 Key Findings:")
        for finding in report.key_findings:
            print(f"  • {finding}")
    
    if report.red_flags:
        print(f"\n⚠️ Red Flags:")
        for flag in report.red_flags:
            print(f"  • {flag}")
    
    if report.synergies:
        print(f"\n🤝 Synergy Opportunities:")
        for synergy in report.synergies:
            print(f"  • {synergy}")
    
    # Export report
    filename = analyzer.export_report(report)
    print(f"\n📄 Report exported to: {filename}")


if __name__ == "__main__":
    demo_usage()