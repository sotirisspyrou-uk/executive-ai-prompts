"""
Executive AI Prompts - ROI Investment Evaluator

Comprehensive investment decision support prompts with financial modeling,
ROI analysis, and capital allocation optimization frameworks.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from enum import Enum
from prompt_manager import PromptTemplate, PromptCategory, prompt_manager
from context_adapter import context_adapter


class InvestmentType(Enum):
    CAPEX = "capital_expenditure"
    ACQUISITION = "acquisition"
    R_AND_D = "research_development"
    TECHNOLOGY = "technology_infrastructure"
    MARKET_EXPANSION = "market_expansion"
    OPERATIONAL = "operational_improvement"


@dataclass
class InvestmentConfig:
    """Configuration for investment evaluation analysis."""
    investment_type: InvestmentType = InvestmentType.CAPEX
    investment_amount: Optional[float] = None
    time_horizon: str = "5 years"
    hurdle_rate: Optional[float] = None
    risk_category: str = "medium"  # "low", "medium", "high"
    strategic_importance: str = "core"  # "core", "growth", "experimental"
    competitive_analysis: bool = True
    sensitivity_analysis: bool = True
    scenario_modeling: bool = True


class ROIInvestmentEvaluator:
    """Advanced ROI and investment evaluation prompt generator."""
    
    def __init__(self):
        self.templates = {}
        self._initialize_templates()
    
    def _initialize_templates(self) -> None:
        """Initialize investment evaluation templates."""
        
        # Comprehensive Investment Analysis
        self.templates['comprehensive_investment_analysis'] = PromptTemplate(
            name="Comprehensive Investment ROI Analysis",
            category=PromptCategory.FINANCIAL_ANALYSIS,
            base_prompt="""
As {role} evaluating a {investment_type} investment of {investment_amount} over a {time_horizon} timeframe, conduct comprehensive ROI analysis and investment decision support.

**INVESTMENT EVALUATION FRAMEWORK:**

1. **INVESTMENT OVERVIEW AND STRATEGIC RATIONALE**
   - Investment description and strategic objectives
   - Strategic fit and alignment with business priorities
   - Competitive necessity vs. growth opportunity
   - Timeline and implementation requirements
   - Key assumptions and dependencies

2. **FINANCIAL ANALYSIS AND MODELING**
   
   **Revenue Impact Analysis:**
   - Direct revenue generation potential
   - Market share and customer acquisition impact
   - Pricing and margin improvement opportunities
   - Cross-selling and upselling benefits
   - Revenue timing and ramp-up profile
   
   **Cost and Investment Analysis:**
   - Initial capital investment requirements
   - Ongoing operational cost implications
   - Implementation and transition costs
   - Working capital and cash flow impacts
   - Opportunity costs and resource allocation
   
   **ROI and Financial Metrics:**
   - Net Present Value (NPV) calculation
   - Internal Rate of Return (IRR) analysis
   - Payback period and discounted payback
   - Return on Investment (ROI) and Return on Assets (ROA)
   - Economic Value Added (EVA) assessment

3. **RISK ASSESSMENT AND SENSITIVITY ANALYSIS**
   
   **Risk Factor Identification:**
   - Market and demand risks
   - Execution and operational risks
   - Technology and obsolescence risks
   - Competitive response risks
   - Regulatory and compliance risks
   
   **Sensitivity Analysis:**
   - Revenue sensitivity to market assumptions
   - Cost sensitivity to implementation variables
   - IRR sensitivity to key input changes
   - Break-even analysis and threshold identification
   - Scenario modeling (optimistic, base, pessimistic)

4. **STRATEGIC VALUE ASSESSMENT**
   - Competitive advantage creation
   - Market positioning improvement
   - Capability building and platform value
   - Option value and future opportunity creation
   - Strategic synergies and portfolio benefits

5. **COMPARATIVE ANALYSIS AND ALTERNATIVES**
   - Alternative investment options evaluation
   - Resource allocation trade-offs
   - Timing optimization analysis
   - Build vs. buy vs. partner analysis
   - Investment portfolio prioritization

**INVESTMENT RECOMMENDATION:**
- Go/No-Go decision with rationale
- Optimal investment sizing and timing
- Risk mitigation and contingency planning
- Performance monitoring and success metrics
- Investment committee presentation summary

{industry_context}
{role_focus}
{regulatory_considerations}

Provide quantitative analysis with clear financial justification and decision criteria.

{communication_guidance}
""",
            variables={
                "investment_type": "capital investment",
                "investment_amount": "TBD",
                "time_horizon": "5 years"
            },
            context_adaptations={
                "financial_services": "Include regulatory capital impact, Basel III considerations, and stress testing requirements. Address risk-weighted asset implications.",
                "technology": "Focus on scalability, technical debt, platform effects, and innovation velocity. Consider cybersecurity and data privacy investments.",
                "healthcare": "Include clinical validation, regulatory approval costs, and reimbursement considerations. Address patient safety and outcomes.",
                "cfo": "Emphasize capital allocation framework, financing options, and impact on financial ratios and credit metrics.",
                "ceo": "Frame for board approval with strategic rationale, competitive positioning, and shareholder value creation."
            },
            quality_criteria=[
                "Comprehensive financial modeling with NPV and IRR analysis",
                "Thorough risk assessment with sensitivity analysis",
                "Strategic value quantification beyond financial returns",
                "Clear investment recommendation with decision criteria",
                "Implementation roadmap with monitoring metrics"
            ],
            tags=["roi_analysis", "investment_evaluation", "capital_allocation", "financial_modeling"]
        )
        
        # Capital Allocation Framework
        self.templates['capital_allocation_framework'] = PromptTemplate(
            name="Strategic Capital Allocation Framework",
            category=PromptCategory.FINANCIAL_ANALYSIS,
            base_prompt="""
Develop comprehensive capital allocation strategy and investment prioritization framework for optimal resource deployment across {strategic_priorities} initiatives.

**CAPITAL ALLOCATION FRAMEWORK:**

1. **INVESTMENT UNIVERSE AND CATEGORIZATION**
   
   **Core Business Investments (Maintain Competitive Position):**
   - Maintenance capital expenditure
   - Technology infrastructure upgrades
   - Regulatory and compliance investments
   - Essential operational improvements
   - Market position defense initiatives
   
   **Growth Investments (Expand Market Position):**
   - Market expansion and new geography entry
   - Product development and innovation
   - Customer acquisition and retention
   - Channel development and partnerships
   - Capacity expansion and scale investments
   
   **Transformational Investments (Create New Value):**
   - Digital transformation initiatives
   - Business model innovation
   - Acquisitions and strategic partnerships
   - Platform and ecosystem development
   - Disruptive technology adoption

2. **INVESTMENT EVALUATION CRITERIA**
   
   **Financial Criteria:**
   - Risk-adjusted return thresholds by category
   - Payback period and NPV requirements
   - Cash flow generation and timing
   - Capital intensity and scalability
   - Financial ratio and covenant impacts
   
   **Strategic Criteria:**
   - Strategic fit and competitive advantage
   - Market opportunity size and growth
   - Execution probability and capability fit
   - Optionality and future value creation
   - Synergy potential and portfolio effects

3. **CAPITAL ALLOCATION METHODOLOGY**
   
   **Portfolio Optimization Approach:**
   - Risk-return optimization across investment categories
   - Correlation and diversification benefits
   - Capital constraints and financing capacity
   - Timing optimization and sequencing
   - Resource allocation and capability requirements
   
   **Decision Framework:**
   - Investment committee governance structure
   - Approval thresholds and escalation criteria
   - Performance monitoring and review processes
   - Course correction and exit criteria
   - Portfolio rebalancing triggers

4. **CAPITAL ALLOCATION SCENARIOS**
   - Conservative allocation (capital preservation focus)
   - Balanced allocation (growth and returns optimization)
   - Aggressive allocation (growth and market share focus)
   - Defensive allocation (competitive protection focus)
   - Opportunistic allocation (market disruption response)

5. **IMPLEMENTATION AND GOVERNANCE**
   - Annual capital allocation planning process
   - Quarterly investment review and adjustment
   - Performance tracking and success metrics
   - Stakeholder communication and reporting
   - Continuous improvement and learning integration

**STRATEGIC RECOMMENDATIONS:**
- Optimal capital allocation strategy
- Investment prioritization and sequencing
- Resource requirements and capability gaps
- Risk management and hedging strategies
- Performance measurement and accountability

{industry_context}
{role_focus}
{regulatory_considerations}

Focus on maximizing shareholder value while maintaining financial strength and strategic flexibility.
""",
            variables={
                "strategic_priorities": "growth and transformation"
            },
            quality_criteria=[
                "Comprehensive investment categorization and evaluation criteria",
                "Quantitative optimization framework with risk-return analysis",
                "Clear decision governance and approval processes",
                "Scenario-based allocation strategies",
                "Implementation roadmap with performance tracking"
            ],
            tags=["capital_allocation", "investment_prioritization", "portfolio_optimization", "resource_allocation"]
        )
        
        # Cost-Benefit Analysis
        self.templates['cost_benefit_analysis'] = PromptTemplate(
            name="Executive Cost-Benefit Analysis Framework",
            category=PromptCategory.FINANCIAL_ANALYSIS,
            base_prompt="""
Conduct comprehensive cost-benefit analysis for {investment_initiative} with full quantification of costs, benefits, and strategic value creation.

**COST-BENEFIT ANALYSIS FRAMEWORK:**

1. **COMPREHENSIVE COST ANALYSIS**
   
   **Direct Costs:**
   - Initial capital investment and setup costs
   - Technology and infrastructure expenses
   - Personnel and training costs
   - Operating expenses and ongoing costs
   - Implementation and project management costs
   
   **Indirect Costs:**
   - Opportunity costs of alternative investments
   - Disruption and transition costs
   - Risk management and insurance costs
   - Compliance and regulatory costs
   - Financing costs and cost of capital
   
   **Hidden and Contingent Costs:**
   - Change management and organizational costs
   - Integration and system complexity costs
   - Vendor management and contract costs
   - Exit and termination costs
   - Contingency and risk buffer costs

2. **COMPREHENSIVE BENEFIT QUANTIFICATION**
   
   **Revenue Benefits:**
   - Direct revenue generation and growth
   - Market share gains and customer acquisition
   - Pricing optimization and margin improvement
   - Cross-selling and customer lifetime value
   - New market access and expansion benefits
   
   **Cost Reduction Benefits:**
   - Operational efficiency and automation savings
   - Process improvement and standardization
   - Scale economies and purchasing power
   - Error reduction and quality improvements
   - Regulatory and compliance cost savings
   
   **Strategic Benefits:**
   - Competitive advantage and market positioning
   - Capability building and knowledge creation
   - Option value and future opportunity creation
   - Risk reduction and business continuity
   - Brand and reputation enhancement

3. **FINANCIAL MODELING AND VALUATION**
   - Cash flow projection and timing analysis
   - Net present value (NPV) calculation
   - Benefit-cost ratio (BCR) assessment
   - Internal rate of return (IRR) analysis
   - Sensitivity analysis and scenario modeling

4. **RISK-ADJUSTED ANALYSIS**
   - Risk factor identification and quantification
   - Probability-weighted benefit estimation
   - Risk-adjusted discount rate application
   - Contingency planning and cost estimation
   - Value-at-risk and stress testing

5. **STRATEGIC VALUE INTEGRATION**
   - Quantifiable strategic benefits
   - Non-quantifiable strategic considerations
   - Portfolio and synergy effects
   - Long-term value creation potential
   - Competitive and market implications

**DECISION RECOMMENDATION:**
- Clear cost-benefit summary and recommendation
- Risk assessment and mitigation strategies
- Implementation timeline and resource requirements
- Success metrics and performance monitoring
- Alternative scenarios and contingency planning

{industry_context}
{role_focus}
{investment_initiative} specific considerations and industry benchmarks.

Provide comprehensive quantitative analysis with clear decision support and strategic context.
""",
            variables={
                "investment_initiative": "strategic initiative"
            },
            quality_criteria=[
                "Comprehensive cost identification and quantification",
                "Thorough benefit analysis with strategic value inclusion",
                "Risk-adjusted financial modeling and valuation",
                "Clear decision recommendation with supporting analysis",
                "Implementation guidance with success metrics"
            ],
            tags=["cost_benefit_analysis", "financial_evaluation", "investment_analysis", "decision_support"]
        )
        
        # Register templates
        for template in self.templates.values():
            prompt_manager.register_template(template)
    
    def generate_investment_analysis_prompt(self, config: InvestmentConfig,
                                          context: Dict[str, Any]) -> str:
        """Generate comprehensive investment analysis prompt."""
        template = self.templates['comprehensive_investment_analysis']
        
        investment_amount_text = f"${config.investment_amount:,.0f}" if config.investment_amount else "TBD"
        
        variables = {
            'investment_type': config.investment_type.value.replace('_', ' '),
            'investment_amount': investment_amount_text,
            'time_horizon': config.time_horizon
        }
        
        prompt = template.base_prompt
        for key, value in variables.items():
            prompt = prompt.replace(f"{{{key}}}", str(value))
        
        adapted_prompt = context_adapter.adapt_prompt(prompt, context.get('prompt_context'))
        
        return adapted_prompt
    
    def generate_capital_allocation_prompt(self, strategic_priorities: str,
                                         context: Dict[str, Any]) -> str:
        """Generate capital allocation framework prompt."""
        template = self.templates['capital_allocation_framework']
        
        variables = {
            'strategic_priorities': strategic_priorities
        }
        
        prompt = template.base_prompt
        for key, value in variables.items():
            prompt = prompt.replace(f"{{{key}}}", str(value))
        
        adapted_prompt = context_adapter.adapt_prompt(prompt, context.get('prompt_context'))
        
        return adapted_prompt
    
    def generate_cost_benefit_prompt(self, investment_initiative: str,
                                   context: Dict[str, Any]) -> str:
        """Generate cost-benefit analysis prompt."""
        template = self.templates['cost_benefit_analysis']
        
        variables = {
            'investment_initiative': investment_initiative
        }
        
        prompt = template.base_prompt
        for key, value in variables.items():
            prompt = prompt.replace(f"{{{key}}}", str(value))
        
        adapted_prompt = context_adapter.adapt_prompt(prompt, context.get('prompt_context'))
        
        return adapted_prompt
    
    def get_financial_evaluation_metrics(self) -> Dict[str, Dict[str, Any]]:
        """Generate comprehensive financial evaluation metrics framework."""
        return {
            'profitability_metrics': {
                'description': 'Measures of investment profitability and returns',
                'metrics': [
                    'Net Present Value (NPV)',
                    'Internal Rate of Return (IRR)',
                    'Modified Internal Rate of Return (MIRR)',
                    'Return on Investment (ROI)',
                    'Return on Assets (ROA)',
                    'Return on Equity (ROE)',
                    'Economic Value Added (EVA)'
                ],
                'industry_benchmarks': {
                    'technology': {'min_irr': 15, 'target_irr': 25},
                    'financial_services': {'min_irr': 12, 'target_irr': 18},
                    'healthcare': {'min_irr': 10, 'target_irr': 20}
                }
            },
            'cash_flow_metrics': {
                'description': 'Measures of cash generation and timing',
                'metrics': [
                    'Free Cash Flow (FCF)',
                    'Cash Flow Return on Investment (CFROI)',
                    'Cash Payback Period',
                    'Discounted Payback Period',
                    'Cash Flow Coverage Ratio'
                ]
            },
            'risk_adjusted_metrics': {
                'description': 'Risk-adjusted performance measures',
                'metrics': [
                    'Risk-Adjusted NPV',
                    'Sharpe Ratio for Investments',
                    'Value at Risk (VaR)',
                    'Conditional Value at Risk (CVaR)',
                    'Real Options Value'
                ]
            },
            'strategic_metrics': {
                'description': 'Strategic and non-financial performance measures',
                'metrics': [
                    'Market Share Impact',
                    'Customer Acquisition Cost (CAC)',
                    'Customer Lifetime Value (CLV)',
                    'Time to Market',
                    'Competitive Advantage Duration'
                ]
            }
        }
    
    def generate_investment_decision_matrix(self) -> Dict[str, Any]:
        """Generate investment decision criteria matrix."""
        return {
            'decision_criteria': {
                'financial_criteria': {
                    'weight': 0.4,
                    'sub_criteria': [
                        {'name': 'NPV', 'weight': 0.3, 'threshold': 'positive'},
                        {'name': 'IRR', 'weight': 0.3, 'threshold': 'above_hurdle'},
                        {'name': 'Payback', 'weight': 0.2, 'threshold': 'within_target'},
                        {'name': 'Cash_Flow', 'weight': 0.2, 'threshold': 'positive_cumulative'}
                    ]
                },
                'strategic_criteria': {
                    'weight': 0.3,
                    'sub_criteria': [
                        {'name': 'Strategic_Fit', 'weight': 0.4, 'scale': '1-10'},
                        {'name': 'Competitive_Advantage', 'weight': 0.3, 'scale': '1-10'},
                        {'name': 'Market_Opportunity', 'weight': 0.3, 'scale': '1-10'}
                    ]
                },
                'execution_criteria': {
                    'weight': 0.2,
                    'sub_criteria': [
                        {'name': 'Implementation_Risk', 'weight': 0.4, 'scale': '1-10'},
                        {'name': 'Capability_Fit', 'weight': 0.3, 'scale': '1-10'},
                        {'name': 'Resource_Availability', 'weight': 0.3, 'scale': '1-10'}
                    ]
                },
                'risk_criteria': {
                    'weight': 0.1,
                    'sub_criteria': [
                        {'name': 'Market_Risk', 'weight': 0.3, 'scale': '1-10'},
                        {'name': 'Technology_Risk', 'weight': 0.3, 'scale': '1-10'},
                        {'name': 'Regulatory_Risk', 'weight': 0.4, 'scale': '1-10'}
                    ]
                }
            },
            'scoring_methodology': 'Weighted average of criteria scores',
            'decision_thresholds': {
                'approve': 7.0,
                'conditional_approve': 6.0,
                'defer': 5.0,
                'reject': 'below_5.0'
            }
        }
    
    def generate_sensitivity_analysis_framework(self) -> Dict[str, Any]:
        """Generate sensitivity analysis framework for investment evaluation."""
        return {
            'key_variables': [
                'Revenue growth rate',
                'Market share capture',
                'Implementation costs',
                'Operating margin',
                'Discount rate',
                'Project timeline',
                'Competitive response',
                'Market size'
            ],
            'sensitivity_ranges': {
                'revenue_growth': {'base': 10, 'range': [-5, +15]},
                'costs': {'base': 100, 'range': [80, 130]},
                'timeline': {'base': 24, 'range': [18, 36]}
            },
            'analysis_types': [
                'One-way sensitivity (tornado diagram)',
                'Two-way sensitivity (data tables)',
                'Monte Carlo simulation',
                'Scenario analysis (optimistic/base/pessimistic)',
                'Break-even analysis'
            ],
            'output_metrics': [
                'NPV sensitivity ranges',
                'IRR breakeven points',
                'Probability of positive NPV',
                'Value at risk percentiles',
                'Key driver identification'
            ]
        }


# Global ROI investment evaluator instance
roi_investment_evaluator = ROIInvestmentEvaluator()