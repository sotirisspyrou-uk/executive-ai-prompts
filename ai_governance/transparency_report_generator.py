"""
Executive AI Prompts - AI Transparency Report Generator

Comprehensive AI transparency reporting, algorithmic accountability frameworks,
and stakeholder communication for responsible AI deployment.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from enum import Enum
from prompt_manager import PromptTemplate, PromptCategory, prompt_manager
from context_adapter import context_adapter


class ReportScope(Enum):
    ENTERPRISE_WIDE = "enterprise_wide_ai"
    PRODUCT_SPECIFIC = "product_specific_ai"
    HIGH_RISK_SYSTEMS = "high_risk_ai_systems"
    CUSTOMER_FACING = "customer_facing_ai"
    REGULATORY_COMPLIANCE = "regulatory_mandated"


class AudienceType(Enum):
    GENERAL_PUBLIC = "general_public"
    CUSTOMERS_USERS = "customers_users"
    REGULATORY_AUTHORITIES = "regulatory_authorities"
    INVESTORS_SHAREHOLDERS = "investors_shareholders"
    TECHNICAL_COMMUNITY = "technical_community"
    MEDIA_STAKEHOLDERS = "media_stakeholders"


class ReportFrequency(Enum):
    ANNUAL = "annual_reporting"
    BIANNUAL = "biannual_reporting"
    QUARTERLY = "quarterly_reporting"
    ON_DEMAND = "on_demand_reporting"


@dataclass
class TransparencyConfig:
    """Configuration for AI transparency reporting."""
    report_scope: ReportScope = ReportScope.ENTERPRISE_WIDE
    target_audience: AudienceType = AudienceType.GENERAL_PUBLIC
    reporting_frequency: ReportFrequency = ReportFrequency.ANNUAL
    technical_detail_level: str = "executive"  # "executive", "detailed", "technical"
    include_metrics: bool = True
    include_case_studies: bool = True
    regulatory_compliance: bool = True


class AITransparencyReportGenerator:
    """Advanced AI transparency reporting and accountability communication."""
    
    def __init__(self):
        self.templates = {}
        self._initialize_templates()
    
    def _initialize_templates(self) -> None:
        """Initialize AI transparency report templates."""
        
        # Comprehensive AI Transparency Report
        self.templates['comprehensive_transparency_report'] = PromptTemplate(
            name="Comprehensive AI Transparency and Accountability Report",
            category=PromptCategory.AI_GOVERNANCE,
            base_prompt="""
As Chief AI Ethics Officer, develop comprehensive AI transparency report covering {report_scope} for {target_audience} with {technical_detail_level} level detail, demonstrating responsible AI deployment and stakeholder accountability.

**AI TRANSPARENCY REPORT STRUCTURE:**

**EXECUTIVE SUMMARY AND KEY MESSAGES:**

**AI Vision and Commitment:**
- Organizational AI mission and ethical principles
- Leadership commitment to responsible AI development
- Stakeholder value creation through trustworthy AI
- Innovation balance with safety and accountability
- Continuous improvement and learning commitment

**Key Highlights and Achievements:**
- Major AI deployments and positive impact outcomes
- Ethical AI milestones and governance improvements
- Stakeholder trust and satisfaction metrics
- Regulatory compliance and standard adherence
- Innovation leadership and industry contributions

**Transparency and Accountability Priorities:**
- Open communication and stakeholder engagement
- Algorithmic accountability and explainability
- Bias mitigation and fairness advancement
- Privacy protection and data stewardship
- Safety assurance and risk management

**AI DEPLOYMENT OVERVIEW AND IMPACT:**

**AI System Portfolio:**
- Customer-facing AI applications and services
- Internal operational AI and automation systems
- Decision support and analytics platforms
- Product and service AI feature integration
- Research and development AI capabilities
- Third-party AI service and platform utilization

**Stakeholder Impact Assessment:**
- Customer experience enhancement and value creation
- Employee productivity and capability augmentation
- Business efficiency and performance improvement
- Social benefit and positive community impact
- Environmental sustainability and resource optimization
- Economic value creation and stakeholder returns

**AI Performance and Outcomes:**
- System accuracy and reliability metrics
- User satisfaction and adoption rates
- Business value realization and ROI measurement
- Error rates and failure analysis
- Performance improvements and optimizations
- Comparative benchmark and industry standards

**ETHICAL AI IMPLEMENTATION:**

**Bias and Fairness Management:**
- Bias detection and measurement methodologies
- Fairness metrics and demographic parity analysis
- Mitigation strategies and corrective measures
- Ongoing monitoring and assessment protocols
- Stakeholder feedback integration and response
- Fairness improvement initiatives and outcomes

**Privacy and Data Protection:**
- Privacy by design implementation and safeguards
- Data minimization and purpose limitation practices
- Consent management and user control mechanisms
- Cross-border transfer compliance and adequacy
- Third-party data sharing governance and oversight
- Privacy incident management and resolution

**Transparency and Explainability:**
- AI decision-making transparency and documentation
- Algorithmic explanation and interpretability provision
- User notification and AI identification requirements
- Stakeholder education and awareness programs
- Public disclosure and information accessibility
- Right to explanation fulfillment and support

**GOVERNANCE AND OVERSIGHT FRAMEWORK:**

**AI Governance Structure:**
- AI Ethics Committee composition and responsibilities
- Executive AI oversight and accountability framework
- Cross-functional AI governance coordination
- Technical AI safety and security expertise
- Legal and compliance AI specialization
- External advisory and independent validation

**Risk Management and Controls:**
- AI risk assessment and management methodology
- Control framework and safeguard implementation
- Continuous monitoring and performance tracking
- Incident response and remediation protocols
- Audit and assurance program execution
- Regulatory compliance and standard adherence

**STAKEHOLDER ENGAGEMENT AND FEEDBACK:**

**Multi-Stakeholder Approach:**
- Customer and user engagement and consultation
- Employee AI literacy and capability development
- Regulatory cooperation and proactive dialogue
- Industry collaboration and standard development
- Academic partnership and research contribution
- Civil society engagement and public interest

**Feedback Integration and Response:**
- Stakeholder feedback collection and analysis
- Concern identification and resolution processes
- Policy adaptation and improvement implementation
- Communication enhancement and transparency increase
- Trust building and relationship strengthening
- Continuous dialogue and engagement maintenance

**REGULATORY COMPLIANCE AND STANDARDS:**

**Regulatory Adherence:**
- EU AI Act compliance and conformity assessment
- US AI regulatory guidance and executive order alignment
- Industry-specific AI regulation and standard compliance
- International AI governance framework participation
- Professional ethics and standard organization engagement
- Emerging regulation monitoring and preparation

**Standards and Certification:**
- ISO/IEC AI standard implementation and compliance
- Industry AI certification and accreditation pursuit
- Third-party validation and independent assessment
- Benchmark participation and performance comparison
- Best practice development and knowledge sharing
- Thought leadership and standard contribution

**PERFORMANCE METRICS AND MEASUREMENT:**

**AI Ethics and Responsibility Metrics:**
- Bias and fairness measurement across demographics
- Privacy compliance and data protection effectiveness
- Transparency and explainability assessment
- User trust and satisfaction survey results
- Incident frequency and resolution effectiveness
- Regulatory compliance and examination performance

**Business and Societal Impact Metrics:**
- Economic value creation and stakeholder benefits
- Social impact and community contribution
- Environmental sustainability and resource efficiency
- Innovation acceleration and capability development
- Market leadership and competitive advantage
- Long-term value creation and sustainability

**FUTURE COMMITMENTS AND ROADMAP:**

**Continuous Improvement Initiatives:**
- AI ethics and governance enhancement priorities
- Technology advancement and capability development
- Stakeholder engagement and trust building programs
- Industry leadership and standard development
- Innovation and research contribution expansion
- Global AI governance and policy participation

**Forward-Looking Commitments:**
- Next-generation AI responsibility and accountability
- Emerging technology ethical integration
- Stakeholder value creation and protection
- Regulatory leadership and proactive compliance
- Industry transformation and positive impact
- Long-term sustainability and societal benefit

{industry_context}
{report_scope} specific applications and stakeholder considerations.
{role_focus}
{regulatory_considerations}

Focus on building stakeholder trust through transparent communication and demonstrated accountability.

{communication_guidance}
""",
            variables={
                "report_scope": "enterprise wide AI",
                "target_audience": "general public",
                "technical_detail_level": "executive"
            },
            context_adaptations={
                "financial_services": "Include algorithmic trading transparency, credit decision fairness, and financial AI consumer protection. Address regulatory compliance and supervisory expectations.",
                "healthcare": "Focus on clinical AI transparency, patient safety assurance, and medical AI decision support. Include regulatory approval and clinical validation processes.",
                "technology": "Emphasize platform AI transparency, user privacy protection, and content moderation. Include developer community and user empowerment initiatives.",
                "ceo": "Frame for stakeholder confidence and brand reputation with strategic positioning and competitive advantage focus.",
                "legal_counsel": "Emphasize legal compliance, liability management, and regulatory relationship with risk mitigation focus."
            ],
            quality_criteria=[
                "Comprehensive AI deployment and impact coverage",
                "Clear ethical AI implementation and governance",
                "Stakeholder-focused communication and engagement",
                "Measurable performance metrics and outcomes",
                "Forward-looking commitment and continuous improvement"
            ],
            tags=["ai_transparency", "accountability_reporting", "stakeholder_communication", "ethical_ai"]
        )
        
        # Algorithmic Impact Assessment Report
        self.templates['algorithmic_impact_assessment'] = PromptTemplate(
            name="Algorithmic Impact Assessment and Disclosure Report",
            category=PromptCategory.AI_GOVERNANCE,
            base_prompt="""
Create comprehensive algorithmic impact assessment report for {ai_system_name} analyzing stakeholder impact, bias evaluation, and mitigation measures with public transparency and accountability.

**ALGORITHMIC IMPACT ASSESSMENT REPORT:**

**SYSTEM OVERVIEW AND PURPOSE:**

**Algorithm Description:**
- System name, version, and deployment date
- Primary purpose and intended use cases
- Target users and affected stakeholder groups
- Integration context and operational environment
- Performance objectives and success criteria
- Expected lifespan and update schedule

**Technical Architecture:**
- Algorithm type and methodological approach
- Input data sources and feature engineering
- Model training and validation methodology
- Output format and decision-making process
- Human oversight and intervention capabilities
- System integration and API specifications

**STAKEHOLDER IMPACT ANALYSIS:**

**Primary Stakeholder Groups:**
- Direct users and service recipients
- Employees and operational staff
- Business partners and ecosystem participants
- Community members and affected populations
- Regulatory authorities and oversight bodies
- Shareholders and organizational stakeholders

**Impact Assessment by Stakeholder:**
- Benefit realization and value creation
- Risk exposure and potential harm
- Rights and interests implications
- Autonomy and agency considerations
- Privacy and data protection impacts
- Economic and social consequences

**BIAS AND FAIRNESS EVALUATION:**

**Bias Assessment Methodology:**
- Training data bias analysis and measurement
- Feature selection and representation evaluation
- Historical discrimination pattern identification
- Demographic group impact assessment
- Intersectional bias and compound discrimination
- Temporal bias and concept drift analysis

**Fairness Metrics and Measurement:**
- Individual fairness and similar treatment
- Demographic parity and statistical parity
- Equalized odds and opportunity equality
- Calibration and predictive parity
- Counterfactual fairness evaluation
- Procedural fairness and process equity

**Fairness Results and Findings:**
- Quantitative fairness metric results
- Demographic group performance comparison
- Bias source identification and analysis
- Fairness trade-off evaluation and decisions
- Stakeholder consultation and feedback integration
- Continuous monitoring and improvement plans

**PRIVACY AND DATA PROTECTION:**

**Data Processing and Privacy:**
- Personal data collection and processing scope
- Legal basis and consent management
- Data minimization and purpose limitation
- Retention period and deletion protocols
- Third-party sharing and transfer governance
- Individual rights fulfillment and support

**Privacy Risk Assessment:**
- Re-identification risk and anonymization adequacy
- Inference attack and privacy leakage potential
- Data aggregation and profiling implications
- Cross-system linking and correlation risks
- Vendor and third-party privacy governance
- International transfer and adequacy assessment

**TRANSPARENCY AND EXPLAINABILITY:**

**Algorithm Transparency:**
- Decision-making process documentation
- Feature importance and influence explanation
- Model behavior and boundary description
- Performance limitation and constraint disclosure
- Update and change notification process
- Stakeholder communication and education

**Individual Explanation Provision:**
- Personalized decision explanation generation
- Right to explanation fulfillment process
- Appeal and review mechanism availability
- Alternative outcome and counterfactual explanation
- Human review and override capability
- Continuous explanation improvement and refinement

**RISK MITIGATION AND SAFEGUARDS:**

**Technical Safeguards:**
- Bias detection and alert mechanisms
- Performance monitoring and drift detection
- Anomaly detection and error handling
- Security controls and access management
- Data quality and integrity validation
- Backup and recovery procedures

**Procedural Safeguards:**
- Human oversight and intervention protocols
- Regular audit and review processes
- Stakeholder feedback and complaint handling
- Issue escalation and resolution procedures
- Performance evaluation and improvement cycles
- Training and competency development programs

**CONTINUOUS MONITORING AND IMPROVEMENT:**

**Performance Monitoring:**
- Key performance indicator tracking and reporting
- Bias and fairness metric continuous measurement
- User feedback and satisfaction assessment
- Incident detection and response evaluation
- Stakeholder impact and outcome monitoring
- Regulatory compliance and standard adherence

**Improvement and Optimization:**
- Performance enhancement and optimization initiatives
- Bias mitigation and fairness improvement measures
- User experience and satisfaction enhancement
- Process refinement and efficiency improvement
- Technology upgrade and modernization planning
- Best practice integration and knowledge sharing

**GOVERNANCE AND ACCOUNTABILITY:**

**Oversight and Accountability:**
- Algorithm owner and accountability assignment
- Governance committee and review board oversight
- Regular assessment and evaluation schedule
- Stakeholder engagement and consultation process
- External validation and independent review
- Public reporting and transparency commitment

**Compliance and Standards:**
- Regulatory requirement compliance verification
- Industry standard and best practice adherence
- Professional ethics and code compliance
- Internal policy and guideline alignment
- Certification and accreditation pursuit
- Continuous compliance monitoring and maintenance

{industry_context}
{ai_system_name} specific impact considerations and stakeholder needs.

Focus on comprehensive impact assessment that supports informed decision-making and public trust.
""",
            variables={
                "ai_system_name": "AI decision-making system"
            },
            quality_criteria=[
                "Comprehensive stakeholder impact analysis",
                "Rigorous bias and fairness evaluation",
                "Clear transparency and explainability provision",
                "Effective risk mitigation and safeguards",
                "Robust governance and accountability framework"
            ],
            tags=["algorithmic_impact", "bias_assessment", "stakeholder_analysis", "public_accountability"]
        )
        
        # AI Ethics Communication Strategy
        self.templates['ai_ethics_communication_strategy'] = PromptTemplate(
            name="AI Ethics and Responsible AI Communication Strategy",
            category=PromptCategory.AI_GOVERNANCE,
            base_prompt="""
Develop comprehensive AI ethics communication strategy for building stakeholder trust, demonstrating responsible AI leadership, and engaging in constructive public dialogue about AI impact and governance.

**AI ETHICS COMMUNICATION STRATEGY:**

**COMMUNICATION VISION AND OBJECTIVES:**

**Core Communication Principles:**
- Transparency and honest communication about AI capabilities and limitations
- Proactive stakeholder engagement and dialogue facilitation
- Educational approach and AI literacy advancement
- Trust building through consistent action and accountability
- Thought leadership and positive industry influence
- Social responsibility and public benefit demonstration

**Strategic Communication Objectives:**
- Build stakeholder trust and confidence in AI deployment
- Demonstrate AI ethics leadership and responsible innovation
- Educate stakeholders about AI benefits and risk management
- Engage constructively in AI policy and regulation development
- Attract and retain talent committed to responsible AI
- Differentiate brand through ethical AI commitment and execution

**STAKEHOLDER-SPECIFIC COMMUNICATION:**

**Customer and User Communication:**
- AI feature and capability explanation and education
- Privacy protection and data stewardship assurance
- Bias mitigation and fairness commitment demonstration
- User control and choice empowerment
- Feedback mechanism and concern resolution
- Value creation and benefit realization highlighting

**Employee and Internal Communication:**
- AI ethics training and capability development
- Responsible AI culture and value integration
- Employee empowerment and AI collaboration
- Career development and future skill building
- Innovation enablement within ethical boundaries
- Pride building and mission alignment reinforcement

**Investor and Shareholder Communication:**
- AI governance and risk management framework
- ESG commitment and performance demonstration
- Long-term value creation through responsible AI
- Regulatory compliance and proactive positioning
- Market leadership and competitive advantage
- Innovation pipeline and future opportunity

**Regulatory and Policy Maker Communication:**
- Proactive engagement and policy dialogue participation
- Industry expertise and best practice sharing
- Regulatory compliance and cooperation demonstration
- Self-regulation and voluntary standard development
- Public-private partnership and collaboration
- Policy research and evidence provision

**PUBLIC COMMUNICATION CHANNELS AND METHODS:**

**Digital Communication Platforms:**
- Company website AI ethics and transparency section
- Social media engagement and thought leadership
- Blog content and technical paper publication
- Podcast participation and speaking engagements
- Video content and documentary participation
- Online community and forum engagement

**Traditional Media and Public Relations:**
- Press release and media statement distribution
- Executive interview and media appearance
- Industry conference and event participation
- Academic conference and research presentation
- Policy forum and public hearing participation
- Awards and recognition pursuit and promotion

**CONTENT STRATEGY AND MESSAGING:**

**Core Messaging Framework:**
- "AI for Good": Positive impact and social benefit focus
- "Responsible Innovation": Balance of advancement and safety
- "Transparent Partnership": Open collaboration and stakeholder engagement
- "Continuous Learning": Commitment to improvement and adaptation
- "Human-Centered AI": Human dignity and empowerment priority
- "Accountable Leadership": Clear responsibility and ethical commitment

**Content Types and Formats:**
- Annual AI transparency and ethics reports
- Case study and success story documentation
- Educational content and AI literacy materials
- Policy position papers and regulatory submissions
- Research collaboration and academic publications
- Interactive tools and demonstration platforms

**CRISIS COMMUNICATION AND REPUTATION MANAGEMENT:**

**AI Incident Communication:**
- Immediate response and stakeholder notification
- Transparent explanation and accountability acceptance
- Corrective action and improvement demonstration
- Ongoing progress update and resolution communication
- Learning integration and prevention measure implementation
- Trust rebuilding and relationship repair

**Reputation Risk Management:**
- Proactive issue identification and early response
- Stakeholder concern monitoring and analysis
- Defensive messaging and fact-based correction
- Expert third-party validation and support
- Industry coalition and peer collaboration
- Long-term reputation recovery and enhancement

**THOUGHT LEADERSHIP AND INDUSTRY ENGAGEMENT:**

**AI Ethics Thought Leadership:**
- Industry standard development and contribution
- Best practice research and methodology sharing
- Policy recommendation and regulatory guidance
- Academic collaboration and research partnership
- International forum and global initiative participation
- Innovation showcase and case study presentation

**Industry Collaboration and Advocacy:**
- Trade association participation and leadership
- Multi-stakeholder initiative and partnership
- Cross-industry working group and committee participation
- Standard setting organization engagement
- Academic and research institution collaboration
- Civil society and NGO partnership

**PERFORMANCE MEASUREMENT AND OPTIMIZATION:**

**Communication Effectiveness Metrics:**
- Stakeholder awareness and understanding measurement
- Trust and confidence indicator tracking
- Engagement rate and quality assessment
- Media coverage and sentiment analysis
- Thought leadership recognition and citation
- Stakeholder feedback and satisfaction evaluation

**Continuous Improvement Process:**
- Regular communication strategy review and update
- Stakeholder feedback integration and response
- Message testing and effectiveness evaluation
- Channel optimization and resource allocation
- Crisis response evaluation and improvement
- Industry benchmark and competitive analysis

{industry_context}
AI ethics communication considerations for {industry} sector.
{role_focus}

Focus on authentic communication that builds lasting stakeholder trust and demonstrates genuine commitment to responsible AI.
""",
            variables={
                "industry": ""
            },
            quality_criteria=[
                "Clear communication vision and stakeholder-specific approach",
                "Comprehensive channel strategy with authentic messaging",
                "Effective crisis communication and reputation management",
                "Thought leadership and industry engagement framework",
                "Performance measurement and continuous improvement"
            ],
            tags=["ai_ethics_communication", "stakeholder_trust", "thought_leadership", "reputation_management"]
        )
        
        # Register templates
        for template in self.templates.values():
            prompt_manager.register_template(template)
    
    def generate_transparency_report_prompt(self, config: TransparencyConfig,
                                          context: Dict[str, Any]) -> str:
        """Generate comprehensive AI transparency report prompt."""
        template = self.templates['comprehensive_transparency_report']
        
        variables = {
            'report_scope': config.report_scope.value.replace('_', ' '),
            'target_audience': config.target_audience.value.replace('_', ' '),
            'technical_detail_level': config.technical_detail_level
        }
        
        prompt = template.base_prompt
        for key, value in variables.items():
            prompt = prompt.replace(f"{{{key}}}", str(value))
        
        adapted_prompt = context_adapter.adapt_prompt(prompt, context.get('prompt_context'))
        
        return adapted_prompt
    
    def generate_algorithmic_impact_prompt(self, ai_system_name: str,
                                         context: Dict[str, Any]) -> str:
        """Generate algorithmic impact assessment prompt."""
        template = self.templates['algorithmic_impact_assessment']
        
        variables = {
            'ai_system_name': ai_system_name
        }
        
        prompt = template.base_prompt
        for key, value in variables.items():
            prompt = prompt.replace(f"{{{key}}}", str(value))
        
        adapted_prompt = context_adapter.adapt_prompt(prompt, context.get('prompt_context'))
        
        return adapted_prompt
    
    def generate_ethics_communication_prompt(self, industry: str,
                                           context: Dict[str, Any]) -> str:
        """Generate AI ethics communication strategy prompt."""
        template = self.templates['ai_ethics_communication_strategy']
        
        variables = {
            'industry': industry
        }
        
        prompt = template.base_prompt
        for key, value in variables.items():
            prompt = prompt.replace(f"{{{key}}}", str(value))
        
        adapted_prompt = context_adapter.adapt_prompt(prompt, context.get('prompt_context'))
        
        return adapted_prompt
    
    def get_transparency_report_framework(self) -> Dict[str, List[str]]:
        """Generate AI transparency report structure framework."""
        return {
            'executive_summary': [
                'AI vision and commitment statement',
                'Key achievements and milestones',
                'Stakeholder impact and value creation',
                'Governance and oversight highlights',
                'Forward-looking commitments'
            ],
            'ai_deployment_overview': [
                'AI system portfolio and applications',
                'Deployment scale and user reach',
                'Performance metrics and outcomes',
                'Business value and stakeholder benefits',
                'Technology evolution and improvements'
            ],
            'ethical_ai_implementation': [
                'Bias detection and mitigation efforts',
                'Privacy protection and data governance',
                'Transparency and explainability measures',
                'Human oversight and control mechanisms',
                'Fairness evaluation and improvement'
            ],
            'governance_and_oversight': [
                'AI governance structure and roles',
                'Risk management and control framework',
                'Audit and assurance processes',
                'Policy development and updates',
                'External validation and certification'
            ],
            'stakeholder_engagement': [
                'Multi-stakeholder consultation processes',
                'Feedback collection and integration',
                'Community engagement and dialogue',
                'Industry collaboration and standards',
                'Academic partnership and research'
            ],
            'performance_and_metrics': [
                'Quantitative performance indicators',
                'Ethics and responsibility metrics',
                'User satisfaction and trust measures',
                'Incident response and resolution',
                'Continuous improvement initiatives'
            ]
        }
    
    def generate_algorithmic_accountability_checklist(self) -> List[str]:
        """Generate algorithmic accountability implementation checklist."""
        return [
            "Clear algorithm purpose and intended use documentation",
            "Comprehensive stakeholder impact assessment completed",
            "Bias detection and measurement methodology implemented",
            "Fairness evaluation across demographic groups conducted",
            "Privacy impact assessment and mitigation measures",
            "Transparency and explainability mechanisms provided",
            "Human oversight and intervention capabilities established",
            "Performance monitoring and drift detection systems",
            "Incident response and remediation procedures defined",
            "Regular audit and review processes scheduled",
            "Stakeholder feedback and complaint mechanisms",
            "Public disclosure and transparency reporting",
            "Regulatory compliance verification and documentation",
            "Continuous improvement and learning integration",
            "External validation and independent assessment arranged"
        ]
    
    def generate_ai_communication_best_practices(self) -> Dict[str, List[str]]:
        """Generate AI communication best practices framework."""
        return {
            'transparency_principles': [
                'Use clear, jargon-free language accessible to your audience',
                'Provide concrete examples and use cases rather than abstract concepts',
                'Acknowledge limitations and uncertainties honestly',
                'Explain both benefits and risks in balanced manner',
                'Update information regularly as systems evolve'
            ],
            'stakeholder_engagement': [
                'Listen actively and respond to stakeholder concerns',
                'Provide multiple channels for feedback and dialogue',
                'Engage early in development process, not just at deployment',
                'Include diverse perspectives in communication planning',
                'Follow up on commitments and report progress'
            ],
            'crisis_communication': [
                'Respond quickly with accurate information',
                'Take responsibility and avoid defensive language',
                'Explain corrective actions and prevention measures',
                'Provide regular updates throughout resolution process',
                'Learn and improve from each incident'
            ],
            'technical_communication': [
                'Adapt technical depth to audience expertise level',
                'Use visualizations and examples to explain complex concepts',
                'Provide links to detailed technical documentation',
                'Offer multiple explanation formats for different learning styles',
                'Validate understanding through feedback and questions'
            ],
            'trust_building': [
                'Demonstrate consistency between words and actions',
                'Share both successes and failures transparently',
                'Involve stakeholders in decision-making processes',
                'Provide evidence and data to support claims',
                'Build long-term relationships through ongoing engagement'
            ]
        }


# Global AI transparency report generator instance
ai_transparency_report_generator = AITransparencyReportGenerator()