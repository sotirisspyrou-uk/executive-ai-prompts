"""
Executive AI Prompts - AI Risk Assessment Framework

Comprehensive AI implementation risk evaluation, ethical decision-making
frameworks, and AI governance strategy for executive leadership.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from enum import Enum
from prompt_manager import PromptTemplate, PromptCategory, prompt_manager
from context_adapter import context_adapter


class AIRiskType(Enum):
    BIAS_FAIRNESS = "bias_discrimination_fairness"
    PRIVACY_SECURITY = "privacy_data_security"
    TRANSPARENCY_EXPLAINABILITY = "transparency_explainability"
    SAFETY_RELIABILITY = "safety_system_reliability"
    REGULATORY_COMPLIANCE = "regulatory_legal_compliance"
    ETHICAL_SOCIAL = "ethical_social_impact"
    OPERATIONAL_TECHNICAL = "operational_technical_risk"
    STRATEGIC_BUSINESS = "strategic_business_risk"


class AIDeploymentScope(Enum):
    CUSTOMER_FACING = "customer_facing_applications"
    INTERNAL_OPERATIONS = "internal_operational_systems"
    DECISION_SUPPORT = "decision_support_analytics"
    PRODUCT_SERVICES = "product_service_features"
    ENTERPRISE_PLATFORM = "enterprise_wide_platform"


class AIMaturityLevel(Enum):
    EXPERIMENTAL = "pilot_experimental"
    LIMITED_PRODUCTION = "limited_production"
    FULL_DEPLOYMENT = "full_scale_deployment"
    ENTERPRISE_SCALE = "enterprise_wide_adoption"


@dataclass
class AIRiskConfig:
    """Configuration for AI risk assessment."""
    risk_types: List[AIRiskType] = field(default_factory=lambda: [AIRiskType.BIAS_FAIRNESS, AIRiskType.PRIVACY_SECURITY])
    deployment_scope: AIDeploymentScope = AIDeploymentScope.CUSTOMER_FACING
    maturity_level: AIMaturityLevel = AIMaturityLevel.LIMITED_PRODUCTION
    industry_sensitivity: str = "high"  # "low", "medium", "high", "critical"
    regulatory_oversight: bool = True
    stakeholder_impact: str = "significant"  # "minimal", "moderate", "significant", "critical"


class AIRiskAssessmentPrompts:
    """Advanced AI risk assessment and governance framework generator."""
    
    def __init__(self):
        self.templates = {}
        self._initialize_templates()
    
    def _initialize_templates(self) -> None:
        """Initialize AI risk assessment templates."""
        
        # Comprehensive AI Risk Assessment
        self.templates['comprehensive_ai_risk_assessment'] = PromptTemplate(
            name="Comprehensive AI Risk Assessment and Governance Framework",
            category=PromptCategory.AI_GOVERNANCE,
            base_prompt="""
As Chief AI Officer conducting comprehensive AI risk assessment for {deployment_scope} systems at {maturity_level} scale, evaluate {risk_types} risks and develop enterprise AI governance framework with stakeholder protection and ethical compliance.

**AI RISK ASSESSMENT FRAMEWORK:**

**AI SYSTEM CLASSIFICATION AND SCOPE:**

**AI Application Categories:**
- Customer-facing AI systems and services
- Internal operational and workflow automation
- Decision support and analytics platforms
- Product feature and service enhancement
- Enterprise infrastructure and platform AI
- Data processing and insight generation

**Risk Classification Matrix:**
- High-risk AI: Significant stakeholder impact potential
- Medium-risk AI: Moderate operational or customer impact
- Low-risk AI: Limited impact with existing safeguards
- Prohibited AI: Unacceptable risk applications
- Human oversight requirements by risk category
- Regulatory compliance obligations by classification

**BIAS AND FAIRNESS RISK ASSESSMENT:**

**Algorithmic Bias Identification:**
- Training data bias and representation gaps
- Feature selection and model architecture bias
- Historical discrimination perpetuation risks
- Demographic group disparate impact analysis
- Intersectional bias and compound discrimination
- Feedback loop amplification and reinforcement

**Fairness Framework Implementation:**
- Individual fairness and similar treatment principles
- Group fairness and demographic parity standards
- Equalized odds and opportunity frameworks
- Counterfactual fairness and causal reasoning
- Procedural fairness and transparent processes
- Corrective measures and bias mitigation strategies

**PRIVACY AND DATA SECURITY RISKS:**

**Data Protection and Privacy:**
- Personal data collection, processing, and storage
- Consent management and user control mechanisms
- Data minimization and purpose limitation compliance
- Cross-border data transfer and sovereignty
- Re-identification risks and anonymization adequacy
- Third-party data sharing and vendor management

**AI Security Risk Management:**
- Adversarial attacks and model poisoning
- Data poisoning and training set manipulation
- Model stealing and intellectual property protection
- Inference attacks and privacy leakage
- System availability and denial of service
- Secure deployment and access control

**TRANSPARENCY AND EXPLAINABILITY:**

**AI Explainability Requirements:**
- Decision-making process transparency
- Model interpretability and feature importance
- Automated decision explanation generation
- Human-readable output and reasoning
- Stakeholder-appropriate explanation levels
- Right to explanation and algorithmic auditing

**Transparency Framework:**
- AI system documentation and disclosure
- Algorithm impact assessment publication
- Performance metrics and limitation communication
- Data source and methodology transparency
- Continuous monitoring and reporting mechanisms
- Stakeholder feedback and improvement integration

**SAFETY AND RELIABILITY ASSURANCE:**

**AI System Reliability:**
- Performance consistency and stability
- Edge case handling and graceful degradation
- Error detection and recovery mechanisms
- System monitoring and anomaly detection
- Fail-safe design and human override capability
- Quality assurance and testing protocols

**Safety-Critical Applications:**
- Human safety impact assessment
- Critical system integration and dependencies
- Emergency response and incident management
- Backup systems and redundancy planning
- Safety validation and certification requirements
- Continuous safety monitoring and updates

**ETHICAL AND SOCIAL IMPACT EVALUATION:**

**Ethical AI Principles:**
- Human dignity and autonomy respect
- Beneficence and non-maleficence adherence
- Justice and fairness in AI application
- Transparency and accountability maintenance
- Human oversight and meaningful control
- Social good and positive impact optimization

**Societal Impact Assessment:**
- Employment and workforce displacement
- Social inequality and digital divide implications
- Cultural sensitivity and value alignment
- Democratic participation and civic engagement
- Human agency and decision-making autonomy
- Community benefit and stakeholder value

**AI GOVERNANCE AND OVERSIGHT FRAMEWORK:**

**AI Governance Structure:**
- AI Ethics Committee and oversight board
- Cross-functional AI governance team
- Business unit AI coordinators and champions
- Technical AI safety and security specialists
- Legal and compliance AI expertise
- External advisory and independent oversight

**Risk Management Process:**
- Pre-deployment risk assessment and approval
- Ongoing monitoring and performance evaluation
- Incident response and remediation protocols
- Regular audit and compliance verification
- Stakeholder feedback and grievance handling
- Continuous improvement and learning integration

**REGULATORY COMPLIANCE AND STANDARDS:**

**AI Regulatory Landscape:**
- EU AI Act compliance and conformity assessment
- US AI executive orders and agency guidance
- Industry-specific AI regulations and standards
- International AI governance and coordination
- Professional and ethical standards adherence
- Emerging AI liability and accountability frameworks

**Compliance Implementation:**
- Regulatory mapping and requirement analysis
- Compliance monitoring and reporting systems
- Documentation and record-keeping protocols
- Third-party validation and certification
- Regulatory relationship and engagement management
- Policy adaptation and update processes

**STAKEHOLDER ENGAGEMENT AND COMMUNICATION:**

**Multi-Stakeholder Approach:**
- Customer trust and transparency building
- Employee AI literacy and capability development
- Investor confidence and ESG compliance
- Regulatory cooperation and proactive engagement
- Community dialogue and social license
- Industry collaboration and standard setting

**Communication Strategy:**
- AI transparency reports and public disclosure
- Stakeholder education and awareness programs
- Incident communication and response protocols
- Success story sharing and positive impact highlighting
- Feedback collection and concern addressing
- Thought leadership and policy contribution

{industry_context}
{deployment_scope} specific AI applications and risk considerations.
{regulatory_considerations}
{role_focus}

Focus on responsible AI deployment that protects stakeholders while enabling innovation and competitive advantage.

{communication_guidance}
""",
            variables={
                "deployment_scope": "customer facing applications",
                "maturity_level": "limited production",
                "risk_types": "bias and privacy"
            },
            context_adaptations={
                "financial_services": "Include model risk management, algorithmic trading oversight, credit decision fairness, and regulatory capital implications for AI systems.",
                "healthcare": "Focus on clinical AI safety, patient privacy protection, diagnostic accuracy, and medical device regulation compliance.",
                "technology": "Emphasize platform liability, user privacy protection, content moderation, and AI safety research and development.",
                "ceo": "Frame for board governance and strategic risk management with competitive advantage and stakeholder value focus.",
                "cio": "Focus on technical implementation, system integration, and operational risk management with security and performance emphasis."
            ],
            quality_criteria=[
                "Comprehensive AI risk identification across all dimensions",
                "Practical governance framework with clear accountability",
                "Stakeholder protection and ethical compliance integration",
                "Regulatory compliance and standards adherence",
                "Continuous monitoring and improvement mechanisms"
            ],
            tags=["ai_risk_assessment", "ai_governance", "ethical_ai", "regulatory_compliance"]
        )
        
        # AI Ethics Decision Framework
        self.templates['ai_ethics_decision_framework'] = PromptTemplate(
            name="AI Ethics Decision-Making and Implementation Framework",
            category=PromptCategory.AI_GOVERNANCE,
            base_prompt="""
Develop comprehensive AI ethics decision-making framework for evaluating AI projects, implementations, and applications with stakeholder impact assessment and ethical compliance.

**AI ETHICS DECISION FRAMEWORK:**

**ETHICAL AI PRINCIPLES AND VALUES:**

**Core Ethical Principles:**
1. **Human Dignity and Autonomy:**
   - Respect for human agency and decision-making
   - Meaningful human control and oversight
   - Individual privacy and consent protection
   - Freedom from manipulation and coercion
   - Support for human flourishing and well-being

2. **Fairness and Non-Discrimination:**
   - Equal treatment and opportunity provision
   - Bias prevention and mitigation
   - Inclusive design and accessibility
   - Demographic parity and equitable outcomes
   - Historical injustice correction and remediation

3. **Transparency and Accountability:**
   - Explainable and interpretable AI systems
   - Clear responsibility and liability assignment
   - Open communication about AI capabilities and limitations
   - Stakeholder participation in AI development
   - Regular auditing and performance evaluation

4. **Beneficence and Social Good:**
   - Positive societal impact maximization
   - Harm prevention and risk minimization
   - Public benefit and common good promotion
   - Sustainable development and environmental protection
   - Social justice and inequality reduction

**ETHICAL DECISION-MAKING PROCESS:**

**Phase 1: Ethical Impact Assessment**
- Stakeholder identification and impact analysis
- Potential benefit and harm evaluation
- Rights and interests consideration
- Cultural and contextual sensitivity assessment
- Long-term consequence and precedent evaluation

**Phase 2: Ethical Analysis and Deliberation**
- Ethical principle application and trade-off analysis
- Alternative approach evaluation and comparison
- Stakeholder consultation and feedback integration
- Expert advisory and independent review
- Consensus building and decision documentation

**Phase 3: Implementation and Monitoring**
- Ethical safeguard integration and deployment
- Ongoing monitoring and impact assessment
- Stakeholder feedback collection and analysis
- Course correction and improvement implementation
- Learning integration and knowledge sharing

**AI ETHICS COMMITTEE STRUCTURE:**

**Ethics Committee Composition:**
- Executive sponsor and senior leadership
- Technical AI expertise and development teams
- Legal and compliance professionals
- Ethics and philosophy subject matter experts
- Diverse stakeholder representation
- External advisory and independent oversight

**Committee Responsibilities:**
- AI ethics policy development and maintenance
- AI project ethical review and approval
- Ethical incident investigation and response
- Ethics training and awareness program oversight
- Stakeholder engagement and communication
- Ethics performance measurement and reporting

**STAKEHOLDER IMPACT ASSESSMENT:**

**Primary Stakeholder Groups:**
- End users and customers directly affected by AI
- Employees whose work is augmented or replaced
- Communities and societies impacted by AI deployment
- Business partners and ecosystem participants
- Regulatory authorities and compliance oversight
- Future generations and long-term societal impact

**Impact Evaluation Criteria:**
- Magnitude and scope of potential impact
- Probability and uncertainty of outcomes
- Reversibility and mitigation possibilities
- Distribution of benefits and burdens
- Consent and voluntary participation
- Alternative options and choice availability

**ETHICAL AI IMPLEMENTATION GUIDELINES:**

**Design Phase Ethics Integration:**
- Inclusive and participatory design processes
- Diverse team composition and perspective integration
- Ethical requirement specification and documentation
- Risk assessment and mitigation planning
- Stakeholder consultation and feedback incorporation
- Ethical testing and validation protocols

**Deployment Phase Safeguards:**
- Graduated rollout and controlled deployment
- Real-time monitoring and performance tracking
- User education and expectation management
- Feedback collection and concern addressing
- Incident response and remediation protocols
- Continuous improvement and optimization

**ETHICAL DILEMMA RESOLUTION:**

**Common AI Ethical Dilemmas:**
- Privacy vs. utility trade-offs in data use
- Individual fairness vs. group equality optimization
- Transparency vs. competitive advantage protection
- Innovation speed vs. safety assurance
- Human oversight vs. system efficiency
- Local vs. global ethical standard application

**Resolution Framework:**
- Ethical principle prioritization and weighting
- Stakeholder consultation and consensus building
- Expert advisory and independent review
- Precedent analysis and consistency maintenance
- Documentation and rationale recording
- Monitoring and course correction planning

**ETHICS PERFORMANCE MEASUREMENT:**

**Ethical AI Metrics:**
- Bias and fairness measurement across demographics
- User satisfaction and trust indicators
- Complaint and grievance resolution effectiveness
- Transparency and explainability assessment
- Social impact and benefit realization
- Compliance and standard adherence

**Continuous Improvement Process:**
- Regular ethics review and assessment
- Stakeholder feedback integration and response
- Best practice identification and sharing
- Policy update and guideline refinement
- Training and capability development
- Industry collaboration and standard contribution

{industry_context}
AI ethics considerations specific to {industry} sector applications.
{role_focus}

Focus on practical ethical decision-making that enables responsible innovation and stakeholder trust.
""",
            variables={
                "industry": ""
            },
            quality_criteria=[
                "Clear ethical principles and decision-making process",
                "Comprehensive stakeholder impact assessment",
                "Practical implementation guidelines and safeguards",
                "Effective governance structure and oversight",
                "Performance measurement and continuous improvement"
            ],
            tags=["ai_ethics", "ethical_decision_making", "stakeholder_impact", "responsible_innovation"]
        )
        
        # AI Compliance and Audit Framework
        self.templates['ai_compliance_audit_framework'] = PromptTemplate(
            name="AI Compliance and Audit Framework",
            category=PromptCategory.AI_GOVERNANCE,
            base_prompt="""
Create comprehensive AI compliance and audit framework ensuring regulatory adherence, risk management, and continuous improvement in AI system governance and oversight.

**AI COMPLIANCE AND AUDIT FRAMEWORK:**

**REGULATORY COMPLIANCE LANDSCAPE:**

**Global AI Regulation Overview:**
- EU AI Act: High-risk AI system compliance and conformity assessment
- US AI Executive Orders: Federal agency AI governance and oversight
- China AI Regulations: Algorithm recommendation and data security
- UK AI White Paper: Principles-based regulatory approach
- Canada AIDA: Proposed Artificial Intelligence and Data Act
- Industry-specific AI regulations and standards

**Compliance Requirements by AI Risk Category:**

**High-Risk AI Systems:**
- Risk management system implementation
- Data governance and quality assurance
- Technical documentation and record keeping
- Transparency and information provision
- Human oversight and intervention capability
- Accuracy, robustness, and cybersecurity measures
- Conformity assessment and CE marking (EU)

**Limited Risk AI Systems:**
- Transparency obligations and user notification
- Clear identification as AI-generated content
- Manipulation and deception prevention
- User consent and interaction clarity
- Performance monitoring and quality control

**AI AUDIT METHODOLOGY:**

**Pre-Deployment Audit:**
- Requirements specification and design review
- Training data quality and bias assessment
- Model performance and fairness evaluation
- Security and privacy protection verification
- Documentation completeness and accuracy
- Stakeholder impact and ethical assessment
- Regulatory compliance verification

**Ongoing Operational Audit:**
- Performance monitoring and drift detection
- Fairness and bias measurement across groups
- Security incident and vulnerability assessment
- User feedback and complaint analysis
- Data quality and integrity verification
- Human oversight effectiveness evaluation
- Compliance maintenance and updates

**Post-Incident Audit:**
- Root cause analysis and impact assessment
- Response adequacy and timeliness evaluation
- Stakeholder communication effectiveness
- System recovery and remediation verification
- Process improvement and learning integration
- Regulatory reporting and cooperation assessment

**COMPLIANCE MANAGEMENT SYSTEM:**

**Policy and Procedure Framework:**
- AI governance policy and standard operating procedures
- Risk assessment and management protocols
- Data governance and quality assurance procedures
- Model development and validation standards
- Deployment approval and oversight processes
- Incident response and remediation protocols

**Documentation and Record Keeping:**
- AI system inventory and classification records
- Risk assessment and mitigation documentation
- Training data provenance and quality records
- Model performance and testing results
- Deployment approval and oversight documentation
- Incident reports and resolution records

**AUDIT EXECUTION FRAMEWORK:**

**Internal Audit Program:**
- Annual audit plan and schedule development
- Risk-based audit scope and priority setting
- Audit team training and competency development
- Audit execution and evidence collection
- Finding documentation and recommendation development
- Management response and corrective action tracking

**External Audit and Validation:**
- Third-party audit firm selection and management
- Regulatory examination preparation and cooperation
- Industry benchmark and peer comparison
- Certification and accreditation pursuit
- External validation and assurance programs
- Stakeholder audit result communication

**AUDIT FINDINGS AND REMEDIATION:**

**Finding Classification and Prioritization:**
- Critical findings requiring immediate action
- Significant findings with compliance risk
- Moderate findings for improvement opportunity
- Minor findings with best practice enhancement
- Observation and advisory recommendations

**Remediation Process:**
- Corrective action plan development and approval
- Resource allocation and timeline establishment
- Implementation monitoring and progress tracking
- Effectiveness validation and verification
- Documentation update and process improvement
- Lesson learned integration and sharing

**CONTINUOUS IMPROVEMENT INTEGRATION:**

**Audit Learning and Enhancement:**
- Audit finding trend analysis and pattern identification
- Root cause analysis and systemic issue addressing
- Process improvement and efficiency enhancement
- Training and capability development needs assessment
- Technology tool and automation opportunity identification
- Industry best practice and standard integration

**Performance Measurement and Reporting:**
- Compliance performance metrics and KPI tracking
- Audit effectiveness and efficiency measurement
- Stakeholder satisfaction and confidence assessment
- Regulatory relationship and examination performance
- Incident response and resolution effectiveness
- Continuous improvement and innovation metrics

{industry_context}
AI compliance requirements specific to {industry} sector.
{regulatory_considerations}

Focus on proactive compliance management that supports innovation while ensuring regulatory adherence and stakeholder protection.
""",
            quality_criteria=[
                "Comprehensive regulatory compliance coverage",
                "Risk-based audit methodology and execution",
                "Effective compliance management system",
                "Continuous improvement and learning integration",
                "Stakeholder confidence and regulatory relationship"
            ],
            tags=["ai_compliance", "ai_audit", "regulatory_adherence", "continuous_improvement"]
        )
        
        # Register templates
        for template in self.templates.values():
            prompt_manager.register_template(template)
    
    def generate_ai_risk_assessment_prompt(self, config: AIRiskConfig,
                                         context: Dict[str, Any]) -> str:
        """Generate comprehensive AI risk assessment prompt."""
        template = self.templates['comprehensive_ai_risk_assessment']
        
        risk_types_text = " and ".join([t.value.replace('_', ' ') for t in config.risk_types])
        
        variables = {
            'deployment_scope': config.deployment_scope.value.replace('_', ' '),
            'maturity_level': config.maturity_level.value.replace('_', ' '),
            'risk_types': risk_types_text
        }
        
        prompt = template.base_prompt
        for key, value in variables.items():
            prompt = prompt.replace(f"{{{key}}}", str(value))
        
        adapted_prompt = context_adapter.adapt_prompt(prompt, context.get('prompt_context'))
        
        return adapted_prompt
    
    def generate_ai_ethics_framework_prompt(self, industry: str,
                                          context: Dict[str, Any]) -> str:
        """Generate AI ethics decision-making framework prompt."""
        template = self.templates['ai_ethics_decision_framework']
        
        variables = {
            'industry': industry
        }
        
        prompt = template.base_prompt
        for key, value in variables.items():
            prompt = prompt.replace(f"{{{key}}}", str(value))
        
        adapted_prompt = context_adapter.adapt_prompt(prompt, context.get('prompt_context'))
        
        return adapted_prompt
    
    def generate_ai_compliance_audit_prompt(self, context: Dict[str, Any]) -> str:
        """Generate AI compliance and audit framework prompt."""
        template = self.templates['ai_compliance_audit_framework']
        
        adapted_prompt = context_adapter.adapt_prompt(template.base_prompt, context.get('prompt_context'))
        
        return adapted_prompt
    
    def get_ai_risk_taxonomy(self) -> Dict[str, List[str]]:
        """Generate comprehensive AI risk taxonomy."""
        return {
            'technical_risks': [
                'Model performance degradation and concept drift',
                'Adversarial attacks and security vulnerabilities',
                'Data quality issues and training set bias',
                'System integration and compatibility problems',
                'Scalability and performance bottlenecks',
                'Algorithm explanation and interpretability gaps'
            ],
            'operational_risks': [
                'Human oversight and intervention failures',
                'Process integration and workflow disruption',
                'Change management and user adoption challenges',
                'Vendor dependency and third-party risks',
                'Business continuity and disaster recovery',
                'Cost overruns and resource allocation issues'
            ],
            'ethical_risks': [
                'Algorithmic bias and discriminatory outcomes',
                'Privacy invasion and consent violations',
                'Autonomy reduction and human agency loss',
                'Transparency and explainability deficits',
                'Fairness and justice concerns',
                'Social manipulation and behavior influence'
            ],
            'legal_regulatory_risks': [
                'Regulatory non-compliance and penalties',
                'Liability and accountability uncertainty',
                'Intellectual property and patent disputes',
                'Data protection law violations',
                'Consumer protection and safety standards',
                'International regulation and jurisdiction conflicts'
            ],
            'reputational_risks': [
                'Public trust and brand damage',
                'Stakeholder confidence erosion',
                'Media criticism and negative coverage',
                'Customer dissatisfaction and defection',
                'Employee morale and talent retention',
                'Investor concern and ESG impact'
            ],
            'strategic_risks': [
                'Competitive disadvantage and market position loss',
                'Innovation pace and technology obsolescence',
                'Business model disruption and value creation',
                'Strategic dependency and vendor lock-in',
                'Market acceptance and adoption rates',
                'Economic impact and cost-benefit realization'
            ]
        }
    
    def generate_ai_governance_maturity_model(self) -> Dict[str, Dict[str, str]]:
        """Generate AI governance maturity assessment model."""
        return {
            'level_1_initial': {
                'description': 'Ad hoc AI development with minimal governance',
                'characteristics': 'Informal processes, limited risk awareness, reactive approach',
                'focus_areas': 'Basic policy development, team education, risk identification'
            },
            'level_2_managed': {
                'description': 'Basic AI governance policies and procedures established',
                'characteristics': 'Documented processes, risk-based approach, management oversight',
                'focus_areas': 'Process standardization, risk assessment, compliance framework'
            },
            'level_3_defined': {
                'description': 'Comprehensive AI governance framework implemented',
                'characteristics': 'Standardized processes, integrated risk management, stakeholder engagement',
                'focus_areas': 'Process optimization, advanced risk management, stakeholder value'
            },
            'level_4_quantitatively_managed': {
                'description': 'Data-driven AI governance with performance measurement',
                'characteristics': 'Metrics-based management, predictive capabilities, continuous improvement',
                'focus_areas': 'Performance optimization, predictive risk management, innovation enablement'
            },
            'level_5_optimized': {
                'description': 'Continuously improving AI governance with innovation leadership',
                'characteristics': 'Innovation leadership, adaptive processes, industry benchmark setting',
                'focus_areas': 'Industry leadership, ecosystem development, transformational innovation'
            }
        }
    
    def generate_ai_incident_response_framework(self) -> Dict[str, Any]:
        """Generate AI incident response and management framework."""
        return {
            'incident_classification': {
                'severity_1_critical': {
                    'definition': 'Immediate safety risk or significant harm potential',
                    'response_time': '< 1 hour',
                    'escalation': 'CEO and board notification required'
                },
                'severity_2_high': {
                    'definition': 'Significant bias, discrimination, or privacy breach',
                    'response_time': '< 4 hours',
                    'escalation': 'Executive team and legal counsel engagement'
                },
                'severity_3_medium': {
                    'definition': 'Performance degradation or user experience issues',
                    'response_time': '< 24 hours',
                    'escalation': 'Management team and technical leads involvement'
                },
                'severity_4_low': {
                    'definition': 'Minor issues with limited impact',
                    'response_time': '< 72 hours',
                    'escalation': 'Team lead and technical resolution'
                }
            },
            'response_process': [
                'Incident detection and initial assessment',
                'Immediate containment and harm mitigation',
                'Stakeholder notification and communication',
                'Root cause analysis and investigation',
                'Remediation implementation and validation',
                'Lessons learned integration and improvement'
            ],
            'communication_strategy': [
                'Internal stakeholder notification and coordination',
                'Customer communication and expectation management',
                'Regulatory reporting and cooperation',
                'Media relations and public communication',
                'Employee update and morale management',
                'Partner and vendor coordination'
            ]
        }


# Global AI risk assessment prompts instance
ai_risk_assessment_prompts = AIRiskAssessmentPrompts()