"""
Executive AI Prompts - Industry Trend Analyzer

Advanced industry trend analysis, technology disruption assessment,
and market evolution prediction for strategic decision-making.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from enum import Enum
from prompt_manager import PromptTemplate, PromptCategory, prompt_manager
from context_adapter import context_adapter


class TrendType(Enum):
    TECHNOLOGY = "technology_innovation"
    REGULATORY = "regulatory_policy"
    CONSUMER = "consumer_behavior"
    ECONOMIC = "economic_shifts"
    COMPETITIVE = "competitive_dynamics"
    SOCIAL = "social_cultural"
    ENVIRONMENTAL = "environmental_sustainability"


class TrendImpact(Enum):
    DISRUPTIVE = "disruptive_transformation"
    EVOLUTIONARY = "evolutionary_change"
    CYCLICAL = "cyclical_pattern"
    EMERGING = "emerging_development"


class TrendTimeline(Enum):
    IMMEDIATE = "0-12_months"
    SHORT_TERM = "1-3_years"
    MEDIUM_TERM = "3-7_years"
    LONG_TERM = "7_plus_years"


@dataclass
class TrendAnalysisConfig:
    """Configuration for industry trend analysis."""
    trend_types: List[TrendType] = field(default_factory=lambda: [TrendType.TECHNOLOGY, TrendType.CONSUMER])
    analysis_horizon: TrendTimeline = TrendTimeline.MEDIUM_TERM
    geographic_scope: str = "global"
    competitive_focus: bool = True
    strategic_implications: bool = True
    investment_opportunities: bool = True


class IndustryTrendAnalyzer:
    """Advanced industry trend analysis and market evolution prediction."""
    
    def __init__(self):
        self.templates = {}
        self._initialize_templates()
    
    def _initialize_templates(self) -> None:
        """Initialize industry trend analysis templates."""
        
        # Comprehensive Industry Trend Analysis
        self.templates['comprehensive_trend_analysis'] = PromptTemplate(
            name="Comprehensive Industry Trend Analysis",
            category=PromptCategory.MARKET_INTELLIGENCE,
            base_prompt="""
As Chief Strategy Officer analyzing {trend_types} trends in the {industry} sector over a {analysis_horizon} timeframe, provide comprehensive trend analysis with strategic implications and competitive positioning guidance.

**INDUSTRY TREND ANALYSIS FRAMEWORK:**

**TREND IDENTIFICATION AND CATEGORIZATION:**

**Technology Innovation Trends:**
- Artificial intelligence and machine learning adoption
- Automation and robotics integration
- Digital platform and ecosystem evolution
- Cybersecurity and data privacy advancement
- Cloud computing and infrastructure modernization
- Internet of Things (IoT) and connectivity expansion
- Blockchain and distributed ledger applications

**Consumer Behavior Evolution:**
- Digital-first preferences and expectations
- Sustainability and social responsibility demands
- Personalization and customization requirements
- Omnichannel experience and seamless integration
- Value-conscious purchasing and price sensitivity
- Health and wellness prioritization
- Remote and hybrid lifestyle adoption

**Regulatory and Policy Shifts:**
- Data privacy and protection regulations
- Environmental and sustainability mandates
- Competition and antitrust enforcement
- Industry-specific compliance requirements
- International trade and tariff policies
- Taxation and financial reporting changes
- Labor and employment law evolution

**Economic and Market Dynamics:**
- Interest rate environment and monetary policy
- Supply chain resilience and localization
- Inflation pressures and cost management
- Investment flows and capital availability
- Currency fluctuations and global trade
- Economic growth patterns and cycles
- Market consolidation and fragmentation trends

**TREND IMPACT ASSESSMENT:**

**Market Size and Growth Implications:**
- Total addressable market expansion or contraction
- Customer segment growth and evolution
- Geographic market development and maturation
- Product category emergence and obsolescence
- Service delivery model transformation
- Value chain reconfiguration and disintermediation

**Competitive Landscape Evolution:**
- New entrant threats and market disruption
- Incumbent response and adaptation strategies
- Competitive advantage sustainability and erosion
- Partnership and ecosystem collaboration trends
- Technology adoption and digital transformation
- Market share redistribution and concentration

**STRATEGIC IMPLICATIONS ANALYSIS:**

**Opportunity Identification:**
- Emerging market segments and customer needs
- Technology-enabled business model innovation
- Operational efficiency and cost optimization
- Customer experience enhancement possibilities
- New revenue stream and monetization models
- Strategic partnership and alliance opportunities

**Threat Assessment:**
- Disruptive technology and business model risks
- Regulatory compliance and policy changes
- Competitive pressure and market share erosion
- Customer preference shifts and loyalty risks
- Supply chain disruption and cost inflation
- Talent shortage and skill gap challenges

**INVESTMENT AND RESOURCE ALLOCATION:**

**Strategic Investment Priorities:**
- Technology infrastructure and platform development
- Research and development capability building
- Talent acquisition and skill development
- Market expansion and customer acquisition
- Partnership development and ecosystem participation
- Operational efficiency and automation initiatives

**Resource Reallocation Considerations:**
- Legacy system modernization and replacement
- Underperforming asset divestiture and optimization
- Geographic footprint optimization and expansion
- Product portfolio rationalization and focus
- Organizational capability development and enhancement

**IMPLEMENTATION ROADMAP:**

**Short-Term Actions (0-18 months):**
- Trend monitoring and intelligence capability building
- Pilot programs and proof-of-concept development
- Strategic partnership exploration and establishment
- Talent development and skill building initiatives
- Customer feedback and market research enhancement

**Medium-Term Strategy (18 months - 3 years):**
- Technology platform and infrastructure investment
- Business model innovation and testing
- Market expansion and customer acquisition
- Operational transformation and efficiency improvement
- Competitive positioning and differentiation enhancement

**Long-Term Positioning (3+ years):**
- Market leadership and ecosystem development
- Innovation and disruption capability building
- Sustainable competitive advantage creation
- Global expansion and scale optimization
- Industry standard setting and thought leadership

{industry_context}
{trend_types} specific analysis and implications for {industry} sector.
{role_focus}
{regulatory_considerations}

Focus on actionable strategic insights that drive competitive advantage and market leadership.

{communication_guidance}
""",
            variables={
                "trend_types": "technology and consumer behavior",
                "industry": "",
                "analysis_horizon": "3-7 years"
            },
            context_adaptations={
                "financial_services": "Include fintech disruption, regulatory technology, and digital banking trends. Address open banking, blockchain, and regulatory compliance evolution.",
                "technology": "Focus on platform evolution, AI/ML advancement, cybersecurity trends, and developer ecosystem changes. Include cloud computing and edge computing developments.",
                "healthcare": "Analyze telemedicine, personalized medicine, AI diagnostics, and value-based care trends. Include regulatory approval processes and patient experience evolution.",
                "ceo": "Frame for strategic planning and board discussion with market leadership and competitive positioning focus.",
                "cmo": "Emphasize customer behavior changes, marketing technology trends, and brand positioning implications."
            },
            quality_criteria=[
                "Comprehensive trend identification across multiple dimensions",
                "Clear impact assessment with strategic implications",
                "Actionable investment and resource allocation guidance",
                "Timeline-based implementation roadmap",
                "Competitive positioning and market leadership strategy"
            ],
            tags=["trend_analysis", "market_intelligence", "strategic_planning", "competitive_advantage"]
        )
        
        # Technology Disruption Assessment
        self.templates['technology_disruption_assessment'] = PromptTemplate(
            name="Technology Disruption and Innovation Impact Analysis",
            category=PromptCategory.MARKET_INTELLIGENCE,
            base_prompt="""
Conduct comprehensive technology disruption assessment focusing on {technology_focus} innovations and their transformative impact on the {industry} industry and competitive landscape.

**TECHNOLOGY DISRUPTION FRAMEWORK:**

**EMERGING TECHNOLOGY LANDSCAPE:**

**Artificial Intelligence and Machine Learning:**
- Generative AI and large language models
- Computer vision and image recognition
- Natural language processing and understanding
- Predictive analytics and decision automation
- Robotic process automation and intelligent automation
- Edge AI and real-time processing capabilities

**Platform and Ecosystem Technologies:**
- API-first architecture and microservices
- Low-code/no-code development platforms
- Integration platforms and middleware solutions
- Marketplace and ecosystem orchestration
- Data mesh and decentralized data architecture
- Cloud-native and containerization technologies

**Next-Generation Computing:**
- Quantum computing and cryptography
- Edge computing and distributed processing
- 5G/6G connectivity and network capabilities
- Extended reality (AR/VR/MR) applications
- Blockchain and distributed ledger technologies
- Biometric authentication and security technologies

**DISRUPTION IMPACT ASSESSMENT:**

**Business Model Transformation:**
- Platform-based business models and network effects
- Subscription and as-a-service monetization
- Data monetization and analytics-driven revenue
- Ecosystem orchestration and partnership models
- Direct-to-consumer and disintermediation
- Circular economy and sustainability integration

**Operational Efficiency Revolution:**
- Process automation and workflow optimization
- Predictive maintenance and asset optimization
- Supply chain visibility and optimization
- Real-time decision making and response
- Remote work and distributed operations
- Sustainable operations and carbon footprint reduction

**Customer Experience Innovation:**
- Personalization and hyper-customization
- Omnichannel and seamless integration
- Self-service and autonomous interactions
- Proactive and predictive service delivery
- Immersive and experiential engagement
- Community-driven and social commerce

**COMPETITIVE LANDSCAPE DISRUPTION:**

**New Entrant Threats:**
- Tech giants expanding into traditional industries
- Startup innovation and venture capital funding
- Non-traditional competitors and adjacency entry
- Platform aggregators and marketplace dominance
- Regulatory technology (RegTech) and compliance innovation
- Sustainability-focused and ESG-driven solutions

**Incumbent Response Strategies:**
- Digital transformation and modernization
- Innovation labs and corporate venture capital
- Strategic partnerships and acquisition programs
- Ecosystem development and platform building
- Talent acquisition and capability development
- Customer experience and service innovation

**TECHNOLOGY ADOPTION ROADMAP:**

**Technology Maturity Assessment:**
- Proof of concept and pilot program stage
- Early adoption and market validation phase
- Mainstream adoption and scalability achievement
- Market saturation and commodity status
- Next-generation evolution and replacement cycle

**Implementation Strategy:**
- Build vs. buy vs. partner decision framework
- Pilot program design and success criteria
- Scaling strategy and rollout planning
- Change management and adoption support
- Performance measurement and optimization
- Risk management and security considerations

**STRATEGIC RESPONSE RECOMMENDATIONS:**

**Innovation Investment Priorities:**
- Core technology capability development
- Emerging technology experimentation and piloting
- Partnership and ecosystem participation
- Talent development and skill building
- Infrastructure modernization and platform development
- Customer experience and service innovation

**Defensive and Offensive Strategies:**
- Competitive moat strengthening and differentiation
- Market leadership and standard-setting participation
- Customer lock-in and loyalty enhancement
- Operational efficiency and cost advantage
- Speed to market and innovation velocity
- Ecosystem orchestration and value capture

{industry_context}
{technology_focus} specific implications and adoption patterns in {industry} sector.

Focus on technology-enabled competitive advantage and market disruption preparation.
""",
            variables={
                "technology_focus": "artificial intelligence and automation",
                "industry": ""
            },
            quality_criteria=[
                "Comprehensive technology landscape mapping",
                "Clear disruption impact assessment with business implications",
                "Competitive response strategy recommendations",
                "Technology adoption roadmap with timeline",
                "Strategic investment and resource allocation guidance"
            ],
            tags=["technology_disruption", "innovation_analysis", "digital_transformation", "competitive_strategy"]
        )
        
        # Market Evolution Prediction
        self.templates['market_evolution_prediction'] = PromptTemplate(
            name="Market Evolution and Future Scenario Analysis",
            category=PromptCategory.MARKET_INTELLIGENCE,
            base_prompt="""
Develop comprehensive market evolution analysis with scenario-based predictions for the {market_segment} market over {prediction_timeframe}, including strategic positioning recommendations.

**MARKET EVOLUTION ANALYSIS FRAMEWORK:**

**CURRENT MARKET STATE ASSESSMENT:**

**Market Structure and Dynamics:**
- Market size, growth rate, and maturity stage
- Customer segmentation and demand patterns
- Competitive landscape and market concentration
- Value chain structure and profit distribution
- Regulatory environment and policy framework
- Technology adoption and innovation pace

**Key Success Factors and Drivers:**
- Customer value propositions and differentiation
- Operational efficiency and cost management
- Technology capabilities and innovation
- Brand strength and market positioning
- Distribution channels and market access
- Regulatory compliance and risk management

**EVOLUTIONARY FORCES AND DRIVERS:**

**Demand-Side Evolution:**
- Demographic shifts and generational changes
- Income level changes and economic development
- Lifestyle and preference evolution
- Digitization and technology adoption
- Sustainability and social consciousness
- Globalization and localization trends

**Supply-Side Transformation:**
- Technology innovation and automation
- Business model innovation and disruption
- Operational efficiency and cost reduction
- Talent and skill development
- Capital allocation and investment patterns
- Regulatory and policy adaptation

**SCENARIO-BASED MARKET PREDICTIONS:**

**Scenario 1: Accelerated Digital Transformation**
- Market characteristics and competitive dynamics
- Customer behavior and preference changes
- Technology adoption and platform dominance
- Business model evolution and monetization
- Regulatory adaptation and policy response
- Investment requirements and success factors

**Scenario 2: Sustainable and Conscious Consumption**
- ESG-driven market evolution and customer demands
- Circular economy and sustainability integration
- Regulatory pressure and compliance requirements
- Brand positioning and value proposition shifts
- Supply chain transformation and transparency
- Investment in sustainable technologies and practices

**Scenario 3: Economic Pressure and Value Focus**
- Price sensitivity and value-conscious behavior
- Market consolidation and efficiency focus
- Cost optimization and operational excellence
- Technology adoption for efficiency gains
- Regulatory relaxation and policy support
- Investment in automation and productivity

**Scenario 4: Regulatory Intensive Environment**
- Compliance-driven market evolution
- Technology adoption for regulatory efficiency
- Market structure changes and entry barriers
- Customer protection and privacy enhancement
- International coordination and standardization
- Investment in regulatory technology and compliance

**STRATEGIC POSITIONING IMPLICATIONS:**

**Market Position Optimization:**
- Competitive advantage development and sustainability
- Customer segment focus and value proposition
- Geographic expansion and market penetration
- Product portfolio optimization and innovation
- Channel strategy and distribution excellence
- Brand positioning and market perception

**Investment and Resource Allocation:**
- Technology infrastructure and platform development
- Innovation and R&D capability building
- Market expansion and customer acquisition
- Operational efficiency and automation
- Talent development and organizational capability
- Strategic partnerships and ecosystem participation

**ADAPTIVE STRATEGY DEVELOPMENT:**

**Scenario Monitoring and Triggers:**
- Key indicators and early warning signals
- Market research and intelligence capabilities
- Stakeholder feedback and sentiment analysis
- Regulatory monitoring and policy tracking
- Technology development and adoption patterns
- Competitive activity and market response

**Strategic Flexibility and Options:**
- Multiple scenario preparation and planning
- Real options and staged investment approach
- Partnership and alliance development
- Technology platform and capability building
- Geographic diversification and risk spreading
- Portfolio optimization and resource reallocation

{industry_context}
{market_segment} specific evolution patterns and industry dynamics.
{prediction_timeframe} market outlook and strategic considerations.

Focus on strategic agility and adaptive capability development for market evolution.
""",
            variables={
                "market_segment": "",
                "prediction_timeframe": "5-10 years"
            },
            quality_criteria=[
                "Comprehensive current market assessment",
                "Multiple scenario development with clear predictions",
                "Strategic positioning recommendations for each scenario",
                "Adaptive strategy framework with monitoring triggers",
                "Investment and resource allocation guidance"
            ],
            tags=["market_evolution", "scenario_analysis", "strategic_positioning", "future_planning"]
        )
        
        # Register templates
        for template in self.templates.values():
            prompt_manager.register_template(template)
    
    def generate_trend_analysis_prompt(self, config: TrendAnalysisConfig,
                                     context: Dict[str, Any]) -> str:
        """Generate comprehensive industry trend analysis prompt."""
        template = self.templates['comprehensive_trend_analysis']
        
        trend_types_text = " and ".join([t.value.replace('_', ' ') for t in config.trend_types])
        
        variables = {
            'trend_types': trend_types_text,
            'industry': context.get('industry', 'target industry'),
            'analysis_horizon': config.analysis_horizon.value.replace('_', ' ')
        }
        
        prompt = template.base_prompt
        for key, value in variables.items():
            prompt = prompt.replace(f"{{{key}}}", str(value))
        
        adapted_prompt = context_adapter.adapt_prompt(prompt, context.get('prompt_context'))
        
        return adapted_prompt
    
    def generate_technology_disruption_prompt(self, technology_focus: str, industry: str,
                                            context: Dict[str, Any]) -> str:
        """Generate technology disruption assessment prompt."""
        template = self.templates['technology_disruption_assessment']
        
        variables = {
            'technology_focus': technology_focus,
            'industry': industry
        }
        
        prompt = template.base_prompt
        for key, value in variables.items():
            prompt = prompt.replace(f"{{{key}}}", str(value))
        
        adapted_prompt = context_adapter.adapt_prompt(prompt, context.get('prompt_context'))
        
        return adapted_prompt
    
    def generate_market_evolution_prompt(self, market_segment: str, timeframe: str,
                                       context: Dict[str, Any]) -> str:
        """Generate market evolution prediction prompt."""
        template = self.templates['market_evolution_prediction']
        
        variables = {
            'market_segment': market_segment,
            'prediction_timeframe': timeframe
        }
        
        prompt = template.base_prompt
        for key, value in variables.items():
            prompt = prompt.replace(f"{{{key}}}", str(value))
        
        adapted_prompt = context_adapter.adapt_prompt(prompt, context.get('prompt_context'))
        
        return adapted_prompt
    
    def get_trend_monitoring_framework(self) -> Dict[str, List[str]]:
        """Generate comprehensive trend monitoring framework."""
        return {
            'technology_indicators': [
                'Patent filing activity and innovation metrics',
                'Venture capital investment and startup funding',
                'Technology adoption rates and user engagement',
                'Platform usage and developer activity',
                'Research publication and academic development',
                'Industry conference themes and discussions',
                'Technology vendor announcements and roadmaps'
            ],
            'consumer_indicators': [
                'Consumer survey results and preference studies',
                'Social media sentiment and discussion trends',
                'E-commerce behavior and purchase patterns',
                'Mobile app usage and engagement metrics',
                'Search trend analysis and keyword research',
                'Demographic shift and generational studies',
                'Lifestyle and behavior research reports'
            ],
            'regulatory_indicators': [
                'Legislative proposal and policy development',
                'Regulatory agency statements and guidance',
                'Industry consultation and public comment',
                'International regulatory coordination',
                'Enforcement action and compliance trends',
                'Legal precedent and court decisions',
                'Policy think tank and advocacy positions'
            ],
            'competitive_indicators': [
                'Competitor product launches and announcements',
                'Strategic partnership and acquisition activity',
                'Executive hiring and organizational changes',
                'Investment and capital allocation patterns',
                'Market share and performance metrics',
                'Customer feedback and satisfaction trends',
                'Industry analyst reports and recommendations'
            ]
        }
    
    def generate_trend_impact_matrix(self) -> Dict[str, Dict[str, str]]:
        """Generate trend impact assessment matrix."""
        return {
            'high_impact_high_probability': {
                'description': 'Certain disruption requiring immediate preparation',
                'strategic_response': 'Proactive investment and capability building',
                'timeline': 'Immediate action within 6-12 months',
                'resource_allocation': 'Significant investment and priority focus'
            },
            'high_impact_low_probability': {
                'description': 'Potential major disruption requiring monitoring',
                'strategic_response': 'Option development and scenario planning',
                'timeline': 'Monitoring with contingency planning',
                'resource_allocation': 'Limited investment in options and capabilities'
            },
            'low_impact_high_probability': {
                'description': 'Gradual change requiring adaptation',
                'strategic_response': 'Incremental adjustment and optimization',
                'timeline': 'Gradual implementation over 1-2 years',
                'resource_allocation': 'Moderate investment in process improvement'
            },
            'low_impact_low_probability': {
                'description': 'Minor change with limited implications',
                'strategic_response': 'Monitoring and periodic review',
                'timeline': 'Passive monitoring with annual review',
                'resource_allocation': 'Minimal investment in intelligence gathering'
            }
        }
    
    def generate_innovation_opportunity_framework(self) -> Dict[str, Any]:
        """Generate innovation opportunity identification framework."""
        return {
            'opportunity_categories': {
                'customer_pain_points': [
                    'Unmet needs and service gaps',
                    'Process friction and inefficiency',
                    'Cost and affordability challenges',
                    'Accessibility and convenience barriers',
                    'Quality and reliability issues'
                ],
                'technology_enablers': [
                    'Automation and efficiency opportunities',
                    'Data and analytics applications',
                    'Platform and ecosystem development',
                    'Integration and interoperability solutions',
                    'Security and privacy enhancements'
                ],
                'market_whitespace': [
                    'Underserved customer segments',
                    'Geographic expansion opportunities',
                    'Adjacent market applications',
                    'New use cases and applications',
                    'Cross-industry collaboration potential'
                ]
            },
            'evaluation_criteria': {
                'market_attractiveness': [
                    'Market size and growth potential',
                    'Customer willingness to pay',
                    'Competitive intensity and barriers',
                    'Regulatory environment and support',
                    'Technology maturity and adoption'
                ],
                'strategic_fit': [
                    'Core competency alignment',
                    'Brand and reputation compatibility',
                    'Resource and capability requirements',
                    'Strategic objective contribution',
                    'Risk profile and tolerance'
                ]
            }
        }


# Global industry trend analyzer instance
industry_trend_analyzer = IndustryTrendAnalyzer()