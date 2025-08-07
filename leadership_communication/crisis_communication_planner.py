"""
Executive AI Prompts - Crisis Communication Planner

Comprehensive crisis response messaging, stakeholder communication strategies,
and reputation management frameworks for executive leadership.
"""

from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field
from enum import Enum
from prompt_manager import PromptTemplate, PromptCategory, prompt_manager
from context_adapter import context_adapter


class CrisisType(Enum):
    OPERATIONAL = "operational_disruption"
    CYBERSECURITY = "cybersecurity_incident"
    REGULATORY = "regulatory_investigation"
    FINANCIAL = "financial_distress"
    REPUTATION = "reputation_damage"
    SAFETY = "safety_incident"
    ENVIRONMENTAL = "environmental_incident"
    LEADERSHIP = "leadership_crisis"


class CrisisSeverity(Enum):
    LOW = "low_impact"
    MEDIUM = "medium_impact"
    HIGH = "high_impact"
    CRITICAL = "critical_impact"


class StakeholderGroup(Enum):
    CUSTOMERS = "customers"
    EMPLOYEES = "employees"
    INVESTORS = "investors_shareholders"
    REGULATORS = "regulatory_authorities"
    MEDIA = "media_press"
    COMMUNITY = "local_community"
    PARTNERS = "business_partners"
    BOARD = "board_directors"


@dataclass
class CrisisConfig:
    """Configuration for crisis communication planning."""
    crisis_type: CrisisType = CrisisType.OPERATIONAL
    severity: CrisisSeverity = CrisisSeverity.MEDIUM
    affected_stakeholders: List[StakeholderGroup] = field(default_factory=lambda: [StakeholderGroup.CUSTOMERS])
    media_attention: bool = True
    regulatory_involvement: bool = False
    legal_implications: bool = False
    timeline_urgency: str = "immediate"  # "immediate", "24_hours", "72_hours"


class CrisisCommunicationPlanner:
    """Advanced crisis communication and reputation management generator."""
    
    def __init__(self):
        self.templates = {}
        self._initialize_templates()
    
    def _initialize_templates(self) -> None:
        """Initialize crisis communication templates."""
        
        # Comprehensive Crisis Response Plan
        self.templates['comprehensive_crisis_response'] = PromptTemplate(
            name="Comprehensive Crisis Communication Response Plan",
            category=PromptCategory.LEADERSHIP_COMMUNICATION,
            base_prompt="""
As Chief Communications Officer during a {crisis_type} situation with {severity} impact, develop comprehensive crisis communication strategy addressing {affected_stakeholders} within {timeline_urgency} response timeframe.

**CRISIS COMMUNICATION RESPONSE FRAMEWORK:**

**SITUATION ASSESSMENT & MESSAGING FOUNDATION:**

**Crisis Situation Analysis:**
- Incident nature, scope, and immediate impacts
- Stakeholder groups affected and level of impact
- Media attention and public interest assessment
- Regulatory involvement and compliance implications
- Legal considerations and litigation risk evaluation

**Core Message Development:**
- Acknowledgment of situation with appropriate tone
- Demonstration of responsibility and accountability
- Commitment to resolution and corrective action
- Stakeholder protection and support measures
- Transparency and ongoing communication promise

**Key Message Pillars:**
1. **RESPONSIBILITY**: "We take full responsibility and are committed to resolution"
2. **ACTION**: "Immediate steps taken to address the situation and prevent recurrence"
3. **STAKEHOLDER CARE**: "Our priority is protecting and supporting those affected"
4. **TRANSPARENCY**: "We will provide regular updates as information becomes available"
5. **IMPROVEMENT**: "We are learning from this to strengthen our operations"

**STAKEHOLDER-SPECIFIC COMMUNICATION STRATEGY:**

**Customer Communication:**
- Immediate notification and situation explanation
- Impact assessment and customer-specific implications
- Service continuity and alternative solution provision
- Compensation and remediation program details
- Customer support enhancement and dedicated resources

**Employee Communication:**
- Transparent internal briefing and context setting
- Employee safety and job security reassurance
- Role clarity and crisis response participation
- Morale support and leadership visibility
- Regular updates and two-way communication channels

**Investor and Shareholder Communication:**
- Financial impact assessment and disclosure
- Business continuity and recovery plan explanation
- Management response and corrective actions
- Long-term implications and strategic adjustments
- Analyst briefing and investor relations management

**Regulatory Communication:**
- Formal incident notification and compliance reporting
- Cooperation and investigation support commitment
- Corrective action plan and timeline provision
- Regular status updates and progress reporting
- Regulatory relationship management and repair

**Media and Public Communication:**
- Proactive media engagement and statement release
- Key spokesperson designation and message training
- Press briefing and interview preparation
- Social media monitoring and response strategy
- Crisis narrative control and fact-based messaging

**CRISIS COMMUNICATION TIMELINE:**

**IMMEDIATE RESPONSE (0-2 hours):**
- Crisis team activation and command center setup
- Initial stakeholder notification and holding statements
- Media monitoring and social listening activation
- Internal communication and employee briefing
- Regulatory notification and compliance actions

**SHORT-TERM RESPONSE (2-24 hours):**
- Comprehensive stakeholder communication launch
- Media interviews and press conference execution
- Customer service capacity enhancement
- Social media engagement and monitoring
- Initial remediation and corrective action communication

**ONGOING RESPONSE (24-72 hours):**
- Regular stakeholder updates and progress reports
- Media relations management and narrative control
- Customer support and remediation program execution
- Employee engagement and morale management
- Regulatory cooperation and investigation support

**REPUTATION RECOVERY & REBUILDING:**
- Long-term communication strategy and messaging
- Stakeholder trust rebuilding initiatives
- Brand reputation monitoring and management
- Crisis learnings integration and communication
- Organizational culture and improvement storytelling

**CRISIS COMMUNICATION GOVERNANCE:**
- Crisis communication team roles and responsibilities
- Decision-making authority and escalation procedures
- Message approval and quality control processes
- Stakeholder feedback monitoring and response
- Performance measurement and communication effectiveness

{industry_context}
{crisis_type} specific protocols and regulatory requirements.
{regulatory_considerations}
{urgency_level}: Immediate response and stakeholder protection required.

Focus on stakeholder protection, reputation preservation, and organizational resilience.

{communication_guidance}
""",
            variables={
                "crisis_type": "operational disruption",
                "severity": "medium impact",
                "affected_stakeholders": "customers and employees",
                "timeline_urgency": "immediate"
            },
            context_adaptations={
                "financial_services": "Include regulatory reporting requirements, customer data protection, and financial stability messaging. Address supervisory communication and industry reputation.",
                "technology": "Focus on data security, user privacy protection, and platform reliability. Address cybersecurity protocols and technical incident response.",
                "healthcare": "Emphasize patient safety, clinical quality, and regulatory compliance. Address public health implications and medical community concerns.",
                "ceo": "Frame as CEO leadership response with strategic vision and organizational accountability. Include board and shareholder communication priorities.",
                "cmo": "Focus on brand protection, customer communication, and market perception management. Emphasize marketing and public relations coordination."
            ],
            quality_criteria=[
                "Comprehensive stakeholder analysis with tailored messaging",
                "Clear crisis response timeline with immediate actions",
                "Professional crisis communication strategy with governance",
                "Reputation protection and recovery framework",
                "Regulatory compliance and legal risk management"
            ],
            tags=["crisis_communication", "reputation_management", "stakeholder_engagement", "emergency_response"]
        )
        
        # Media Relations Crisis Management
        self.templates['media_relations_crisis'] = PromptTemplate(
            name="Crisis Media Relations and Public Communications",
            category=PromptCategory.LEADERSHIP_COMMUNICATION,
            base_prompt="""
Develop comprehensive media relations strategy for {crisis_situation} crisis with proactive media engagement, narrative control, and public perception management.

**MEDIA RELATIONS CRISIS FRAMEWORK:**

**MEDIA STRATEGY DEVELOPMENT:**

**Media Landscape Assessment:**
- Traditional media outlets and key journalists
- Digital media and social platform dynamics
- Industry trade publications and specialists
- Local and regional media considerations
- International media attention and implications

**Narrative Strategy:**
- Core story and key message development
- Fact-based narrative with supporting evidence
- Proactive story positioning and context setting
- Defensive messaging for challenging questions
- Long-term reputation recovery narrative

**MEDIA COMMUNICATION EXECUTION:**

**Press Statement and Release:**
```
FOR IMMEDIATE RELEASE
[Company Logo and Header]

[HEADLINE: Clear, Direct, and Factual]

[City, Date] - [Company Name] today announced [brief situation description] and outlined immediate response actions to address the situation and support affected stakeholders.

"[CEO/Leadership Quote expressing responsibility, action, and commitment]"

KEY FACTS:
• Situation description and scope
• Immediate response actions taken
• Stakeholder protection measures
• Investigation and corrective actions
• Ongoing communication commitment

[Company commitment statement and next steps]

For more information:
[Media Contact Information]
[Company Website and Updates Page]
```

**Press Conference Planning:**
- Spokesperson designation and message training
- Key talking points and Q&A preparation
- Visual materials and supporting documentation
- Logistics coordination and media accommodation
- Follow-up interview scheduling and management

**MEDIA INTERVIEW PREPARATION:**

**Key Messages and Talking Points:**
- Opening statement and situation acknowledgment
- Responsibility acceptance and leadership accountability
- Immediate action summary and ongoing response
- Stakeholder protection and support measures
- Long-term improvement and prevention commitments

**Difficult Question Preparation:**
- Liability and legal responsibility questions
- Financial impact and business implications
- Prevention and oversight failure inquiries
- Competitive advantage and market position
- Timeline and resolution expectation management

**Message Discipline Framework:**
- Bridge phrases to return to key messages
- Fact-based responses with supporting data
- "What we know/don't know" transparency approach
- Future-focused improvement and prevention messaging
- Stakeholder care and protection emphasis

**SOCIAL MEDIA CRISIS MANAGEMENT:**

**Social Media Response Strategy:**
- Platform-specific messaging and engagement
- Real-time monitoring and response protocols
- Community management and customer service
- Influencer engagement and advocacy building
- Negative sentiment management and mitigation

**Content Strategy:**
- Regular updates and progress communications
- Visual content and infographics for clarity
- Employee advocacy and authentic storytelling
- Customer testimonials and support showcasing
- Behind-the-scenes recovery and improvement content

**REPUTATION MONITORING & MANAGEMENT:**

**Media Coverage Analysis:**
- Traditional and digital media sentiment tracking
- Key message penetration and narrative control
- Journalist relationship and coverage quality
- Competitive media comparison and benchmarking
- Long-term reputation trend monitoring

**Public Perception Management:**
- Stakeholder feedback and sentiment analysis
- Community engagement and relationship repair
- Industry positioning and thought leadership
- Crisis learnings communication and transparency
- Organizational culture and values demonstration

{industry_context}
{crisis_situation} specific media considerations and industry protocols.
{regulatory_considerations}

Focus on maintaining credibility, controlling narrative, and protecting long-term reputation.
""",
            variables={
                "crisis_situation": "operational crisis"
            },
            quality_criteria=[
                "Professional media strategy with clear messaging",
                "Comprehensive press materials and interview preparation",
                "Social media crisis management framework",
                "Reputation monitoring and recovery planning",
                "Stakeholder communication integration"
            ],
            tags=["media_relations", "public_communications", "reputation_management", "crisis_response"]
        )
        
        # Internal Crisis Communication
        self.templates['internal_crisis_communication'] = PromptTemplate(
            name="Internal Crisis Communication and Employee Engagement",
            category=PromptCategory.LEADERSHIP_COMMUNICATION,
            base_prompt="""
Create comprehensive internal communication strategy during {crisis_type} crisis focusing on employee engagement, morale management, and organizational unity.

**INTERNAL CRISIS COMMUNICATION FRAMEWORK:**

**EMPLOYEE COMMUNICATION STRATEGY:**

**Leadership Communication Cascade:**
- Executive leadership unified messaging
- Management team briefing and alignment
- Supervisor and team leader preparation
- Frontline employee engagement and support
- Cross-functional coordination and collaboration

**Communication Channels and Methods:**
- All-hands meetings and town halls
- Executive video messages and updates
- Email communications and newsletters
- Intranet and internal portal updates
- Team meetings and department briefings

**IMMEDIATE EMPLOYEE COMMUNICATION (Crisis Announcement):**

**CEO Message to All Employees:**
```
Subject: Important Update - [Crisis Situation] Response

Dear [Company] Team,

I want to personally update you on a situation that requires our immediate attention and unified response.

[SITUATION DESCRIPTION]
• What happened: [Clear, factual description]
• Impact scope: [Who and what is affected]
• Immediate actions: [Steps already taken]

[EMPLOYEE ASSURANCE]
• Your safety and job security are our top priorities
• We are taking all necessary steps to protect our team
• Regular updates will be provided as information becomes available

[COMPANY RESPONSE]
• Leadership team is fully engaged and coordinating response
• We are working with [relevant authorities/partners]
• Our values guide our response and decision-making

[EMPLOYEE EXPECTATIONS]
• Continue focusing on serving our customers with excellence
• Follow established protocols and procedures
• Direct questions to your manager or HR team
• Maintain confidentiality and professional communication

Thank you for your dedication during this challenging time.

[CEO Name and Title]
```

**ONGOING EMPLOYEE ENGAGEMENT:**

**Regular Update Communications:**
- Weekly progress updates and milestone achievements
- Transparent communication about challenges and setbacks
- Employee question and answer sessions
- Success stories and positive developments
- Long-term outlook and recovery planning

**Employee Support and Resources:**
- Employee assistance programs and counseling
- Flexible work arrangements and accommodations
- Training and development continuity
- Recognition and appreciation programs
- Career development and advancement assurance

**TWO-WAY COMMUNICATION CHANNELS:**
- Employee feedback surveys and pulse checks
- Anonymous suggestion and concern submission
- Management office hours and open door policies
- Employee resource groups and representatives
- Cross-functional crisis response team participation

**ORGANIZATIONAL CULTURE AND MORALE:**

**Culture Reinforcement During Crisis:**
- Company values demonstration through actions
- Leadership visibility and accessibility
- Team collaboration and mutual support
- Innovation and problem-solving encouragement
- Long-term vision and purpose communication

**Morale Management Strategies:**
- Achievement celebration and milestone recognition
- Team building activities and engagement events
- Professional development and learning opportunities
- Community service and giving initiatives
- Future planning and growth discussions

**CRISIS RECOVERY AND LEARNING:**

**Post-Crisis Communication:**
- Lessons learned and improvement integration
- Employee contribution recognition and appreciation
- Organizational strength and resilience demonstration
- Future preparedness and capability building
- Culture evolution and values reinforcement

**Knowledge Management:**
- Crisis response documentation and best practices
- Employee training and preparedness enhancement
- Process improvement and system strengthening
- Communication effectiveness evaluation
- Organizational learning and development integration

{industry_context}
{crisis_type} specific employee considerations and industry practices.

Focus on maintaining employee trust, engagement, and organizational resilience throughout crisis.
""",
            variables={
                "crisis_type": "operational disruption"
            },
            quality_criteria=[
                "Clear, honest, and transparent employee communication",
                "Comprehensive employee support and resource provision",
                "Two-way communication and feedback mechanisms",
                "Culture and morale management during crisis",
                "Long-term organizational learning and improvement"
            ],
            tags=["internal_communication", "employee_engagement", "crisis_management", "organizational_culture"]
        )
        
        # Register templates
        for template in self.templates.values():
            prompt_manager.register_template(template)
    
    def generate_crisis_response_prompt(self, config: CrisisConfig,
                                      context: Dict[str, Any]) -> str:
        """Generate comprehensive crisis response communication prompt."""
        template = self.templates['comprehensive_crisis_response']
        
        stakeholders_text = " and ".join([s.value.replace('_', ' ') for s in config.affected_stakeholders])
        
        variables = {
            'crisis_type': config.crisis_type.value.replace('_', ' '),
            'severity': config.severity.value.replace('_', ' '),
            'affected_stakeholders': stakeholders_text,
            'timeline_urgency': config.timeline_urgency.replace('_', ' ')
        }
        
        prompt = template.base_prompt
        for key, value in variables.items():
            prompt = prompt.replace(f"{{{key}}}", str(value))
        
        adapted_prompt = context_adapter.adapt_prompt(prompt, context.get('prompt_context'))
        
        return adapted_prompt
    
    def generate_media_relations_prompt(self, crisis_situation: str,
                                      context: Dict[str, Any]) -> str:
        """Generate media relations crisis management prompt."""
        template = self.templates['media_relations_crisis']
        
        variables = {
            'crisis_situation': crisis_situation
        }
        
        prompt = template.base_prompt
        for key, value in variables.items():
            prompt = prompt.replace(f"{{{key}}}", str(value))
        
        adapted_prompt = context_adapter.adapt_prompt(prompt, context.get('prompt_context'))
        
        return adapted_prompt
    
    def generate_internal_communication_prompt(self, crisis_type: str,
                                             context: Dict[str, Any]) -> str:
        """Generate internal crisis communication prompt."""
        template = self.templates['internal_crisis_communication']
        
        variables = {
            'crisis_type': crisis_type
        }
        
        prompt = template.base_prompt
        for key, value in variables.items():
            prompt = prompt.replace(f"{{{key}}}", str(value))
        
        adapted_prompt = context_adapter.adapt_prompt(prompt, context.get('prompt_context'))
        
        return adapted_prompt
    
    def get_crisis_communication_checklist(self) -> Dict[str, List[str]]:
        """Generate crisis communication response checklist."""
        return {
            'immediate_response_0_2_hours': [
                'Activate crisis communication team',
                'Assess situation and gather initial facts',
                'Develop holding statements for all stakeholders',
                'Notify key executives and board members',
                'Begin media monitoring and social listening',
                'Prepare internal employee notification',
                'Contact legal counsel and regulatory bodies',
                'Set up crisis command center and communications hub'
            ],
            'short_term_response_2_24_hours': [
                'Release official statements to stakeholders',
                'Conduct media briefings and interviews',
                'Launch customer communication and support programs',
                'Enhance customer service capacity and resources',
                'Execute employee town halls and updates',
                'Engage with regulatory authorities and compliance teams',
                'Monitor social media and respond to inquiries',
                'Update website and digital channels with information'
            ],
            'medium_term_response_24_72_hours': [
                'Provide regular stakeholder progress updates',
                'Conduct follow-up media interviews and briefings',
                'Launch remediation and customer compensation programs',
                'Execute comprehensive employee support initiatives',
                'Begin reputation recovery and rebuilding efforts',
                'Engage with community and local stakeholders',
                'Coordinate with industry partners and associations',
                'Prepare detailed incident reports and analysis'
            ],
            'long_term_recovery_ongoing': [
                'Develop comprehensive reputation recovery strategy',
                'Integrate crisis learnings into organizational processes',
                'Strengthen stakeholder relationships and trust',
                'Enhance crisis preparedness and response capabilities',
                'Monitor long-term reputation and brand perception',
                'Communicate organizational improvements and changes',
                'Update crisis communication plans and procedures',
                'Conduct crisis response evaluation and improvement'
            ]
        }
    
    def generate_stakeholder_messaging_matrix(self) -> Dict[str, Dict[str, str]]:
        """Generate stakeholder-specific messaging matrix."""
        return {
            'customers': {
                'primary_concern': 'Service disruption and personal impact',
                'key_messages': [
                    'Your data and accounts are secure and protected',
                    'We are working to restore full service as quickly as possible',
                    'Customer support is available 24/7 for assistance',
                    'We will make this right with appropriate compensation'
                ],
                'communication_channels': 'Email, SMS, website, customer service, social media',
                'tone': 'Apologetic, reassuring, action-oriented'
            },
            'employees': {
                'primary_concern': 'Job security and organizational stability',
                'key_messages': [
                    'Your jobs and benefits are secure during this situation',
                    'We need your continued dedication and professionalism',
                    'Leadership is taking full responsibility and action',
                    'This challenge will make us stronger as an organization'
                ],
                'communication_channels': 'All-hands meetings, email, intranet, team meetings',
                'tone': 'Honest, supportive, unifying, inspiring'
            },
            'investors': {
                'primary_concern': 'Financial impact and business viability',
                'key_messages': [
                    'Financial impact is manageable and quantified',
                    'Business fundamentals remain strong',
                    'Management is taking decisive corrective action',
                    'Long-term strategy and growth remain on track'
                ],
                'communication_channels': 'Investor calls, SEC filings, analyst briefings, press releases',
                'tone': 'Factual, confident, forward-looking, transparent'
            },
            'media': {
                'primary_concern': 'Story accuracy and public interest',
                'key_messages': [
                    'We are committed to full transparency and cooperation',
                    'Facts are still being gathered and will be shared',
                    'We take full responsibility and are taking action',
                    'Our priority is protecting those affected'
                ],
                'communication_channels': 'Press releases, interviews, briefings, statements',
                'tone': 'Professional, factual, accountable, accessible'
            }
        }
    
    def generate_crisis_severity_protocols(self) -> Dict[str, Dict[str, Any]]:
        """Generate crisis response protocols by severity level."""
        return {
            'low_impact': {
                'response_time': 'Within 4 hours',
                'leadership_involvement': 'Department head and communications team',
                'stakeholder_notification': 'Affected customers and relevant employees',
                'media_strategy': 'Reactive only, prepared statements available',
                'escalation_triggers': [
                    'Media inquiry received',
                    'Regulatory interest expressed',
                    'Customer complaints exceed threshold',
                    'Social media attention increases'
                ]
            },
            'medium_impact': {
                'response_time': 'Within 2 hours',
                'leadership_involvement': 'Executive team and crisis communication team',
                'stakeholder_notification': 'All affected stakeholders, proactive communication',
                'media_strategy': 'Proactive engagement, press release, spokesperson available',
                'escalation_triggers': [
                    'Impact spreads to additional stakeholder groups',
                    'Financial impact exceeds materiality threshold',
                    'Regulatory investigation initiated',
                    'Negative media coverage intensifies'
                ]
            },
            'high_impact': {
                'response_time': 'Within 1 hour',
                'leadership_involvement': 'CEO, full executive team, board notification',
                'stakeholder_notification': 'Immediate notification to all stakeholder groups',
                'media_strategy': 'Full media engagement, press conference, multiple spokespeople',
                'escalation_triggers': [
                    'National media attention',
                    'Regulatory enforcement action',
                    'Legal action initiated',
                    'Industry-wide implications'
                ]
            },
            'critical_impact': {
                'response_time': 'Immediate (within 30 minutes)',
                'leadership_involvement': 'CEO leadership, emergency board meeting, external advisors',
                'stakeholder_notification': 'Emergency notifications, crisis hotlines activated',
                'media_strategy': 'Crisis press conference, CEO interviews, 24/7 media response',
                'special_considerations': [
                    'Government and regulatory coordination',
                    'Industry association engagement',
                    'Third-party crisis management support',
                    'Legal and litigation management'
                ]
            }
        }


# Global crisis communication planner instance
crisis_communication_planner = CrisisCommunicationPlanner()