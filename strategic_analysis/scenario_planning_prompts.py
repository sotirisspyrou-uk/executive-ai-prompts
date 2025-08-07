"""
Executive AI Prompts - Scenario Planning Generator

Advanced scenario planning and strategic option evaluation frameworks
for executive decision-making under uncertainty.
"""

from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field
from enum import Enum
from prompt_manager import PromptTemplate, PromptCategory, prompt_manager
from context_adapter import context_adapter


class ScenarioType(Enum):
    ECONOMIC = "economic"
    COMPETITIVE = "competitive" 
    REGULATORY = "regulatory"
    TECHNOLOGY = "technology"
    GEOPOLITICAL = "geopolitical"
    OPERATIONAL = "operational"


@dataclass
class ScenarioConfig:
    """Configuration for scenario planning analysis."""
    scenario_types: List[ScenarioType] = field(default_factory=lambda: [ScenarioType.ECONOMIC, ScenarioType.COMPETITIVE])
    time_horizon: str = "3-5 years"
    scenario_count: int = 4  # Usually optimistic, base, pessimistic, stress
    strategic_focus: str = "business_strategy"  # "business_strategy", "risk_management", "investment_planning"
    quantitative_modeling: bool = True
    stress_testing: bool = True
    option_value_analysis: bool = False


class ScenarioPlanningGenerator:
    """Advanced scenario planning and strategic option evaluation."""
    
    def __init__(self):
        self.templates = {}
        self._initialize_templates()
    
    def _initialize_templates(self) -> None:
        """Initialize scenario planning templates."""
        
        # Comprehensive Scenario Planning
        self.templates['comprehensive_scenario_planning'] = PromptTemplate(
            name="Executive Scenario Planning Framework",
            category=PromptCategory.STRATEGIC_ANALYSIS,
            base_prompt="""
As chief strategic planning officer for the {role}, develop comprehensive scenario planning analysis for strategic decision-making over a {time_horizon} timeframe, focusing on {scenario_types} scenarios.

**SCENARIO PLANNING FRAMEWORK:**

1. **SCENARIO ARCHITECTURE DEVELOPMENT**
   - Key uncertainty identification and prioritization
   - Scenario dimension mapping (2x2 or multi-dimensional)
   - Driving force analysis and interdependencies
   - Scenario narrative development and naming
   - Probability assessment and confidence intervals

2. **SCENARIO CONSTRUCTION**
   
   **OPTIMISTIC SCENARIO: "Growth Acceleration"**
   - Favorable market conditions and demand growth
   - Competitive advantage expansion
   - Regulatory tailwinds and policy support
   - Technology enablers and innovation success
   - Economic expansion and capital availability
   
   **BASE SCENARIO: "Steady Progress"**
   - Moderate market growth and stable demand
   - Competitive equilibrium maintenance
   - Regulatory stability with gradual evolution
   - Incremental technology advancement
   - Economic stability with normal volatility
   
   **PESSIMISTIC SCENARIO: "Market Challenges"**
   - Market contraction and demand uncertainty
   - Competitive pressure and margin compression
   - Regulatory headwinds and compliance costs
   - Technology disruption and obsolescence risks
   - Economic recession and capital constraints
   
   **STRESS SCENARIO: "Crisis Response"**
   - Severe market disruption and demand collapse
   - Aggressive competitive attacks and market share loss
   - Regulatory crisis and punitive measures
   - Major technology failure or cyber incident
   - Financial crisis and liquidity constraints

3. **IMPACT ANALYSIS BY SCENARIO**
   - Financial performance implications (revenue, profitability, cash flow)
   - Market position and competitive standing changes
   - Operational requirements and capability needs
   - Investment priorities and resource allocation shifts
   - Risk profile and mitigation requirements

4. **STRATEGIC OPTION EVALUATION**
   - Core strategy robustness across scenarios
   - Strategic flexibility and optionality value
   - Contingent strategies and trigger mechanisms
   - Investment staging and real options analysis
   - Portfolio diversification and hedging strategies

5. **DECISION FRAMEWORK AND RECOMMENDATIONS**
   - Robust strategic initiatives (work in all scenarios)
   - Contingent strategies with decision triggers
   - Hedging and risk management approaches
   - Monitoring systems and early warning indicators
   - Adaptive capacity and organizational agility requirements

**IMPLEMENTATION ROADMAP:**
- Immediate strategic decisions and commitments
- Scenario monitoring and trigger development
- Organizational preparedness and capability building
- Stakeholder communication and alignment
- Periodic scenario review and updating process

{industry_context}
{role_focus}
{regulatory_considerations}

Provide actionable strategic guidance that enhances decision quality under uncertainty.

{communication_guidance}
""",
            variables={
                "time_horizon": "3-5 years",
                "scenario_types": "economic and competitive"
            },
            context_adaptations={
                "financial_services": "Include regulatory capital scenarios, interest rate environments, and credit cycle impacts. Consider fintech disruption and digital banking evolution.",
                "technology": "Focus on technology disruption scenarios, platform evolution, and innovation cycles. Include cybersecurity and data privacy regulatory scenarios.",
                "healthcare": "Consider regulatory approval scenarios, healthcare reform impacts, and value-based care evolution. Include pandemic and public health scenarios.",
                "ceo": "Frame for board strategic planning with focus on long-term value creation and strategic positioning across scenarios.",
                "cfo": "Emphasize financial planning implications, capital allocation across scenarios, and risk management strategies."
            },
            quality_criteria=[
                "Comprehensive scenario architecture with clear differentiation",
                "Quantitative impact analysis with financial modeling",
                "Strategic option evaluation with decision criteria",
                "Robust strategy recommendations across scenarios",
                "Implementation roadmap with monitoring triggers"
            ],
            tags=["scenario_planning", "strategic_planning", "risk_management", "decision_framework"]
        )
        
        # Crisis Scenario Planning
        self.templates['crisis_scenario_planning'] = PromptTemplate(
            name="Crisis and Black Swan Scenario Planning",
            category=PromptCategory.STRATEGIC_ANALYSIS,
            base_prompt="""
Develop crisis scenario planning and black swan event preparedness for potential severe disruptions to our {industry} business operations and strategic objectives.

**CRISIS SCENARIO FRAMEWORK:**

1. **CRISIS TYPOLOGY AND PROBABILITY ASSESSMENT**
   - External crises: economic collapse, pandemic, geopolitical conflict
   - Industry crises: regulatory crackdown, technology obsolescence, market disruption
   - Company-specific crises: cyber attack, operational failure, reputation damage
   - Systemic crises: financial system collapse, supply chain breakdown
   - Black swan events: unprecedented and high-impact scenarios

2. **SEVERE IMPACT SCENARIOS**
   
   **ECONOMIC CRISIS SCENARIO:**
   - Severe recession with 30%+ demand decline
   - Credit markets freeze and liquidity constraints
   - Mass unemployment and consumer behavior shifts
   - Government intervention and policy responses
   - Industry consolidation and competitive shakeout
   
   **OPERATIONAL CRISIS SCENARIO:**
   - Major system failure or cybersecurity breach
   - Supply chain disruption and vendor failures
   - Key talent exodus and capability loss
   - Regulatory investigation or enforcement action
   - Product recall or safety incident
   
   **COMPETITIVE CRISIS SCENARIO:**
   - Market disruption by new technology or business model
   - Major competitor acquisition or consolidation
   - Price war and margin compression
   - Customer concentration and dependency risks
   - Intellectual property or legal challenges

3. **CRISIS IMPACT ASSESSMENT**
   - Financial impact: revenue loss, cost increase, cash burn
   - Operational impact: business continuity, service delivery
   - Reputational impact: stakeholder trust, brand value
   - Strategic impact: competitive position, market access
   - Organizational impact: talent retention, culture, morale

4. **CRISIS RESPONSE STRATEGIES**
   - Immediate survival and business continuity
   - Financial preservation and liquidity management
   - Stakeholder communication and relationship management
   - Operational restructuring and cost management
   - Strategic repositioning and recovery planning

5. **CRISIS PREPAREDNESS AND RESILIENCE**
   - Early warning systems and trigger mechanisms
   - Crisis management team and governance
   - Emergency communication protocols
   - Financial reserves and contingency funding
   - Scenario-based stress testing and exercises

**CRISIS MANAGEMENT RECOMMENDATIONS:**
- Crisis response playbook development
- Organizational resilience building
- Stakeholder relationship strengthening
- Financial flexibility and optionality
- Strategic diversification and hedging

{industry_context}
{urgency_level}: Focus on actionable crisis preparedness measures.
{regulatory_considerations}

Emphasize business continuity and stakeholder protection in crisis scenarios.
""",
            variables={
                "industry": ""
            },
            quality_criteria=[
                "Comprehensive crisis scenario identification",
                "Detailed impact assessment with quantification",
                "Actionable crisis response strategies",
                "Crisis preparedness and resilience measures",
                "Practical implementation guidance"
            ],
            tags=["crisis_planning", "business_continuity", "risk_management", "black_swan_scenarios"]
        )
        
        # Strategic Option Valuation
        self.templates['strategic_option_valuation'] = PromptTemplate(
            name="Strategic Option Valuation Under Uncertainty",
            category=PromptCategory.STRATEGIC_ANALYSIS,
            base_prompt="""
Evaluate strategic options and investment decisions using scenario-based analysis and real options valuation methodology for our {strategic_focus} initiatives.

**STRATEGIC OPTION VALUATION FRAMEWORK:**

1. **STRATEGIC OPTION IDENTIFICATION**
   - Core strategic initiatives (must-do investments)
   - Growth options (expansion and new market opportunities)
   - Flexibility options (ability to adapt and change course)
   - Abandonment options (ability to exit or reduce commitment)
   - Staging options (ability to invest in phases)

2. **SCENARIO-BASED VALUATION**
   - Net present value (NPV) calculation by scenario
   - Probability-weighted expected value analysis
   - Risk-adjusted discount rates by scenario
   - Sensitivity analysis on key assumptions
   - Monte Carlo simulation for uncertainty modeling

3. **REAL OPTIONS ANALYSIS**
   - Option to expand: value of scaling successful initiatives
   - Option to abandon: value of limiting downside losses
   - Option to delay: value of waiting for better information
   - Option to stage: value of phased investment approach
   - Option to switch: value of operational flexibility

4. **PORTFOLIO OPTIMIZATION**
   - Strategic option portfolio construction
   - Correlation and diversification benefits
   - Resource allocation and capital constraints
   - Risk-return optimization across scenarios
   - Strategic synergies and option interactions

5. **DECISION CRITERIA AND THRESHOLDS**
   - Investment hurdle rates by risk category
   - Decision triggers and go/no-go criteria
   - Option exercise conditions and timing
   - Portfolio rebalancing triggers
   - Performance monitoring and adjustment mechanisms

**STRATEGIC RECOMMENDATIONS:**
- Optimal strategic option portfolio
- Investment timing and staging recommendations
- Risk management and hedging strategies
- Monitoring and decision trigger systems
- Organizational capabilities for option management

{industry_context}
{role_focus}
{strategic_focus} specific considerations and valuation approaches.

Provide quantitative analysis with clear decision frameworks for strategic option evaluation.
""",
            variables={
                "strategic_focus": "business_strategy"
            },
            quality_criteria=[
                "Comprehensive strategic option identification",
                "Quantitative valuation with scenario analysis",
                "Real options methodology application",
                "Portfolio optimization framework",
                "Clear decision criteria and triggers"
            ],
            tags=["option_valuation", "strategic_options", "investment_analysis", "portfolio_optimization"]
        )
        
        # Register templates
        for template in self.templates.values():
            prompt_manager.register_template(template)
    
    def generate_scenario_planning_prompt(self, config: ScenarioConfig,
                                        context: Dict[str, Any]) -> str:
        """Generate comprehensive scenario planning prompt."""
        template = self.templates['comprehensive_scenario_planning']
        
        scenario_types_text = " and ".join([s.value for s in config.scenario_types])
        
        variables = {
            'time_horizon': config.time_horizon,
            'scenario_types': scenario_types_text
        }
        
        prompt = template.base_prompt
        for key, value in variables.items():
            prompt = prompt.replace(f"{{{key}}}", str(value))
        
        adapted_prompt = context_adapter.adapt_prompt(prompt, context.get('prompt_context'))
        
        return adapted_prompt
    
    def generate_crisis_planning_prompt(self, industry: str,
                                      context: Dict[str, Any]) -> str:
        """Generate crisis scenario planning prompt."""
        template = self.templates['crisis_scenario_planning']
        
        variables = {
            'industry': industry
        }
        
        prompt = template.base_prompt
        for key, value in variables.items():
            prompt = prompt.replace(f"{{{key}}}", str(value))
        
        adapted_prompt = context_adapter.adapt_prompt(prompt, context.get('prompt_context'))
        
        return adapted_prompt
    
    def generate_option_valuation_prompt(self, strategic_focus: str,
                                       context: Dict[str, Any]) -> str:
        """Generate strategic option valuation prompt."""
        template = self.templates['strategic_option_valuation']
        
        variables = {
            'strategic_focus': strategic_focus
        }
        
        prompt = template.base_prompt
        for key, value in variables.items():
            prompt = prompt.replace(f"{{{key}}}", str(value))
        
        adapted_prompt = context_adapter.adapt_prompt(prompt, context.get('prompt_context'))
        
        return adapted_prompt
    
    def get_scenario_dimensions_framework(self) -> Dict[str, List[str]]:
        """Generate scenario dimension framework for 2x2 matrices."""
        return {
            'economic_dimensions': [
                'Economic growth (high/low)',
                'Interest rates (rising/falling)',
                'Inflation (high/low)',
                'Consumer confidence (strong/weak)',
                'Government spending (expansionary/contractionary)'
            ],
            'competitive_dimensions': [
                'Market competition (intense/stable)',
                'Industry consolidation (high/low)',
                'New entrants (many/few)',
                'Competitive advantage (sustainable/eroding)',
                'Price competition (aggressive/disciplined)'
            ],
            'technology_dimensions': [
                'Innovation pace (rapid/gradual)',
                'Disruption level (revolutionary/evolutionary)',
                'Technology adoption (fast/slow)',
                'Platform effects (strong/weak)',
                'Digital transformation (accelerated/steady)'
            ],
            'regulatory_dimensions': [
                'Regulatory environment (restrictive/permissive)',
                'Policy stability (stable/volatile)',
                'Compliance costs (high/low)',
                'Market intervention (high/low)',
                'International coordination (strong/weak)'
            ]
        }
    
    def generate_scenario_indicators(self) -> Dict[str, List[str]]:
        """Generate early warning indicators for scenario monitoring."""
        return {
            'economic_indicators': [
                'GDP growth rate trends',
                'Employment and unemployment rates',
                'Consumer confidence indices',
                'Business investment levels',
                'Credit availability and conditions',
                'Currency exchange rates',
                'Commodity price movements'
            ],
            'competitive_indicators': [
                'Market share shifts',
                'New product launch frequency',
                'Pricing pressure trends',
                'M&A activity levels',
                'Competitor financial performance',
                'Customer switching behavior',
                'Innovation investment levels'
            ],
            'regulatory_indicators': [
                'Regulatory proposal pipeline',
                'Enforcement action trends',
                'Policy maker statements',
                'Industry consultation activity',
                'Compliance cost evolution',
                'International regulatory coordination',
                'Public opinion and media coverage'
            ],
            'technology_indicators': [
                'R&D investment trends',
                'Patent filing activity',
                'Technology adoption rates',
                'Startup funding in relevant areas',
                'Academic research developments',
                'Standards development activity',
                'Cybersecurity incident frequency'
            ]
        }
    
    def generate_decision_trees(self, scenarios: List[str], decisions: List[str]) -> Dict[str, Any]:
        """Generate decision tree framework for scenario planning."""
        decision_tree = {
            'root_decision': 'Strategic Direction Choice',
            'scenarios': scenarios,
            'decision_options': decisions,
            'evaluation_criteria': [
                'Expected value across scenarios',
                'Downside risk and protection',
                'Upside potential and optionality',
                'Resource requirements and constraints',
                'Strategic fit and capability leverage',
                'Flexibility and reversibility',
                'Stakeholder alignment and support'
            ],
            'decision_framework': {
                'phase_1': 'Scenario probability assessment',
                'phase_2': 'Option payoff calculation by scenario',
                'phase_3': 'Risk-adjusted expected value analysis',
                'phase_4': 'Sensitivity and robustness testing',
                'phase_5': 'Strategic recommendation synthesis'
            }
        }
        return decision_tree
    
    def generate_stress_testing_framework(self) -> Dict[str, Any]:
        """Generate stress testing framework for scenario analysis."""
        return {
            'stress_test_categories': {
                'financial_stress': [
                    'Revenue decline of 30-50%',
                    'Cost increase of 20-40%',
                    'Cash flow interruption',
                    'Credit availability restriction',
                    'Currency devaluation impact'
                ],
                'operational_stress': [
                    'Key supplier failure',
                    'Critical system downtime',
                    'Major talent exodus',
                    'Supply chain disruption',
                    'Quality or safety incident'
                ],
                'market_stress': [
                    'Competitive market disruption',
                    'Customer concentration risk',
                    'Regulatory enforcement action',
                    'Reputation damage event',
                    'Technology obsolescence'
                ]
            },
            'stress_test_methodology': [
                'Baseline scenario establishment',
                'Stress factor identification and calibration',
                'Impact pathway mapping',
                'Quantitative stress impact modeling',
                'Business continuity assessment',
                'Recovery scenario development',
                'Risk mitigation evaluation'
            ],
            'resilience_measures': [
                'Financial buffer requirements',
                'Operational redundancy needs',
                'Strategic flexibility options',
                'Crisis response capabilities',
                'Stakeholder relationship strength'
            ]
        }


# Global scenario planning generator instance
scenario_planning_generator = ScenarioPlanningGenerator()