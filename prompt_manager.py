"""
Executive AI Prompts - Central Prompt Management System

This module provides the core infrastructure for managing executive-level AI prompts,
including dynamic customization, template variables, and quality validation.
"""

from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass, field
from enum import Enum
import json
import uuid
from datetime import datetime


class IndustryType(Enum):
    FINANCIAL_SERVICES = "financial_services"
    HEALTHCARE = "healthcare" 
    TECHNOLOGY = "technology"
    MANUFACTURING = "manufacturing"
    RETAIL = "retail"
    ENERGY = "energy"
    CONSULTING = "consulting"
    GENERAL = "general"


class ExecutiveRole(Enum):
    CEO = "ceo"
    CFO = "cfo"
    COO = "coo"
    CTO = "cto"
    BOARD_DIRECTOR = "board_director"
    VP_STRATEGY = "vp_strategy"
    VP_OPERATIONS = "vp_operations"


class PromptCategory(Enum):
    STRATEGIC_ANALYSIS = "strategic_analysis"
    FINANCIAL_ANALYSIS = "financial_analysis"
    LEADERSHIP_COMMUNICATION = "leadership_communication"
    MARKET_INTELLIGENCE = "market_intelligence"
    OPERATIONAL_EXCELLENCE = "operational_excellence"
    AI_GOVERNANCE = "ai_governance"


@dataclass
class PromptContext:
    """Context information for prompt customization."""
    industry: IndustryType
    role: ExecutiveRole
    company_size: str  # "startup", "mid_market", "enterprise", "fortune_500"
    region: str = "global"
    specific_focus: Optional[str] = None
    urgency_level: str = "normal"  # "low", "normal", "high", "critical"
    confidentiality: str = "internal"  # "public", "internal", "confidential", "restricted"


@dataclass
class PromptTemplate:
    """Core prompt template structure."""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = ""
    category: PromptCategory = PromptCategory.STRATEGIC_ANALYSIS
    base_prompt: str = ""
    variables: Dict[str, Any] = field(default_factory=dict)
    context_adaptations: Dict[str, str] = field(default_factory=dict)
    quality_criteria: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
    version: str = "1.0.0"
    tags: List[str] = field(default_factory=list)


@dataclass
class PromptExecution:
    """Record of prompt execution for analytics."""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    prompt_id: str = ""
    context: PromptContext = None
    generated_prompt: str = ""
    response: str = ""
    quality_score: Optional[float] = None
    execution_time: datetime = field(default_factory=datetime.now)
    feedback: Optional[Dict[str, Any]] = None


class PromptManager:
    """Central management system for executive AI prompts."""
    
    def __init__(self):
        self.templates: Dict[str, PromptTemplate] = {}
        self.executions: List[PromptExecution] = []
        self.context_adapters: Dict[str, callable] = {}
        
    def register_template(self, template: PromptTemplate) -> str:
        """Register a new prompt template."""
        self.templates[template.id] = template
        return template.id
    
    def get_template(self, template_id: str) -> Optional[PromptTemplate]:
        """Retrieve a prompt template by ID."""
        return self.templates.get(template_id)
    
    def list_templates(self, category: Optional[PromptCategory] = None) -> List[PromptTemplate]:
        """List all templates, optionally filtered by category."""
        templates = list(self.templates.values())
        if category:
            templates = [t for t in templates if t.category == category]
        return sorted(templates, key=lambda x: x.name)
    
    def generate_prompt(self, template_id: str, context: PromptContext, 
                       variables: Optional[Dict[str, Any]] = None) -> str:
        """Generate a customized prompt based on template and context."""
        template = self.get_template(template_id)
        if not template:
            raise ValueError(f"Template {template_id} not found")
        
        # Start with base prompt
        prompt = template.base_prompt
        
        # Apply context adaptations
        context_key = f"{context.industry.value}_{context.role.value}"
        if context_key in template.context_adaptations:
            prompt = template.context_adaptations[context_key]
        elif context.industry.value in template.context_adaptations:
            prompt = template.context_adaptations[context.industry.value]
        elif context.role.value in template.context_adaptations:
            prompt = template.context_adaptations[context.role.value]
        
        # Apply variable substitution
        all_variables = {**template.variables}
        if variables:
            all_variables.update(variables)
            
        # Add context variables
        all_variables.update({
            'industry': context.industry.value.replace('_', ' ').title(),
            'role': context.role.value.replace('_', ' ').title(), 
            'company_size': context.company_size.replace('_', ' ').title(),
            'region': context.region.title(),
            'urgency_level': context.urgency_level,
            'confidentiality': context.confidentiality
        })
        
        # Perform variable substitution
        for key, value in all_variables.items():
            placeholder = f"{{{key}}}"
            if placeholder in prompt:
                prompt = prompt.replace(placeholder, str(value))
        
        return prompt
    
    def execute_prompt(self, template_id: str, context: PromptContext,
                      variables: Optional[Dict[str, Any]] = None) -> PromptExecution:
        """Execute a prompt and record the execution."""
        generated_prompt = self.generate_prompt(template_id, context, variables)
        
        execution = PromptExecution(
            prompt_id=template_id,
            context=context,
            generated_prompt=generated_prompt
        )
        
        self.executions.append(execution)
        return execution
    
    def update_execution_response(self, execution_id: str, response: str, 
                                 quality_score: Optional[float] = None) -> bool:
        """Update execution with response and quality score."""
        for execution in self.executions:
            if execution.id == execution_id:
                execution.response = response
                execution.quality_score = quality_score
                return True
        return False
    
    def get_usage_analytics(self, category: Optional[PromptCategory] = None,
                          industry: Optional[IndustryType] = None,
                          role: Optional[ExecutiveRole] = None) -> Dict[str, Any]:
        """Generate usage analytics for prompts."""
        filtered_executions = self.executions
        
        if category or industry or role:
            filtered_executions = []
            for execution in self.executions:
                template = self.get_template(execution.prompt_id)
                if category and template and template.category != category:
                    continue
                if industry and execution.context and execution.context.industry != industry:
                    continue
                if role and execution.context and execution.context.role != role:
                    continue
                filtered_executions.append(execution)
        
        total_executions = len(filtered_executions)
        avg_quality = None
        quality_scores = [e.quality_score for e in filtered_executions if e.quality_score is not None]
        
        if quality_scores:
            avg_quality = sum(quality_scores) / len(quality_scores)
        
        popular_templates = {}
        for execution in filtered_executions:
            template_id = execution.prompt_id
            popular_templates[template_id] = popular_templates.get(template_id, 0) + 1
        
        return {
            'total_executions': total_executions,
            'average_quality_score': avg_quality,
            'popular_templates': sorted(popular_templates.items(), 
                                      key=lambda x: x[1], reverse=True)[:10],
            'execution_count_by_day': self._get_executions_by_day(filtered_executions)
        }
    
    def _get_executions_by_day(self, executions: List[PromptExecution]) -> Dict[str, int]:
        """Group executions by day for analytics."""
        by_day = {}
        for execution in executions:
            day = execution.execution_time.strftime('%Y-%m-%d')
            by_day[day] = by_day.get(day, 0) + 1
        return by_day
    
    def export_templates(self, category: Optional[PromptCategory] = None) -> str:
        """Export templates to JSON format."""
        templates_to_export = self.list_templates(category)
        
        export_data = {
            'templates': [
                {
                    'id': t.id,
                    'name': t.name,
                    'category': t.category.value,
                    'base_prompt': t.base_prompt,
                    'variables': t.variables,
                    'context_adaptations': t.context_adaptations,
                    'quality_criteria': t.quality_criteria,
                    'version': t.version,
                    'tags': t.tags,
                    'created_at': t.created_at.isoformat()
                } for t in templates_to_export
            ],
            'export_timestamp': datetime.now().isoformat()
        }
        
        return json.dumps(export_data, indent=2)
    
    def import_templates(self, json_data: str) -> List[str]:
        """Import templates from JSON format."""
        data = json.loads(json_data)
        imported_ids = []
        
        for template_data in data.get('templates', []):
            template = PromptTemplate(
                id=template_data.get('id', str(uuid.uuid4())),
                name=template_data['name'],
                category=PromptCategory(template_data['category']),
                base_prompt=template_data['base_prompt'],
                variables=template_data.get('variables', {}),
                context_adaptations=template_data.get('context_adaptations', {}),
                quality_criteria=template_data.get('quality_criteria', []),
                version=template_data.get('version', '1.0.0'),
                tags=template_data.get('tags', []),
                created_at=datetime.fromisoformat(template_data.get('created_at', datetime.now().isoformat()))
            )
            
            template_id = self.register_template(template)
            imported_ids.append(template_id)
        
        return imported_ids


# Global prompt manager instance
prompt_manager = PromptManager()