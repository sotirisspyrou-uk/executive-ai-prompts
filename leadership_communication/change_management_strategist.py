"""
Executive AI Prompts - Change Management Strategist

Comprehensive organizational change communication, employee engagement,
and transformation strategy frameworks for executive leadership.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from enum import Enum
from prompt_manager import PromptTemplate, PromptCategory, prompt_manager
from context_adapter import context_adapter


class ChangeType(Enum):
    STRATEGIC_TRANSFORMATION = "strategic_transformation"
    DIGITAL_TRANSFORMATION = "digital_transformation"
    ORGANIZATIONAL_RESTRUCTURE = "organizational_restructure"
    MERGER_ACQUISITION = "merger_acquisition"
    CULTURAL_CHANGE = "cultural_change"
    OPERATIONAL_IMPROVEMENT = "operational_improvement"
    TECHNOLOGY_IMPLEMENTATION = "technology_implementation"
    PROCESS_REENGINEERING = "process_reengineering"


class ChangeScope(Enum):
    ENTERPRISE_WIDE = "enterprise_wide"
    DIVISION_LEVEL = "division_level"
    DEPARTMENT_LEVEL = "department_level"
    TEAM_LEVEL = "team_level"


class ChangeUrgency(Enum):
    GRADUAL = "gradual_evolution"
    MODERATE = "moderate_pace"
    ACCELERATED = "accelerated_timeline"
    EMERGENCY = "crisis_driven"


@dataclass
class ChangeConfig:
    """Configuration for change management strategy."""
    change_type: ChangeType = ChangeType.STRATEGIC_TRANSFORMATION
    change_scope: ChangeScope = ChangeScope.ENTERPRISE_WIDE
    urgency: ChangeUrgency = ChangeUrgency.MODERATE
    timeline: str = "12-18 months"
    affected_employees: str = "all employees"
    resistance_level: str = "moderate"  # "low", "moderate", "high"
    leadership_alignment: str = "strong"  # "weak", "moderate", "strong"


class ChangeManagementStrategist:
    """Advanced change management and transformation communication generator."""
    
    def __init__(self):
        self.templates = {}
        self._initialize_templates()
    
    def _initialize_templates(self) -> None:
        """Initialize change management strategy templates."""
        
        # Comprehensive Change Management Strategy
        self.templates['comprehensive_change_strategy'] = PromptTemplate(
            name="Comprehensive Change Management and Communication Strategy",
            category=PromptCategory.LEADERSHIP_COMMUNICATION,
            base_prompt="""
As Chief Change Officer leading a {change_type} initiative with {change_scope} impact over {timeline}, develop comprehensive change management strategy addressing employee engagement, communication, and organizational transformation.

**CHANGE MANAGEMENT STRATEGY FRAMEWORK:**

**CHANGE VISION AND STRATEGIC CONTEXT:**

**Change Vision Statement:**
- Clear, compelling vision for the future state
- Benefits and value creation for stakeholders
- Alignment with organizational mission and values
- Connection to market dynamics and competitive necessity
- Personal relevance and meaning for employees

**Strategic Rationale and Business Case:**
- Market drivers and competitive imperatives
- Financial benefits and value creation potential
- Risk mitigation and future-proofing objectives
- Stakeholder value enhancement opportunities
- Organizational capability and resilience building

**Change Impact Assessment:**
- Organizational structure and role changes
- Process and workflow modifications
- Technology and system transformations
- Culture and behavior evolution requirements
- Skills and competency development needs

**STAKEHOLDER ANALYSIS AND ENGAGEMENT:**

**Change Stakeholder Mapping:**
- Executive sponsors and change champions
- Middle management and team leaders
- Frontline employees and individual contributors
- Customers and external stakeholders
- Union representatives and employee groups

**Resistance and Support Analysis:**
- Change advocates and early adopters
- Neutral employees and fence-sitters
- Skeptics and change resistors
- Influencer identification and engagement
- Coalition building and momentum creation

**CHANGE COMMUNICATION STRATEGY:**

**Communication Vision and Principles:**
- Transparent, honest, and timely communication
- Two-way dialogue and feedback integration
- Consistent messaging across all channels
- Leadership visibility and accessibility
- Celebration of progress and achievements

**Multi-Channel Communication Approach:**

**Leadership Communication:**
- CEO vision speeches and town halls
- Executive team alignment and messaging
- Leadership storytelling and personal commitment
- Management cascade and supervisor briefings
- Board and investor communication coordination

**Employee Engagement Platforms:**
- All-hands meetings and department briefings
- Change champion networks and ambassadors
- Employee feedback sessions and surveys
- Digital collaboration platforms and forums
- Recognition and celebration events

**Change Communication Timeline:**

**Phase 1: Vision and Awareness (Months 1-3):**
- Change vision launch and executive communication
- "Why change" education and business case sharing
- Initial stakeholder engagement and feedback
- Change champion identification and training
- Communication channel establishment and testing

**Phase 2: Understanding and Buy-in (Months 4-6):**
- Detailed change impact communication
- Skills development and training program launch
- Success story sharing and progress celebration
- Resistance addressing and concern resolution
- Middle management enablement and support

**Phase 3: Implementation and Adoption (Months 7-12):**
- Change implementation communication and support
- Real-time feedback and course correction
- Performance measurement and progress tracking
- Continuous improvement and optimization
- Sustainable behavior reinforcement

**Phase 4: Integration and Sustainment (Months 13-18):**
- New state integration and normalization
- Culture evolution and value reinforcement
- Lessons learned and best practice sharing
- Change capability institutionalization
- Future change readiness preparation

**EMPLOYEE ENGAGEMENT AND SUPPORT:**

**Change Support Infrastructure:**
- Change management office and resources
- Training and development program enhancement
- Coaching and mentoring support systems
- Employee assistance and wellness programs
- Career development and advancement opportunities

**Engagement and Participation Strategies:**
- Co-creation and collaborative design sessions
- Pilot programs and prototype development
- Feedback integration and improvement cycles
- Recognition and reward system alignment
- Innovation and idea generation platforms

**CHANGE LEADERSHIP AND GOVERNANCE:**

**Change Leadership Structure:**
- Executive sponsor and steering committee
- Change management office and team
- Business unit change leaders and coordinators
- Change champion network and ambassadors
- Subject matter experts and advisors

**Governance and Decision-Making:**
- Change steering committee oversight
- Progress monitoring and reporting cadence
- Issue escalation and resolution processes
- Resource allocation and investment decisions
- Risk management and mitigation strategies

**MEASUREMENT AND SUCCESS METRICS:**

**Change Success Indicators:**
- Employee engagement and satisfaction scores
- Change readiness and adoption rates
- Training completion and competency development
- Business performance and outcome achievement
- Culture transformation and behavior change

**Communication Effectiveness Measurement:**
- Message awareness and understanding
- Communication channel utilization and feedback
- Leadership credibility and trust levels
- Employee participation and engagement
- Resistance reduction and support building

{industry_context}
{change_type} specific considerations and industry best practices.
{role_focus}
{regulatory_considerations}

Focus on building organizational capability, employee engagement, and sustainable transformation.

{communication_guidance}
""",
            variables={
                "change_type": "strategic transformation",
                "change_scope": "enterprise wide",
                "timeline": "12-18 months"
            },
            context_adaptations={
                "financial_services": "Include regulatory change requirements, compliance training, and risk management implications. Address customer service continuity and stakeholder communication.",
                "technology": "Focus on technical skill development, platform migration, and innovation culture. Address cybersecurity and data privacy considerations.",
                "healthcare": "Emphasize patient safety, clinical quality, and regulatory compliance. Include professional development and accreditation requirements.",
                "ceo": "Frame as CEO transformation leadership with vision communication and organizational alignment. Include board and investor communication.",
                "chro": "Focus on people strategy, talent development, and organizational culture. Emphasize employee experience and engagement."
            },
            quality_criteria=[
                "Comprehensive change strategy with clear vision and rationale",
                "Stakeholder-specific engagement and communication plans",
                "Detailed implementation timeline with measurement metrics",
                "Employee support and development infrastructure",
                "Sustainable change integration and culture transformation"
            ],
            tags=["change_management", "organizational_transformation", "employee_engagement", "communication_strategy"]
        )
        
        # Digital Transformation Communication
        self.templates['digital_transformation_communication'] = PromptTemplate(
            name="Digital Transformation Employee Communication Strategy",
            category=PromptCategory.LEADERSHIP_COMMUNICATION,
            base_prompt="""
Develop comprehensive employee communication strategy for digital transformation initiative addressing technology adoption, skill development, and cultural change over {timeline} period.

**DIGITAL TRANSFORMATION COMMUNICATION FRAMEWORK:**

**DIGITAL VISION AND VALUE PROPOSITION:**

**Digital Future State Vision:**
- Technology-enabled organization and capabilities
- Enhanced customer experience and service delivery
- Operational efficiency and automation benefits
- Innovation acceleration and competitive advantage
- Employee empowerment and productivity enhancement

**Employee Value Proposition:**
- Skill development and career advancement opportunities
- Work experience improvement and job satisfaction
- Technology tools and platform accessibility
- Flexibility and remote work capabilities
- Innovation and creativity enablement

**TECHNOLOGY CHANGE COMMUNICATION:**

**Technology Implementation Roadmap:**
- System modernization and platform migration
- Automation and process digitization
- Data analytics and intelligence capabilities
- Collaboration and communication tools
- Customer-facing technology enhancements

**Employee Impact and Preparation:**
- Role evolution and responsibility changes
- Skill requirements and competency development
- Training program and certification pathways
- Support resources and assistance availability
- Timeline and milestone communication

**DIGITAL SKILL DEVELOPMENT STRATEGY:**

**Competency Assessment and Planning:**
- Current digital skill evaluation
- Future skill requirements identification
- Individual development plan creation
- Learning pathway and resource provision
- Progress tracking and recognition programs

**Training and Development Programs:**
- Technical skill building and certification
- Digital literacy and platform training
- Leadership development in digital environment
- Innovation and agile methodology training
- Change management and adaptation skills

**CULTURE TRANSFORMATION MESSAGING:**

**Digital Culture Values:**
- Innovation and experimentation mindset
- Data-driven decision making
- Collaboration and knowledge sharing
- Continuous learning and development
- Customer-centric and agile thinking

**Behavior Change Communication:**
- New ways of working and collaboration
- Technology adoption and utilization
- Process improvement and optimization
- Cross-functional partnership and integration
- Performance measurement and feedback

**CHANGE RESISTANCE AND SUPPORT:**

**Common Resistance Patterns:**
- Technology anxiety and comfort zone challenges
- Job security and role obsolescence fears
- Workload increase and learning curve concerns
- Generational differences and adaptation speed
- Process disruption and efficiency concerns

**Support and Mitigation Strategies:**
- Personalized training and coaching support
- Mentoring and buddy system programs
- Technology comfort and confidence building
- Career path clarification and development
- Success story sharing and peer learning

**COMMUNICATION CHANNELS AND METHODS:**

**Leadership Communication:**
- Executive vision sharing and commitment demonstration
- Progress updates and milestone celebrations
- Success story highlighting and recognition
- Challenge acknowledgment and support assurance
- Future opportunity communication and inspiration

**Peer-to-Peer Learning:**
- Digital champion network and ambassador program
- Success story sharing and best practice exchange
- Collaboration platform utilization and engagement
- Innovation showcase and idea sharing sessions
- Cross-functional project participation

**MEASUREMENT AND OPTIMIZATION:**

**Digital Adoption Metrics:**
- Technology utilization rates and platform engagement
- Digital skill assessment and competency development
- Employee satisfaction and confidence levels
- Productivity improvement and efficiency gains
- Innovation and idea generation participation

**Communication Effectiveness:**
- Message clarity and understanding assessment
- Communication channel preference and utilization
- Feedback quality and improvement suggestions
- Resistance reduction and support building
- Culture transformation indicators and progress

{industry_context}
Digital transformation specific requirements and technology considerations.
{role_focus}

Focus on employee empowerment, skill development, and sustainable digital culture creation.
""",
            variables={
                "timeline": "18-24 months"
            },
            quality_criteria=[
                "Clear digital vision with employee value proposition",
                "Comprehensive skill development and training strategy",
                "Culture transformation messaging and behavior change",
                "Resistance management and support framework",
                "Measurement and optimization approach"
            ],
            tags=["digital_transformation", "technology_adoption", "skill_development", "culture_change"]
        )
        
        # Organizational Restructuring Communication
        self.templates['restructuring_communication'] = PromptTemplate(
            name="Organizational Restructuring and Employee Communication",
            category=PromptCategory.LEADERSHIP_COMMUNICATION,
            base_prompt="""
Create sensitive and comprehensive communication strategy for organizational restructuring addressing employee concerns, role changes, and organizational effectiveness improvements.

**ORGANIZATIONAL RESTRUCTURING COMMUNICATION:**

**RESTRUCTURING RATIONALE AND VISION:**

**Strategic Business Case:**
- Market dynamics and competitive pressures
- Operational efficiency and cost optimization
- Customer service and experience enhancement
- Growth enablement and capability building
- Long-term sustainability and success positioning

**Organizational Design Principles:**
- Customer-centric organization structure
- Streamlined decision making and accountability
- Enhanced collaboration and communication
- Skill utilization and development optimization
- Agility and responsiveness improvement

**SENSITIVE COMMUNICATION APPROACH:**

**Transparency and Honesty Principles:**
- Clear explanation of necessity and benefits
- Honest assessment of challenges and timeline
- Realistic expectation setting and outcome communication
- Regular update commitment and information sharing
- Open door policy and question encouragement

**Employee-Centric Messaging:**
- Employee value and contribution recognition
- Commitment to fair and respectful treatment
- Support provision and assistance availability
- Career development and opportunity creation
- Long-term employment and growth commitment

**IMPACT COMMUNICATION AND SUPPORT:**

**Role and Responsibility Changes:**
- New organizational chart and reporting relationships
- Role evolution and responsibility expansion
- Skill requirement changes and development support
- Performance expectation and measurement updates
- Career pathway and advancement opportunities

**Transition Support Services:**
- Career counseling and development assistance
- Skill assessment and training program provision
- Internal mobility and placement support
- External placement and outplacement services
- Financial planning and benefit continuation

**TIMING AND SEQUENCING STRATEGY:**

**Pre-Announcement Preparation:**
- Leadership alignment and message consistency
- Manager preparation and briefing sessions
- Support service organization and resource allocation
- Communication material development and approval
- Legal and compliance review and clearance

**Announcement and Initial Communication:**
- Executive leadership announcement and vision sharing
- Department-specific briefings and impact explanation
- Individual meetings and personalized communication
- FAQ development and question addressing
- Support resource activation and availability

**Ongoing Communication and Support:**
- Regular progress updates and milestone communication
- Success story sharing and positive development highlighting
- Challenge acknowledgment and resolution communication
- Feedback collection and concern addressing
- Continuous support and assistance provision

**MANAGER AND SUPERVISOR ENABLEMENT:**

**Leadership Communication Training:**
- Difficult conversation preparation and skill development
- Empathy and emotional intelligence enhancement
- Change leadership and team management
- Performance management during transition
- Recognition and motivation strategy development

**Manager Support Resources:**
- Communication templates and message guidance
- FAQ and response preparation materials
- Employee support resource and referral information
- Performance management tools and techniques
- Team building and morale enhancement strategies

**MORALE AND ENGAGEMENT MAINTENANCE:**

**Culture and Value Reinforcement:**
- Organizational mission and value communication
- Team collaboration and support encouragement
- Innovation and improvement initiative continuation
- Recognition and appreciation program maintenance
- Future vision and opportunity sharing

**Employee Engagement Strategies:**
- Feedback collection and integration processes
- Participation and involvement opportunity creation
- Professional development and learning provision
- Work-life balance and wellness support
- Social connection and team building activities

{industry_context}
Organizational restructuring considerations and industry practices.
{role_focus}

Emphasize empathy, support, and long-term organizational strength building.
""",
            quality_criteria=[
                "Sensitive and empathetic communication approach",
                "Clear rationale and future vision communication",
                "Comprehensive employee support and assistance",
                "Manager enablement and leadership development",
                "Morale maintenance and engagement strategies"
            ],
            tags=["organizational_restructuring", "employee_support", "change_communication", "leadership_development"]
        )
        
        # Register templates
        for template in self.templates.values():
            prompt_manager.register_template(template)
    
    def generate_change_strategy_prompt(self, config: ChangeConfig,
                                      context: Dict[str, Any]) -> str:
        """Generate comprehensive change management strategy prompt."""
        template = self.templates['comprehensive_change_strategy']
        
        variables = {
            'change_type': config.change_type.value.replace('_', ' '),
            'change_scope': config.change_scope.value.replace('_', ' '),
            'timeline': config.timeline
        }
        
        prompt = template.base_prompt
        for key, value in variables.items():
            prompt = prompt.replace(f"{{{key}}}", str(value))
        
        adapted_prompt = context_adapter.adapt_prompt(prompt, context.get('prompt_context'))
        
        return adapted_prompt
    
    def generate_digital_transformation_prompt(self, timeline: str,
                                             context: Dict[str, Any]) -> str:
        """Generate digital transformation communication prompt."""
        template = self.templates['digital_transformation_communication']
        
        variables = {
            'timeline': timeline
        }
        
        prompt = template.base_prompt
        for key, value in variables.items():
            prompt = prompt.replace(f"{{{key}}}", str(value))
        
        adapted_prompt = context_adapter.adapt_prompt(prompt, context.get('prompt_context'))
        
        return adapted_prompt
    
    def generate_restructuring_prompt(self, context: Dict[str, Any]) -> str:
        """Generate organizational restructuring communication prompt."""
        template = self.templates['restructuring_communication']
        
        adapted_prompt = context_adapter.adapt_prompt(template.base_prompt, context.get('prompt_context'))
        
        return adapted_prompt
    
    def get_change_readiness_assessment(self) -> Dict[str, List[str]]:
        """Generate change readiness assessment framework."""
        return {
            'organizational_factors': [
                'Leadership commitment and alignment',
                'Change history and track record',
                'Current performance and financial health',
                'Organizational culture and values',
                'Communication effectiveness and trust'
            ],
            'individual_factors': [
                'Employee engagement and satisfaction',
                'Skill level and development readiness',
                'Change experience and adaptability',
                'Job security and career confidence',
                'Workload and stress levels'
            ],
            'change_factors': [
                'Change scope and complexity',
                'Timeline and urgency pressure',
                'Resource availability and support',
                'Impact magnitude and disruption',
                'Communication clarity and consistency'
            ],
            'support_factors': [
                'Training and development resources',
                'Management capability and preparation',
                'Change champion network strength',
                'Technology and tool availability',
                'Recognition and incentive alignment'
            ]
        }
    
    def generate_change_communication_calendar(self) -> Dict[str, List[str]]:
        """Generate change communication timeline and calendar."""
        return {
            'pre_launch_phase': [
                'Leadership alignment and message development',
                'Change champion identification and training',
                'Communication channel setup and testing',
                'Baseline measurement and assessment',
                'Stakeholder analysis and engagement planning'
            ],
            'launch_phase': [
                'Vision announcement and executive communication',
                'All-hands meetings and department briefings',
                'Manager cascade and supervisor preparation',
                'Employee FAQ and resource publication',
                'Feedback channel activation and monitoring'
            ],
            'implementation_phase': [
                'Weekly progress updates and milestone communication',
                'Training program launch and skill development',
                'Success story sharing and recognition events',
                'Resistance addressing and concern resolution',
                'Continuous feedback collection and integration'
            ],
            'sustainment_phase': [
                'New behavior reinforcement and recognition',
                'Culture integration and value alignment',
                'Lessons learned sharing and best practices',
                'Change capability institutionalization',
                'Future change readiness preparation'
            ]
        }
    
    def generate_resistance_management_framework(self) -> Dict[str, Dict[str, Any]]:
        """Generate change resistance identification and management framework."""
        return {
            'resistance_types': {
                'rational_resistance': {
                    'characteristics': 'Logic-based concerns about change necessity or approach',
                    'management_approach': 'Provide data, evidence, and rational explanations',
                    'communication_strategy': 'Fact-based messaging and business case sharing'
                },
                'emotional_resistance': {
                    'characteristics': 'Fear, anxiety, or emotional attachment to current state',
                    'management_approach': 'Empathy, support, and emotional intelligence',
                    'communication_strategy': 'Personal stories, reassurance, and emotional connection'
                },
                'political_resistance': {
                    'characteristics': 'Power, status, or influence concerns',
                    'management_approach': 'Stakeholder engagement and win-win solutions',
                    'communication_strategy': 'Collaborative approach and benefit highlighting'
                }
            },
            'intervention_strategies': {
                'education_communication': 'Information sharing and awareness building',
                'participation_involvement': 'Co-creation and collaborative design',
                'facilitation_support': 'Training, coaching, and resource provision',
                'negotiation_agreement': 'Compromise and mutual benefit creation',
                'manipulation_cooptation': 'Influence and persuasion techniques',
                'coercion_threats': 'Last resort enforcement and consequences'
            },
            'success_indicators': [
                'Resistance level reduction over time',
                'Employee engagement and participation increase',
                'Feedback quality and constructiveness improvement',
                'Change adoption and behavior modification',
                'Performance and outcome achievement progress'
            ]
        }


# Global change management strategist instance
change_management_strategist = ChangeManagementStrategist()