"""
Executive AI Prompts - Context Adaptation Engine

This module provides industry and role-specific adaptation capabilities
for customizing prompts to executive contexts and business requirements.
"""

from typing import Dict, List, Optional, Callable
from dataclasses import dataclass
from prompt_manager import IndustryType, ExecutiveRole, PromptContext


@dataclass
class AdaptationRule:
    """Rule for adapting prompts based on context."""
    condition: Callable[[PromptContext], bool]
    transformation: Callable[[str, PromptContext], str]
    priority: int = 0
    description: str = ""


class ContextAdapter:
    """Engine for adapting prompts to specific executive contexts."""
    
    def __init__(self):
        self.adaptation_rules: List[AdaptationRule] = []
        self.industry_frameworks = self._initialize_industry_frameworks()
        self.role_perspectives = self._initialize_role_perspectives()
        self.compliance_requirements = self._initialize_compliance_requirements()
        
    def register_rule(self, rule: AdaptationRule) -> None:
        """Register a new adaptation rule."""
        self.adaptation_rules.append(rule)
        self.adaptation_rules.sort(key=lambda r: r.priority, reverse=True)
    
    def adapt_prompt(self, base_prompt: str, context: PromptContext) -> str:
        """Apply context adaptations to a base prompt."""
        adapted_prompt = base_prompt
        
        # Apply industry-specific adaptations
        adapted_prompt = self._apply_industry_adaptation(adapted_prompt, context)
        
        # Apply role-specific adaptations  
        adapted_prompt = self._apply_role_adaptation(adapted_prompt, context)
        
        # Apply compliance requirements
        adapted_prompt = self._apply_compliance_adaptation(adapted_prompt, context)
        
        # Apply custom adaptation rules
        for rule in self.adaptation_rules:
            if rule.condition(context):
                adapted_prompt = rule.transformation(adapted_prompt, context)
        
        # Apply urgency and confidentiality adjustments
        adapted_prompt = self._apply_urgency_adaptation(adapted_prompt, context)
        adapted_prompt = self._apply_confidentiality_adaptation(adapted_prompt, context)
        
        return adapted_prompt
    
    def _apply_industry_adaptation(self, prompt: str, context: PromptContext) -> str:
        """Apply industry-specific terminology and frameworks."""
        framework = self.industry_frameworks.get(context.industry, {})
        
        # Replace generic terms with industry-specific ones
        for generic, specific in framework.get('terminology', {}).items():
            prompt = prompt.replace(f"{{generic_{generic}}}", specific)
        
        # Add industry-specific context
        industry_context = framework.get('context_addition', '')
        if industry_context and '{industry_context}' in prompt:
            prompt = prompt.replace('{industry_context}', industry_context)
        
        # Add regulatory considerations
        regulatory_note = framework.get('regulatory_note', '')
        if regulatory_note and '{regulatory_considerations}' in prompt:
            prompt = prompt.replace('{regulatory_considerations}', regulatory_note)
            
        return prompt
    
    def _apply_role_adaptation(self, prompt: str, context: PromptContext) -> str:
        """Apply role-specific perspective and priorities."""
        perspective = self.role_perspectives.get(context.role, {})
        
        # Adjust focus areas based on role
        focus_areas = perspective.get('focus_areas', [])
        if focus_areas and '{role_focus}' in prompt:
            focus_text = f"Focus particularly on: {', '.join(focus_areas)}"
            prompt = prompt.replace('{role_focus}', focus_text)
        
        # Add role-specific decision criteria
        decision_criteria = perspective.get('decision_criteria', '')
        if decision_criteria and '{decision_framework}' in prompt:
            prompt = prompt.replace('{decision_framework}', decision_criteria)
        
        # Adjust communication style
        communication_style = perspective.get('communication_style', '')
        if communication_style and '{communication_guidance}' in prompt:
            prompt = prompt.replace('{communication_guidance}', communication_style)
            
        return prompt
    
    def _apply_compliance_adaptation(self, prompt: str, context: PromptContext) -> str:
        """Apply compliance and regulatory requirements."""
        requirements = self.compliance_requirements.get(context.industry, [])
        
        if requirements and '{compliance_note}' in prompt:
            compliance_text = "Ensure all recommendations comply with: " + ", ".join(requirements)
            prompt = prompt.replace('{compliance_note}', compliance_text)
            
        return prompt
    
    def _apply_urgency_adaptation(self, prompt: str, context: PromptContext) -> str:
        """Adjust prompt based on urgency level."""
        urgency_adjustments = {
            'critical': 'URGENT: Provide immediate actionable recommendations. ',
            'high': 'High priority: Focus on time-sensitive decisions and actions. ',
            'normal': '',
            'low': 'Consider long-term implications and strategic positioning. '
        }
        
        urgency_prefix = urgency_adjustments.get(context.urgency_level, '')
        if urgency_prefix:
            prompt = urgency_prefix + prompt
            
        return prompt
    
    def _apply_confidentiality_adaptation(self, prompt: str, context: PromptContext) -> str:
        """Adjust prompt based on confidentiality requirements."""
        confidentiality_notes = {
            'restricted': '\n\nNote: This analysis involves highly sensitive information. Ensure all recommendations protect confidential data and competitive advantages.',
            'confidential': '\n\nNote: Maintain confidentiality of all proprietary information in your analysis.',
            'internal': '\n\nNote: This analysis is for internal use and should not reference external benchmarks without approval.',
            'public': ''
        }
        
        confidentiality_note = confidentiality_notes.get(context.confidentiality, '')
        if confidentiality_note:
            prompt += confidentiality_note
            
        return prompt
    
    def _initialize_industry_frameworks(self) -> Dict[IndustryType, Dict]:
        """Initialize industry-specific frameworks and terminology."""
        return {
            IndustryType.FINANCIAL_SERVICES: {
                'terminology': {
                    'customers': 'clients',
                    'products': 'financial products and services',
                    'market': 'financial markets',
                    'competitors': 'financial institutions'
                },
                'context_addition': 'Consider regulatory capital requirements, liquidity ratios, and stress testing scenarios.',
                'regulatory_note': 'Ensure compliance with Basel III, Dodd-Frank, MiFID II, and relevant local banking regulations.'
            },
            IndustryType.HEALTHCARE: {
                'terminology': {
                    'customers': 'patients',
                    'products': 'medical services and treatments',
                    'market': 'healthcare market',
                    'competitors': 'healthcare providers'
                },
                'context_addition': 'Consider patient safety, clinical outcomes, and healthcare delivery efficiency.',
                'regulatory_note': 'Ensure compliance with HIPAA, FDA regulations, Medicare/Medicaid requirements, and clinical safety standards.'
            },
            IndustryType.TECHNOLOGY: {
                'terminology': {
                    'customers': 'users',
                    'products': 'technology solutions',
                    'market': 'technology ecosystem',
                    'competitors': 'technology companies'
                },
                'context_addition': 'Consider scalability, technical debt, cybersecurity, and innovation velocity.',
                'regulatory_note': 'Consider data privacy regulations (GDPR, CCPA), cybersecurity requirements, and platform compliance.'
            },
            IndustryType.MANUFACTURING: {
                'terminology': {
                    'customers': 'customers and supply chain partners',
                    'products': 'manufactured goods',
                    'market': 'manufacturing sector',
                    'competitors': 'manufacturing companies'
                },
                'context_addition': 'Consider operational efficiency, supply chain resilience, and quality management.',
                'regulatory_note': 'Ensure compliance with safety standards, environmental regulations, and industry-specific quality requirements.'
            },
            IndustryType.RETAIL: {
                'terminology': {
                    'customers': 'consumers',
                    'products': 'merchandise and services',
                    'market': 'retail market',
                    'competitors': 'retailers'
                },
                'context_addition': 'Consider consumer behavior, seasonal trends, inventory management, and omnichannel strategy.',
                'regulatory_note': 'Consider consumer protection laws, data privacy requirements, and labor regulations.'
            }
        }
    
    def _initialize_role_perspectives(self) -> Dict[ExecutiveRole, Dict]:
        """Initialize role-specific perspectives and priorities."""
        return {
            ExecutiveRole.CEO: {
                'focus_areas': ['strategic vision', 'stakeholder value', 'competitive positioning', 'organizational culture'],
                'decision_criteria': 'Evaluate based on strategic impact, stakeholder value creation, and long-term competitive advantage.',
                'communication_style': 'Frame recommendations for board presentation and external stakeholder communication.'
            },
            ExecutiveRole.CFO: {
                'focus_areas': ['financial performance', 'risk management', 'capital allocation', 'investor relations'],
                'decision_criteria': 'Prioritize financial impact, ROI, risk-adjusted returns, and capital efficiency.',
                'communication_style': 'Provide quantitative analysis with clear financial metrics and risk assessments.'
            },
            ExecutiveRole.COO: {
                'focus_areas': ['operational efficiency', 'process optimization', 'quality management', 'execution'],
                'decision_criteria': 'Focus on operational impact, execution feasibility, resource requirements, and performance metrics.',
                'communication_style': 'Emphasize implementation details, resource needs, and operational KPIs.'
            },
            ExecutiveRole.CTO: {
                'focus_areas': ['technology strategy', 'innovation', 'digital transformation', 'technical architecture'],
                'decision_criteria': 'Evaluate technical feasibility, scalability, security implications, and innovation potential.',
                'communication_style': 'Balance technical depth with business impact and strategic alignment.'
            },
            ExecutiveRole.BOARD_DIRECTOR: {
                'focus_areas': ['governance', 'oversight', 'strategic guidance', 'risk management'],
                'decision_criteria': 'Focus on governance implications, strategic alignment, and fiduciary responsibilities.',
                'communication_style': 'Provide high-level strategic perspective suitable for board discussions.'
            }
        }
    
    def _initialize_compliance_requirements(self) -> Dict[IndustryType, List[str]]:
        """Initialize compliance requirements by industry."""
        return {
            IndustryType.FINANCIAL_SERVICES: [
                'Basel III capital requirements',
                'Anti-money laundering (AML) regulations',
                'Know Your Customer (KYC) requirements',
                'Securities regulations',
                'Consumer protection laws'
            ],
            IndustryType.HEALTHCARE: [
                'HIPAA privacy requirements',
                'FDA approval processes',
                'Clinical safety standards',
                'Medicare/Medicaid compliance',
                'Healthcare quality measures'
            ],
            IndustryType.TECHNOLOGY: [
                'GDPR data privacy requirements',
                'CCPA consumer privacy laws',
                'Cybersecurity frameworks',
                'Platform compliance standards',
                'Intellectual property protections'
            ]
        }
    
    def get_adaptation_summary(self, context: PromptContext) -> Dict[str, str]:
        """Generate a summary of adaptations that would be applied."""
        summary = {
            'industry_focus': self.industry_frameworks.get(context.industry, {}).get('context_addition', 'Standard business analysis'),
            'role_perspective': self.role_perspectives.get(context.role, {}).get('focus_areas', ['General executive perspective']),
            'compliance_considerations': self.compliance_requirements.get(context.industry, ['Standard business practices']),
            'urgency_adjustment': f"Analysis urgency level: {context.urgency_level}",
            'confidentiality_level': f"Information classification: {context.confidentiality}"
        }
        return summary


# Global context adapter instance
context_adapter = ContextAdapter()