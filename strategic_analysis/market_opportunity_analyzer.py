"""
Executive AI Prompts - Market Opportunity Analyzer

Dynamic prompt generation for comprehensive market opportunity analysis,
competitive landscape assessment, and strategic market entry evaluation.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from prompt_manager import PromptTemplate, PromptCategory, prompt_manager
from context_adapter import context_adapter


@dataclass
class MarketOpportunityConfig:
    """Configuration for market opportunity analysis."""
    market_segment: str
    geographic_scope: str = "global"
    time_horizon: str = "3-5 years"
    investment_range: Optional[str] = None
    strategic_priority: str = "growth"  # "growth", "diversification", "expansion"
    risk_tolerance: str = "moderate"  # "low", "moderate", "high"
    competitive_focus: bool = True
    regulatory_analysis: bool = True
    financial_modeling: bool = True


class MarketOpportunityAnalyzer:
    """Advanced market opportunity analysis prompt generator."""
    
    def __init__(self):
        self.templates = {}
        self._initialize_templates()
    
    def _initialize_templates(self) -> None:
        """Initialize market opportunity analysis templates."""
        
        # Comprehensive Market Analysis
        self.templates['comprehensive_analysis'] = PromptTemplate(
            name="Comprehensive Market Opportunity Analysis",
            category=PromptCategory.STRATEGIC_ANALYSIS,
            base_prompt="""
As a strategic advisor to the {role} of a {company_size} {industry} company, conduct a comprehensive market opportunity analysis for {market_segment} in the {geographic_scope} market over a {time_horizon} timeframe.

**STRATEGIC CONTEXT:**
- Strategic Priority: {strategic_priority}
- Investment Capacity: {investment_range}
- Risk Tolerance: {risk_tolerance}
- {industry_context}

**ANALYSIS FRAMEWORK:**

1. **MARKET SIZING & DYNAMICS**
   - Total Addressable Market (TAM) analysis
   - Serviceable Addressable Market (SAM) assessment  
   - Serviceable Obtainable Market (SOM) estimation
   - Market growth trajectory and key drivers
   - Market maturity and lifecycle stage analysis

2. **COMPETITIVE LANDSCAPE ASSESSMENT**
   - Key competitor identification and positioning
   - Market share distribution and concentration
   - Competitive advantages and differentiation strategies
   - Barrier to entry analysis
   - Threat of substitutes evaluation

3. **OPPORTUNITY EVALUATION**
   - Revenue potential and profitability outlook
   - Strategic fit with existing capabilities
   - Required investment and resource allocation
   - Time to market and scalability considerations
   - Synergies with current business portfolio

4. **RISK ASSESSMENT**
   - Market risks (demand volatility, commoditization)
   - Competitive risks (new entrants, price wars)
   - Operational risks (capability gaps, execution challenges)
   - Regulatory and compliance risks
   - Financial and investment risks

5. **STRATEGIC RECOMMENDATIONS**
   - Market entry strategy recommendation
   - Investment prioritization and phasing
   - Competitive positioning approach
   - Success metrics and milestones
   - Risk mitigation strategies

{regulatory_considerations}
{role_focus}

Provide quantitative analysis where possible, including financial projections and sensitivity analysis. Frame recommendations in terms of strategic impact and competitive advantage creation.

{communication_guidance}
""",
            variables={
                "market_segment": "",
                "geographic_scope": "global",
                "time_horizon": "3-5 years",
                "strategic_priority": "growth",
                "investment_range": "to be determined",
                "risk_tolerance": "moderate"
            },
            context_adaptations={
                "financial_services": "Focus on regulatory capital requirements, compliance costs, and market conduct regulations. Consider Basel III impacts and stress testing scenarios.",
                "technology": "Emphasize scalability, technical moats, platform effects, and innovation velocity. Address cybersecurity and data privacy implications.",
                "healthcare": "Include clinical validation requirements, regulatory approval processes, and patient safety considerations. Address reimbursement and value-based care trends.",
                "manufacturing": "Focus on supply chain implications, operational efficiency, and quality standards. Consider sustainability and ESG factors.",
                "ceo": "Frame analysis for board presentation with emphasis on shareholder value creation and strategic positioning.",
                "cfo": "Emphasize financial modeling, capital allocation, and return on investment analysis with detailed sensitivity scenarios."
            },
            quality_criteria=[
                "Quantitative market sizing with credible data sources",
                "Comprehensive competitive analysis with strategic implications",
                "Clear investment thesis and value creation logic",
                "Robust risk assessment with mitigation strategies",
                "Actionable recommendations with implementation roadmap"
            ],
            tags=["market_analysis", "opportunity_assessment", "competitive_intelligence", "strategic_planning"]
        )
        
        # Growth Opportunity Identification
        self.templates['growth_identification'] = PromptTemplate(
            name="Growth Opportunity Identification Framework",
            category=PromptCategory.STRATEGIC_ANALYSIS,
            base_prompt="""
As chief strategic advisor, identify and prioritize growth opportunities for our {industry} organization in the {market_segment} space, focusing on {strategic_priority} over a {time_horizon} period.

**GROWTH OPPORTUNITY FRAMEWORK:**

1. **MARKET EXPANSION OPPORTUNITIES**
   - Geographic expansion potential
   - Customer segment expansion
   - Product/service line extensions
   - Channel diversification opportunities
   - Vertical integration possibilities

2. **INNOVATION-DRIVEN GROWTH**
   - Technology disruption opportunities
   - Business model innovation potential
   - Digital transformation benefits
   - Platform and ecosystem strategies
   - Sustainability-driven innovation

3. **INORGANIC GROWTH STRATEGIES**
   - Acquisition target identification
   - Strategic partnership opportunities
   - Joint venture possibilities
   - Licensing and IP monetization
   - Ecosystem participation strategies

4. **OPERATIONAL LEVERAGE OPPORTUNITIES**
   - Efficiency improvement potential
   - Process automation benefits
   - Supply chain optimization
   - Asset utilization enhancement
   - Cost structure transformation

5. **STRATEGIC PRIORITIZATION MATRIX**
   - Opportunity size and revenue potential
   - Strategic fit and capability leverage
   - Investment requirements and ROI
   - Time to value and implementation complexity
   - Risk-adjusted return analysis

**IMPLEMENTATION ROADMAP:**
- Priority ranking with rationale
- Resource allocation recommendations
- Timeline and milestone planning
- Success metrics and KPIs
- Risk mitigation and contingency planning

{industry_context}
{role_focus}
{regulatory_considerations}

Provide specific, actionable growth initiatives with clear business cases and implementation guidance.
""",
            variables={
                "market_segment": "",
                "strategic_priority": "sustainable growth",
                "time_horizon": "3-5 years"
            },
            quality_criteria=[
                "Comprehensive opportunity identification across all growth vectors",
                "Clear prioritization framework with quantitative criteria",
                "Specific implementation roadmap with timelines",
                "Risk-adjusted financial projections",
                "Alignment with strategic objectives and capabilities"
            ],
            tags=["growth_strategy", "opportunity_identification", "strategic_prioritization"]
        )
        
        # Risk-Adjusted Market Entry
        self.templates['risk_adjusted_entry'] = PromptTemplate(
            name="Risk-Adjusted Market Entry Evaluation",
            category=PromptCategory.STRATEGIC_ANALYSIS,
            base_prompt="""
Develop a risk-adjusted market entry strategy for {market_segment} considering our {risk_tolerance} risk profile and {investment_range} investment capacity.

**RISK-ADJUSTED ENTRY FRAMEWORK:**

1. **MARKET ENTRY OPTIONS ANALYSIS**
   - Organic development (build internally)
   - Acquisition-based entry (buy existing player)
   - Strategic partnership/joint venture (partner)
   - Licensing or franchise models
   - Gradual vs. aggressive entry strategies

2. **RISK ASSESSMENT MATRIX**
   - Market risks: demand uncertainty, competitive response
   - Execution risks: capability gaps, operational challenges
   - Financial risks: capital requirements, cash flow timing
   - Regulatory risks: compliance costs, approval processes
   - Reputational risks: brand impact, stakeholder perception

3. **RISK MITIGATION STRATEGIES**
   - Phased entry approach with option values
   - Strategic hedging and diversification
   - Partnership and risk-sharing structures
   - Contingency planning and exit strategies
   - Insurance and financial hedging options

4. **SCENARIO ANALYSIS**
   - Base case: most likely market development
   - Optimistic case: favorable market conditions
   - Pessimistic case: challenging market environment
   - Stress case: severe adverse conditions
   - Sensitivity analysis on key assumptions

5. **DECISION FRAMEWORK**
   - Expected value analysis across scenarios
   - Risk-adjusted return calculations
   - Option value and real options analysis
   - Break-even and payback period analysis
   - Strategic value beyond financial returns

**RECOMMENDATION SYNTHESIS:**
- Preferred entry strategy with rationale
- Investment staging and milestone gates
- Risk monitoring and management plan
- Success metrics and decision triggers
- Alternative scenarios and contingencies

{industry_context}
{regulatory_considerations}
{role_focus}

Emphasize quantitative risk assessment and provide clear decision criteria for go/no-go determinations.
""",
            variables={
                "market_segment": "",
                "risk_tolerance": "moderate",
                "investment_range": "to be determined"
            },
            quality_criteria=[
                "Comprehensive risk identification and assessment",
                "Quantitative scenario and sensitivity analysis",
                "Clear risk mitigation strategies",
                "Option value and staging analysis",
                "Actionable decision framework with criteria"
            ],
            tags=["market_entry", "risk_assessment", "scenario_analysis", "decision_framework"]
        )
        
        # Register templates
        for template in self.templates.values():
            prompt_manager.register_template(template)
    
    def generate_market_analysis_prompt(self, config: MarketOpportunityConfig,
                                      context: Dict[str, Any]) -> str:
        """Generate comprehensive market analysis prompt."""
        template = self.templates['comprehensive_analysis']
        
        variables = {
            'market_segment': config.market_segment,
            'geographic_scope': config.geographic_scope,
            'time_horizon': config.time_horizon,
            'strategic_priority': config.strategic_priority,
            'investment_range': config.investment_range or "to be determined",
            'risk_tolerance': config.risk_tolerance
        }
        
        prompt = template.base_prompt
        for key, value in variables.items():
            prompt = prompt.replace(f"{{{key}}}", str(value))
        
        # Apply context adaptations
        adapted_prompt = context_adapter.adapt_prompt(prompt, context.get('prompt_context'))
        
        return adapted_prompt
    
    def generate_growth_opportunity_prompt(self, config: MarketOpportunityConfig,
                                         context: Dict[str, Any]) -> str:
        """Generate growth opportunity identification prompt."""
        template = self.templates['growth_identification']
        
        variables = {
            'market_segment': config.market_segment,
            'strategic_priority': config.strategic_priority,
            'time_horizon': config.time_horizon
        }
        
        prompt = template.base_prompt
        for key, value in variables.items():
            prompt = prompt.replace(f"{{{key}}}", str(value))
        
        adapted_prompt = context_adapter.adapt_prompt(prompt, context.get('prompt_context'))
        
        return adapted_prompt
    
    def generate_market_entry_prompt(self, config: MarketOpportunityConfig,
                                   context: Dict[str, Any]) -> str:
        """Generate risk-adjusted market entry evaluation prompt."""
        template = self.templates['risk_adjusted_entry']
        
        variables = {
            'market_segment': config.market_segment,
            'risk_tolerance': config.risk_tolerance,
            'investment_range': config.investment_range or "to be determined"
        }
        
        prompt = template.base_prompt
        for key, value in variables.items():
            prompt = prompt.replace(f"{{{key}}}", str(value))
        
        adapted_prompt = context_adapter.adapt_prompt(prompt, context.get('prompt_context'))
        
        return adapted_prompt
    
    def get_market_analysis_checklist(self, industry: str) -> List[str]:
        """Generate industry-specific market analysis checklist."""
        base_checklist = [
            "Market size and growth rate validation",
            "Competitive landscape mapping",
            "Customer needs and pain points analysis",
            "Revenue model and pricing analysis",
            "Cost structure and profitability assessment",
            "Regulatory and compliance requirements",
            "Technology and infrastructure needs",
            "Go-to-market strategy development",
            "Risk assessment and mitigation planning",
            "Success metrics and KPI definition"
        ]
        
        industry_specific = {
            'financial_services': [
                "Regulatory capital impact assessment",
                "Credit risk and market risk evaluation",
                "Compliance and reporting requirements",
                "Customer data and privacy considerations",
                "Stress testing and scenario analysis"
            ],
            'technology': [
                "Platform scalability requirements",
                "Cybersecurity and data protection",
                "IP and patent landscape analysis",
                "Technology stack and architecture",
                "Developer ecosystem considerations"
            ],
            'healthcare': [
                "Clinical evidence and efficacy data",
                "Regulatory approval pathways",
                "Reimbursement and payer analysis",
                "Patient safety and adverse events",
                "Healthcare provider adoption factors"
            ]
        }
        
        return base_checklist + industry_specific.get(industry.lower(), [])
    
    def generate_competitive_benchmarking_framework(self) -> Dict[str, List[str]]:
        """Generate competitive benchmarking framework."""
        return {
            'market_position': [
                'Market share and revenue',
                'Customer base and segments',
                'Geographic presence',
                'Brand strength and recognition',
                'Competitive advantages'
            ],
            'financial_performance': [
                'Revenue growth and profitability',
                'Cost structure and margins',
                'Capital efficiency and ROI',
                'Investment and R&D spending',
                'Financial stability and liquidity'
            ],
            'operational_capabilities': [
                'Product portfolio and innovation',
                'Technology and infrastructure',
                'Supply chain and operations',
                'Human capital and expertise',
                'Partnership and alliances'
            ],
            'strategic_direction': [
                'Vision and strategic priorities',
                'Investment focus areas',
                'M&A and partnership strategy',
                'Digital transformation initiatives',
                'Sustainability and ESG commitments'
            ]
        }


# Global market opportunity analyzer instance
market_opportunity_analyzer = MarketOpportunityAnalyzer()