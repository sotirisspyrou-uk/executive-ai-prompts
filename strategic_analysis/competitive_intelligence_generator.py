"""
Executive AI Prompts - Competitive Intelligence Generator

Advanced competitive analysis and intelligence gathering prompts for strategic
decision-making, competitive positioning, and market response strategies.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from prompt_manager import PromptTemplate, PromptCategory, prompt_manager
from context_adapter import context_adapter


@dataclass
class CompetitiveAnalysisConfig:
    """Configuration for competitive intelligence analysis."""
    primary_competitors: List[str] = field(default_factory=list)
    analysis_scope: str = "comprehensive"  # "comprehensive", "focused", "threat_assessment"
    time_horizon: str = "12 months"
    strategic_focus: str = "market_position"  # "market_position", "innovation", "financial", "operational"
    intelligence_depth: str = "executive"  # "executive", "detailed", "tactical"
    response_planning: bool = True
    scenario_analysis: bool = True


class CompetitiveIntelligenceGenerator:
    """Advanced competitive intelligence and analysis prompt generator."""
    
    def __init__(self):
        self.templates = {}
        self._initialize_templates()
    
    def _initialize_templates(self) -> None:
        """Initialize competitive intelligence analysis templates."""
        
        # Comprehensive Competitive Analysis
        self.templates['comprehensive_competitor_analysis'] = PromptTemplate(
            name="Comprehensive Competitive Intelligence Analysis",
            category=PromptCategory.STRATEGIC_ANALYSIS,
            base_prompt="""
As chief competitive intelligence officer reporting to the {role}, conduct a comprehensive competitive analysis focusing on {primary_competitors} over a {time_horizon} timeframe.

**COMPETITIVE INTELLIGENCE FRAMEWORK:**

1. **COMPETITOR PROFILE & POSITIONING**
   - Business model and value proposition analysis
   - Market positioning and competitive advantages
   - Financial performance and investment capacity
   - Leadership team and strategic direction
   - Organizational culture and capabilities

2. **STRATEGIC INITIATIVES ASSESSMENT**
   - Current strategic priorities and investments
   - Product development and innovation pipeline
   - Market expansion and M&A activities
   - Digital transformation and technology investments
   - Partnership and ecosystem development

3. **MARKET PERFORMANCE ANALYSIS**
   - Market share trends and customer acquisition
   - Revenue growth and profitability metrics
   - Pricing strategies and promotional activities
   - Customer satisfaction and loyalty indicators
   - Brand strength and market perception

4. **OPERATIONAL CAPABILITIES EVALUATION**
   - Core competencies and differentiation factors
   - Technology infrastructure and innovation capacity
   - Supply chain and operational efficiency
   - Human capital and talent acquisition
   - Financial resources and capital allocation

5. **COMPETITIVE THREAT ASSESSMENT**
   - Direct competition and market overlap
   - Potential disruption and substitution threats
   - New entrant risks and market dynamics
   - Regulatory and policy impact analysis
   - Technology and innovation disruption potential

6. **COMPETITIVE RESPONSE STRATEGIES**
   - Defensive positioning and market protection
   - Offensive strategies and competitive attacks
   - Partnership and collaboration opportunities
   - Innovation and differentiation responses
   - Pricing and promotional countermeasures

**STRATEGIC IMPLICATIONS:**
- Competitive advantage gaps and opportunities
- Market position strengthening strategies
- Investment priorities and resource allocation
- Risk mitigation and contingency planning
- Long-term competitive sustainability

{industry_context}
{role_focus}
{regulatory_considerations}

Provide actionable intelligence that directly informs strategic decision-making and competitive positioning.

{communication_guidance}
""",
            variables={
                "primary_competitors": "",
                "time_horizon": "12 months",
                "strategic_focus": "market_position"
            },
            context_adaptations={
                "financial_services": "Focus on regulatory positioning, capital strength, digital banking capabilities, and fintech disruption threats.",
                "technology": "Emphasize platform strategies, ecosystem development, IP portfolios, and technical talent acquisition.",
                "healthcare": "Include regulatory pipeline, clinical capabilities, payer relationships, and value-based care positioning.",
                "ceo": "Frame analysis for strategic planning sessions with focus on competitive differentiation and market leadership.",
                "cfo": "Emphasize financial performance benchmarking, investment efficiency, and capital allocation implications."
            },
            quality_criteria=[
                "Comprehensive competitor profiling with strategic insights",
                "Quantitative performance benchmarking with credible data",
                "Clear threat assessment with probability and impact analysis",
                "Actionable competitive response strategies",
                "Strategic implications for decision-making"
            ],
            tags=["competitive_analysis", "competitive_intelligence", "market_positioning", "threat_assessment"]
        )
        
        # Competitive Threat Assessment
        self.templates['competitive_threat_assessment'] = PromptTemplate(
            name="Strategic Competitive Threat Assessment",
            category=PromptCategory.STRATEGIC_ANALYSIS,
            base_prompt="""
Conduct an urgent competitive threat assessment focusing on emerging competitive risks and strategic responses for our {industry} organization.

**THREAT ASSESSMENT FRAMEWORK:**

1. **IMMEDIATE COMPETITIVE THREATS (0-6 months)**
   - Direct competitor aggressive moves
   - Pricing pressure and margin compression
   - Customer defection and market share loss
   - Product/service competitive challenges
   - Regulatory or policy changes favoring competitors

2. **EMERGING THREATS (6-18 months)**
   - New entrant market penetration
   - Technology disruption and innovation
   - Business model transformation threats
   - Partnership and ecosystem shifts
   - Talent and capability drain risks

3. **STRATEGIC THREATS (18+ months)**
   - Market structure transformation
   - Industry convergence and boundary shifts
   - Platform and ecosystem displacement
   - Regulatory framework changes
   - Macro-economic and geopolitical shifts

4. **THREAT IMPACT ANALYSIS**
   - Revenue and market share impact
   - Profitability and margin pressure
   - Strategic position deterioration
   - Competitive advantage erosion
   - Long-term sustainability risks

5. **COMPETITIVE RESPONSE OPTIONS**
   - Immediate defensive measures
   - Strategic repositioning initiatives
   - Investment and capability building
   - Partnership and acquisition strategies
   - Innovation and differentiation accelerators

6. **SCENARIO-BASED RESPONSE PLANNING**
   - Best case: limited competitive impact
   - Base case: moderate competitive pressure
   - Worst case: severe competitive disruption
   - Black swan: unexpected market transformation

**CRISIS RESPONSE RECOMMENDATIONS:**
- Immediate action items and timeline
- Resource mobilization and allocation
- Communication and stakeholder management
- Performance monitoring and adjustment triggers
- Long-term strategic repositioning plan

{industry_context}
{urgency_level}: Provide immediate actionable recommendations for competitive threat response.
{regulatory_considerations}

Focus on time-sensitive decisions and rapid response capabilities.
""",
            variables={
                "industry": "",
                "urgency_level": "high"
            },
            quality_criteria=[
                "Comprehensive threat identification across time horizons",
                "Quantified impact assessment with scenarios",
                "Immediate and long-term response strategies",
                "Clear prioritization and resource allocation",
                "Crisis management and communication planning"
            ],
            tags=["threat_assessment", "competitive_response", "crisis_management", "strategic_defense"]
        )
        
        # Market Position Analysis
        self.templates['market_position_analysis'] = PromptTemplate(
            name="Strategic Market Position Analysis",
            category=PromptCategory.STRATEGIC_ANALYSIS,
            base_prompt="""
Analyze our current market position relative to key competitors and develop strategies for competitive advantage strengthening in the {market_segment} market.

**MARKET POSITION ANALYSIS FRAMEWORK:**

1. **CURRENT COMPETITIVE POSITION**
   - Market share and ranking analysis
   - Competitive differentiation assessment
   - Value proposition comparison
   - Customer perception and preference
   - Brand strength and recognition metrics

2. **COMPETITIVE ADVANTAGE EVALUATION**
   - Core competency assessment
   - Sustainable competitive advantages
   - Competitive moats and barriers
   - Resource-based advantage analysis
   - Dynamic capability evaluation

3. **COMPETITOR POSITIONING MAP**
   - Strategic group analysis
   - Competitive dimension mapping
   - White space identification
   - Positioning gap analysis
   - Optimal positioning assessment

4. **MARKET DYNAMICS IMPACT**
   - Industry evolution and trends
   - Customer behavior shifts
   - Technology disruption effects
   - Regulatory environment changes
   - Economic and market forces

5. **POSITIONING STRATEGY OPTIONS**
   - Defensive positioning strategies
   - Offensive market positioning
   - Niche and specialization strategies
   - Platform and ecosystem positioning
   - Innovation-led differentiation

6. **IMPLEMENTATION ROADMAP**
   - Positioning strategy selection
   - Investment and resource requirements
   - Timeline and milestone planning
   - Success metrics and monitoring
   - Risk management and contingencies

**STRATEGIC RECOMMENDATIONS:**
- Optimal competitive positioning strategy
- Investment priorities and resource allocation
- Competitive advantage building initiatives
- Market position defense and enhancement
- Long-term sustainability planning

{industry_context}
{role_focus}
{market_segment} market-specific considerations and opportunities.

Provide clear strategic direction for competitive positioning and market leadership.
""",
            variables={
                "market_segment": ""
            },
            quality_criteria=[
                "Comprehensive competitive position assessment",
                "Clear competitive advantage evaluation",
                "Strategic positioning options with trade-offs",
                "Implementation roadmap with timelines",
                "Measurable success criteria and KPIs"
            ],
            tags=["market_positioning", "competitive_advantage", "strategic_positioning", "market_leadership"]
        )
        
        # Register templates
        for template in self.templates.values():
            prompt_manager.register_template(template)
    
    def generate_competitive_analysis_prompt(self, config: CompetitiveAnalysisConfig,
                                           context: Dict[str, Any]) -> str:
        """Generate comprehensive competitive analysis prompt."""
        template = self.templates['comprehensive_competitor_analysis']
        
        competitors_text = ", ".join(config.primary_competitors) if config.primary_competitors else "key market competitors"
        
        variables = {
            'primary_competitors': competitors_text,
            'time_horizon': config.time_horizon,
            'strategic_focus': config.strategic_focus
        }
        
        prompt = template.base_prompt
        for key, value in variables.items():
            prompt = prompt.replace(f"{{{key}}}", str(value))
        
        adapted_prompt = context_adapter.adapt_prompt(prompt, context.get('prompt_context'))
        
        return adapted_prompt
    
    def generate_threat_assessment_prompt(self, config: CompetitiveAnalysisConfig,
                                        context: Dict[str, Any]) -> str:
        """Generate competitive threat assessment prompt."""
        template = self.templates['competitive_threat_assessment']
        
        variables = {
            'industry': context.get('industry', 'our industry')
        }
        
        prompt = template.base_prompt
        for key, value in variables.items():
            prompt = prompt.replace(f"{{{key}}}", str(value))
        
        adapted_prompt = context_adapter.adapt_prompt(prompt, context.get('prompt_context'))
        
        return adapted_prompt
    
    def generate_market_position_prompt(self, market_segment: str,
                                      context: Dict[str, Any]) -> str:
        """Generate market position analysis prompt."""
        template = self.templates['market_position_analysis']
        
        variables = {
            'market_segment': market_segment
        }
        
        prompt = template.base_prompt
        for key, value in variables.items():
            prompt = prompt.replace(f"{{{key}}}", str(value))
        
        adapted_prompt = context_adapter.adapt_prompt(prompt, context.get('prompt_context'))
        
        return adapted_prompt
    
    def get_competitive_intelligence_framework(self) -> Dict[str, List[str]]:
        """Generate comprehensive competitive intelligence collection framework."""
        return {
            'financial_intelligence': [
                'Revenue and profitability trends',
                'Investment and capital allocation',
                'Cost structure and efficiency metrics',
                'Financial ratios and benchmarking',
                'Funding and capital raising activities'
            ],
            'strategic_intelligence': [
                'Strategic priorities and initiatives',
                'M&A activities and partnerships',
                'Market expansion and entry strategies',
                'Innovation and R&D investments',
                'Organizational changes and restructuring'
            ],
            'operational_intelligence': [
                'Product development and launches',
                'Technology and infrastructure investments',
                'Supply chain and operational changes',
                'Talent acquisition and key hires',
                'Customer service and experience improvements'
            ],
            'market_intelligence': [
                'Customer acquisition and retention',
                'Pricing strategies and promotional activities',
                'Brand and marketing campaigns',
                'Sales performance and channel strategies',
                'Market share and competitive wins/losses'
            ],
            'leadership_intelligence': [
                'Executive team changes and appointments',
                'Board composition and governance',
                'Strategic vision and public statements',
                'Investor relations and communications',
                'Regulatory and policy engagement'
            ]
        }
    
    def generate_competitive_response_matrix(self) -> Dict[str, Dict[str, str]]:
        """Generate competitive response strategy matrix."""
        return {
            'pricing_pressure': {
                'defensive': 'Cost optimization and value-based pricing',
                'offensive': 'Strategic pricing and market penetration',
                'collaborative': 'Industry pricing discipline and standards'
            },
            'product_competition': {
                'defensive': 'Product enhancement and differentiation',
                'offensive': 'Innovation acceleration and market disruption',
                'collaborative': 'Standards development and ecosystem building'
            },
            'market_encroachment': {
                'defensive': 'Customer retention and loyalty programs',
                'offensive': 'Market expansion and territory protection',
                'collaborative': 'Strategic partnerships and alliances'
            },
            'talent_competition': {
                'defensive': 'Retention strategies and culture strengthening',
                'offensive': 'Strategic talent acquisition and development',
                'collaborative': 'Industry talent development and standards'
            },
            'technology_disruption': {
                'defensive': 'Technology upgrade and modernization',
                'offensive': 'Disruptive innovation and platform development',
                'collaborative': 'Industry standards and technology partnerships'
            }
        }
    
    def generate_competitor_monitoring_checklist(self) -> List[str]:
        """Generate comprehensive competitor monitoring checklist."""
        return [
            "Financial performance and reporting analysis",
            "Strategic announcement and press release tracking",
            "Product launch and innovation monitoring",
            "Leadership changes and executive communications",
            "Investment and M&A activity surveillance",
            "Patent filing and IP development tracking",
            "Customer feedback and review analysis",
            "Pricing and promotional activity monitoring",
            "Partnership and alliance announcement tracking",
            "Regulatory filing and compliance monitoring",
            "Social media and digital presence analysis",
            "Industry conference and event participation",
            "Analyst and media coverage assessment",
            "Talent acquisition and job posting analysis",
            "Technology infrastructure and capability assessment"
        ]
    
    def generate_war_gaming_scenarios(self, competitors: List[str]) -> Dict[str, Dict[str, Any]]:
        """Generate competitive war-gaming scenarios."""
        scenarios = {}
        
        for competitor in competitors:
            scenarios[competitor] = {
                'aggressive_expansion': {
                    'description': f'{competitor} launches aggressive market expansion',
                    'probability': 'medium',
                    'impact': 'high',
                    'response_options': [
                        'Defensive market protection',
                        'Counter-expansion strategy',
                        'Strategic partnership formation'
                    ]
                },
                'disruptive_innovation': {
                    'description': f'{competitor} introduces disruptive technology/service',
                    'probability': 'medium',
                    'impact': 'very_high',
                    'response_options': [
                        'Accelerated innovation program',
                        'Strategic acquisition',
                        'Partnership with innovators'
                    ]
                },
                'price_war_initiation': {
                    'description': f'{competitor} initiates aggressive price competition',
                    'probability': 'high',
                    'impact': 'medium',
                    'response_options': [
                        'Value-based positioning',
                        'Cost optimization program',
                        'Market segmentation strategy'
                    ]
                }
            }
        
        return scenarios


# Global competitive intelligence generator instance
competitive_intelligence_generator = CompetitiveIntelligenceGenerator()