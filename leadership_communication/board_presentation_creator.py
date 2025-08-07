"""
Executive AI Prompts - Board Presentation Creator

Professional board presentation development with strategic narrative,
executive summary generation, and stakeholder communication frameworks.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from enum import Enum
from prompt_manager import PromptTemplate, PromptCategory, prompt_manager
from context_adapter import context_adapter


class PresentationType(Enum):
    QUARTERLY_REVIEW = "quarterly_business_review"
    STRATEGIC_PLANNING = "strategic_planning_session"
    INVESTMENT_APPROVAL = "investment_approval"
    CRISIS_UPDATE = "crisis_management_update"
    TRANSFORMATION = "transformation_progress"
    M_AND_A = "merger_acquisition"
    GOVERNANCE = "governance_compliance"


class AudienceLevel(Enum):
    BOARD_DIRECTORS = "board_of_directors"
    EXECUTIVE_COMMITTEE = "executive_committee"
    AUDIT_COMMITTEE = "audit_committee"
    INVESTMENT_COMMITTEE = "investment_committee"
    SHAREHOLDERS = "shareholder_meeting"


@dataclass
class PresentationConfig:
    """Configuration for board presentation development."""
    presentation_type: PresentationType = PresentationType.QUARTERLY_REVIEW
    audience: AudienceLevel = AudienceLevel.BOARD_DIRECTORS
    time_allocation: str = "60 minutes"
    key_decisions_required: List[str] = field(default_factory=list)
    supporting_materials: bool = True
    executive_summary: bool = True
    q_and_a_preparation: bool = True


class BoardPresentationCreator:
    """Advanced board presentation and executive communication generator."""
    
    def __init__(self):
        self.templates = {}
        self._initialize_templates()
    
    def _initialize_templates(self) -> None:
        """Initialize board presentation templates."""
        
        # Quarterly Board Presentation
        self.templates['quarterly_board_presentation'] = PromptTemplate(
            name="Quarterly Board Presentation Framework",
            category=PromptCategory.LEADERSHIP_COMMUNICATION,
            base_prompt="""
Develop comprehensive quarterly board presentation for the {audience} focusing on strategic performance, financial results, and forward-looking initiatives for {time_allocation} presentation.

**BOARD PRESENTATION STRUCTURE:**

**SLIDE 1-2: EXECUTIVE SUMMARY & KEY MESSAGES**
- Quarter performance highlights and lowlights
- Key financial metrics and strategic progress
- Critical decisions required from the board
- Forward-looking priorities and initiatives
- Risk and opportunity landscape overview

**SLIDE 3-5: FINANCIAL PERFORMANCE REVIEW**
- Revenue and profitability vs. plan and prior year
- Key performance indicator dashboard
- Cash flow and balance sheet highlights
- Industry benchmarking and competitive position
- Full-year guidance and outlook commentary

**SLIDE 6-8: STRATEGIC INITIATIVE PROGRESS**
- Strategic plan execution status and milestones
- Investment progress and ROI performance
- Market position and competitive developments
- Digital transformation and innovation updates
- ESG and sustainability progress metrics

**SLIDE 9-11: OPERATIONAL EXCELLENCE UPDATE**
- Customer satisfaction and market feedback
- Operational efficiency and productivity gains
- Quality metrics and service delivery performance
- Talent development and organizational health
- Technology infrastructure and capability building

**SLIDE 12-14: MARKET DYNAMICS & COMPETITIVE LANDSCAPE**
- Industry trends and market evolution analysis
- Competitive positioning and threat assessment
- Regulatory and policy environment updates
- Economic environment and macroeconomic impacts
- Emerging opportunities and disruption risks

**SLIDE 15-17: RISK MANAGEMENT & GOVERNANCE**
- Enterprise risk assessment and mitigation
- Regulatory compliance and audit updates
- Cybersecurity posture and incident management
- Internal controls and governance effectiveness
- Crisis preparedness and business continuity

**SLIDE 18-20: FORWARD-LOOKING STRATEGY & INVESTMENTS**
- Strategic priorities for next quarter and year
- Investment proposals and capital allocation
- Growth initiatives and market expansion plans
- Organizational development and capability building
- Partnership and acquisition opportunities

**SLIDE 21-22: DECISION ITEMS & BOARD ACTIONS**
- Specific decisions and approvals required
- Board committee referrals and recommendations
- Policy updates and governance changes
- Executive compensation and succession planning
- Stakeholder engagement and communication strategy

**APPENDIX MATERIALS:**
- Detailed financial statements and analysis
- Market research and competitive intelligence
- Risk register and mitigation plans
- Organizational charts and succession plans
- Supporting documentation and references

**EXECUTIVE SUMMARY (2-PAGE DOCUMENT):**
- Quarter performance summary with key metrics
- Strategic progress and milestone achievement
- Critical issues and board decision requirements
- Risk assessment and mitigation status
- Forward-looking priorities and resource needs

{industry_context}
{role_focus}
{regulatory_considerations}

Focus on strategic-level insights that enable effective board governance and oversight.

{communication_guidance}
""",
            variables={
                "audience": "board of directors",
                "time_allocation": "60 minutes"
            },
            context_adaptations={
                "financial_services": "Include regulatory capital updates, stress testing results, and regulatory examination findings. Address Basel III compliance and supervisory feedback.",
                "technology": "Focus on product development progress, platform scalability, cybersecurity posture, and digital transformation metrics. Include innovation pipeline updates.",
                "healthcare": "Include clinical outcomes, patient safety metrics, regulatory compliance status, and value-based care performance. Address quality measures and accreditation updates.",
                "ceo": "Frame as CEO report to board with strategic leadership perspective and shareholder value focus.",
                "cfo": "Emphasize financial stewardship, capital allocation, and investor relations perspective with detailed financial analysis."
            },
            quality_criteria=[
                "Strategic-level content appropriate for board governance",
                "Clear decision items and board action requirements",
                "Comprehensive risk assessment and mitigation updates",
                "Forward-looking strategic guidance and planning",
                "Professional presentation structure with executive summary"
            ],
            tags=["board_presentation", "quarterly_review", "executive_communication", "governance"]
        )
        
        # Strategic Planning Presentation
        self.templates['strategic_planning_presentation'] = PromptTemplate(
            name="Strategic Planning Board Session Framework",
            category=PromptCategory.LEADERSHIP_COMMUNICATION,
            base_prompt="""
Create comprehensive strategic planning presentation for board strategic session focusing on {strategic_focus} with long-term value creation and competitive positioning.

**STRATEGIC PLANNING PRESENTATION STRUCTURE:**

**SECTION I: STRATEGIC CONTEXT & MARKET ANALYSIS (15 minutes)**

**Market Environment Assessment:**
- Industry evolution and disruption trends analysis
- Competitive landscape changes and new entrant threats
- Customer behavior shifts and demand pattern evolution
- Technology disruption and innovation impact assessment
- Regulatory environment changes and policy implications

**Competitive Position Review:**
- Current market position and share analysis
- Competitive advantages and strategic moats evaluation
- Performance benchmarking vs. industry leaders
- Brand strength and customer loyalty assessment
- Capability gaps and development requirements

**SECTION II: STRATEGIC OPTION EVALUATION (20 minutes)**

**Growth Strategy Options:**
- Organic growth opportunities and market expansion
- Inorganic growth through acquisitions and partnerships
- New product/service development and innovation
- Geographic expansion and market entry strategies
- Adjacent market opportunities and diversification

**Competitive Strategy Analysis:**
- Market leadership and differentiation strategies
- Cost leadership and operational excellence approaches
- Niche specialization and focus strategies
- Platform and ecosystem development opportunities
- Innovation and digital transformation priorities

**SECTION III: STRATEGIC PLAN DEVELOPMENT (15 minutes)**

**3-5 Year Strategic Vision:**
- Long-term vision and mission alignment
- Strategic objectives and success metrics
- Market position aspiration and competitive goals
- Financial performance targets and value creation
- Organizational capability and culture development

**Strategic Initiative Portfolio:**
- Core business strengthening and optimization
- Growth platform development and expansion
- Transformation and innovation investments
- Partnership and ecosystem development
- Risk management and resilience building

**SECTION IV: RESOURCE ALLOCATION & INVESTMENT (10 minutes)**

**Capital Allocation Strategy:**
- Investment prioritization and resource allocation
- Financial resources and funding requirements
- Human capital development and talent strategy
- Technology infrastructure and digital investments
- Risk management and contingency planning

**Implementation Roadmap:**
- Strategic initiative sequencing and timeline
- Organizational change management and execution
- Performance monitoring and adjustment mechanisms
- Stakeholder engagement and communication strategy
- Success metrics and milestone tracking

**BOARD DISCUSSION & DECISION FRAMEWORK:**
- Strategic direction approval and endorsement
- Investment authorization and resource allocation
- Risk appetite and tolerance setting
- Performance expectations and accountability
- Oversight and governance framework establishment

{industry_context}
{strategic_focus} specific strategic considerations and industry best practices.
{role_focus}

Facilitate strategic thinking and long-term value creation decision-making.
""",
            variables={
                "strategic_focus": "long-term competitive positioning"
            },
            quality_criteria=[
                "Comprehensive strategic analysis with market context",
                "Clear strategic options with trade-off analysis",
                "Long-term vision with measurable objectives",
                "Resource allocation framework with prioritization",
                "Implementation roadmap with governance structure"
            ],
            tags=["strategic_planning", "long_term_strategy", "competitive_positioning", "value_creation"]
        )
        
        # Crisis Communication Presentation
        self.templates['crisis_communication_presentation'] = PromptTemplate(
            name="Crisis Management Board Communication",
            category=PromptCategory.LEADERSHIP_COMMUNICATION,
            base_prompt="""
Develop urgent crisis management presentation for emergency board session addressing {crisis_situation} with immediate response strategy and stakeholder communication plan.

**CRISIS COMMUNICATION PRESENTATION:**

**SLIDE 1: CRISIS SITUATION OVERVIEW (IMMEDIATE IMPACT)**
- Crisis nature, scope, and severity assessment
- Timeline of events and current status
- Immediate financial and operational impacts
- Stakeholder groups affected and concerns
- Media coverage and public relations implications

**SLIDE 2-3: SITUATION ASSESSMENT & ROOT CAUSE**
- Detailed incident analysis and contributing factors
- Internal and external factors and dependencies
- System failures and process breakdowns
- Human factors and decision-making analysis
- Regulatory and compliance implications

**SLIDE 4-5: IMMEDIATE RESPONSE ACTIONS TAKEN**
- Crisis response team activation and leadership
- Emergency containment and stabilization measures
- Customer protection and service continuity
- Employee safety and security measures
- Regulatory notification and compliance actions

**SLIDE 6-7: STAKEHOLDER IMPACT ASSESSMENT**

**Customer Impact:**
- Service disruption and customer affected count
- Customer communication and support measures
- Compensation and remediation programs
- Customer retention and loyalty implications
- Service restoration timeline and progress

**Financial Impact:**
- Direct costs and expense increases
- Revenue loss and business interruption
- Insurance coverage and claim processing
- Cash flow implications and liquidity needs
- Credit rating and financing implications

**Regulatory Impact:**
- Regulatory investigation and enforcement risk
- Compliance violation and penalty exposure
- Supervisory action and consent order risk
- Industry reputation and regulatory relationship
- Long-term regulatory oversight implications

**SLIDE 8-9: CRISIS RESPONSE STRATEGY**

**Short-term Stabilization (0-30 days):**
- Business continuity and service restoration
- Customer communication and support enhancement
- Regulatory compliance and cooperation
- Media relations and reputation management
- Employee support and organizational stability

**Medium-term Recovery (30-90 days):**
- Operational recovery and service normalization
- Customer confidence rebuilding and retention
- Financial recovery and performance restoration
- Organizational learning and improvement integration
- Stakeholder relationship repair and strengthening

**SLIDE 10-11: GOVERNANCE & OVERSIGHT ENHANCEMENTS**
- Crisis management governance improvements
- Risk management framework enhancements
- Internal controls and monitoring upgrades
- Board oversight and reporting mechanisms
- Independent review and validation processes

**SLIDE 12: BOARD DECISIONS & APPROVALS REQUIRED**
- Crisis response strategy authorization
- Financial commitments and resource allocation
- External communication and disclosure approval
- Legal strategy and litigation management
- Executive authority and decision-making delegation

**EXECUTIVE BRIEFING MATERIALS:**
- Detailed incident timeline and chronology
- Financial impact analysis and projections
- Legal and regulatory assessment summary
- Stakeholder communication materials
- Media monitoring and coverage analysis

{industry_context}
{crisis_situation} specific response protocols and regulatory requirements.
{urgency_level}: Immediate board action and decision-making required.

Provide clear, actionable crisis response framework with board governance and oversight.
""",
            variables={
                "crisis_situation": "operational disruption",
                "urgency_level": "critical"
            },
            quality_criteria=[
                "Clear crisis assessment with immediate impact quantification",
                "Comprehensive response strategy with timeline and milestones",
                "Stakeholder impact analysis with mitigation plans",
                "Governance and oversight framework enhancements",
                "Urgent decision items with board authority requirements"
            ],
            tags=["crisis_management", "emergency_communication", "stakeholder_management", "governance"]
        )
        
        # Register templates
        for template in self.templates.values():
            prompt_manager.register_template(template)
    
    def generate_quarterly_presentation_prompt(self, config: PresentationConfig,
                                             context: Dict[str, Any]) -> str:
        """Generate quarterly board presentation prompt."""
        template = self.templates['quarterly_board_presentation']
        
        variables = {
            'audience': config.audience.value.replace('_', ' '),
            'time_allocation': config.time_allocation
        }
        
        prompt = template.base_prompt
        for key, value in variables.items():
            prompt = prompt.replace(f"{{{key}}}", str(value))
        
        adapted_prompt = context_adapter.adapt_prompt(prompt, context.get('prompt_context'))
        
        return adapted_prompt
    
    def generate_strategic_planning_prompt(self, strategic_focus: str,
                                         context: Dict[str, Any]) -> str:
        """Generate strategic planning presentation prompt."""
        template = self.templates['strategic_planning_presentation']
        
        variables = {
            'strategic_focus': strategic_focus
        }
        
        prompt = template.base_prompt
        for key, value in variables.items():
            prompt = prompt.replace(f"{{{key}}}", str(value))
        
        adapted_prompt = context_adapter.adapt_prompt(prompt, context.get('prompt_context'))
        
        return adapted_prompt
    
    def generate_crisis_communication_prompt(self, crisis_situation: str,
                                           context: Dict[str, Any]) -> str:
        """Generate crisis communication presentation prompt."""
        template = self.templates['crisis_communication_presentation']
        
        variables = {
            'crisis_situation': crisis_situation
        }
        
        prompt = template.base_prompt
        for key, value in variables.items():
            prompt = prompt.replace(f"{{{key}}}", str(value))
        
        adapted_prompt = context_adapter.adapt_prompt(prompt, context.get('prompt_context'))
        
        return adapted_prompt
    
    def get_presentation_best_practices(self) -> Dict[str, List[str]]:
        """Generate board presentation best practices framework."""
        return {
            'content_structure': [
                'Start with executive summary and key messages',
                'Use strategic framework and logical flow',
                'Include forward-looking perspective and guidance',
                'Highlight risks, opportunities, and decision items',
                'Provide supporting data and analysis in appendix'
            ],
            'slide_design': [
                'Professional, clean design with consistent branding',
                'Maximum 6-8 bullet points per slide',
                'Use charts and graphics for complex data',
                'Include slide numbers and confidentiality markings',
                'Ensure readability for remote participants'
            ],
            'communication_style': [
                'Executive-level language and terminology',
                'Focus on strategic implications and decisions',
                'Quantify impacts and provide specific metrics',
                'Address governance and oversight requirements',
                'Prepare for questions and follow-up discussions'
            ],
            'meeting_management': [
                'Distribute materials 48-72 hours in advance',
                'Start with safety moment or key announcement',
                'Manage time allocation and discussion flow',
                'Document decisions and action items clearly',
                'Schedule follow-up sessions for complex topics'
            ],
            'stakeholder_engagement': [
                'Tailor content to board member expertise',
                'Address individual director concerns and interests',
                'Provide context for industry outsiders',
                'Encourage questions and interactive discussion',
                'Follow up with additional information as requested'
            ]
        }
    
    def generate_executive_summary_template(self) -> Dict[str, str]:
        """Generate executive summary template structure."""
        return {
            'header': "EXECUTIVE SUMMARY - [PRESENTATION TITLE] - [DATE]",
            'section_1_performance': """
PERFORMANCE HIGHLIGHTS:
• Financial Performance: [Key metrics vs. plan and prior year]
• Strategic Progress: [Major milestone achievements and progress]
• Operational Excellence: [Key improvements and efficiency gains]
• Risk Management: [Critical risk mitigation and compliance updates]
            """,
            'section_2_decisions': """
BOARD DECISIONS REQUIRED:
• [Decision Item 1]: [Brief description and recommendation]
• [Decision Item 2]: [Brief description and recommendation]
• [Decision Item 3]: [Brief description and recommendation]
            """,
            'section_3_outlook': """
FORWARD-LOOKING PRIORITIES:
• Strategic Initiatives: [Key priorities and resource requirements]
• Investment Proposals: [Major investments and capital allocation]
• Risk Mitigation: [Critical risk management priorities]
• Stakeholder Engagement: [Key communications and relationships]
            """,
            'footer': """
APPENDIX MATERIALS:
• Detailed financial statements and variance analysis
• Market research and competitive intelligence updates
• Risk register and mitigation plan updates
• Organizational development and succession planning
• Supporting documentation and regulatory communications
            """
        }
    
    def generate_q_and_a_preparation(self) -> Dict[str, List[str]]:
        """Generate Q&A preparation framework for board presentations."""
        return {
            'financial_performance': [
                'What drove the variance from budget/plan this quarter?',
                'How do our margins compare to industry peers?',
                'What are the key assumptions in our full-year guidance?',
                'How has working capital management improved?',
                'What is our current liquidity and debt capacity?'
            ],
            'strategic_execution': [
                'Are we on track to achieve our strategic objectives?',
                'What are the biggest risks to our strategic plan?',
                'How are we measuring success of key initiatives?',
                'What competitive threats are you most concerned about?',
                'How is our digital transformation progressing?'
            ],
            'risk_management': [
                'What are our top enterprise risks currently?',
                'How has our risk profile changed this quarter?',
                'Are we adequately prepared for cyber threats?',
                'What regulatory changes are on the horizon?',
                'How do we stress test our business model?'
            ],
            'governance_oversight': [
                'How is management succession planning progressing?',
                'What ESG initiatives are we prioritizing?',
                'Are our internal controls operating effectively?',
                'How do we benchmark our governance practices?',
                'What stakeholder feedback are we receiving?'
            ],
            'investment_decisions': [
                'What is the ROI and payback on proposed investments?',
                'How do these investments align with strategy?',
                'What are the implementation risks and mitigation?',
                'How will we measure success and performance?',
                'What alternatives were considered and why rejected?'
            ]
        }


# Global board presentation creator instance
board_presentation_creator = BoardPresentationCreator()