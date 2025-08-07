"""
Executive AI Prompts - Quality Validation System

This module provides comprehensive quality assessment and validation
for AI-generated executive-level content and recommendations.
"""

from typing import Dict, List, Optional, Tuple, Callable
from dataclasses import dataclass, field
from enum import Enum
import re
import statistics
from datetime import datetime


class QualityDimension(Enum):
    STRATEGIC_RELEVANCE = "strategic_relevance"
    EXECUTIVE_APPROPRIATENESS = "executive_appropriateness"  
    ACTIONABILITY = "actionability"
    BUSINESS_IMPACT = "business_impact"
    CLARITY = "clarity"
    COMPLETENESS = "completeness"
    ACCURACY = "accuracy"
    COMPLIANCE = "compliance"
    STAKEHOLDER_ALIGNMENT = "stakeholder_alignment"
    TIME_SENSITIVITY = "time_sensitivity"


@dataclass 
class QualityMetric:
    """Definition of a quality assessment metric."""
    dimension: QualityDimension
    weight: float  # 0.0 to 1.0
    evaluator: Callable[[str, Dict], float]  # Returns score 0.0 to 10.0
    description: str = ""
    min_threshold: float = 6.0


@dataclass
class QualityAssessment:
    """Results of quality validation."""
    content_id: str
    overall_score: float
    dimension_scores: Dict[QualityDimension, float] = field(default_factory=dict)
    passed_threshold: bool = False
    recommendations: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    assessed_at: datetime = field(default_factory=datetime.now)


class QualityValidator:
    """Comprehensive quality validation system for executive content."""
    
    def __init__(self):
        self.metrics: Dict[QualityDimension, QualityMetric] = {}
        self.assessment_history: List[QualityAssessment] = []
        self._initialize_default_metrics()
    
    def register_metric(self, metric: QualityMetric) -> None:
        """Register a quality assessment metric."""
        self.metrics[metric.dimension] = metric
    
    def validate_content(self, content: str, context: Dict = None, 
                        content_id: Optional[str] = None) -> QualityAssessment:
        """Perform comprehensive quality validation of content."""
        if context is None:
            context = {}
        
        if content_id is None:
            content_id = f"content_{datetime.now().timestamp()}"
        
        assessment = QualityAssessment(content_id=content_id)
        
        # Evaluate each quality dimension
        weighted_scores = []
        for dimension, metric in self.metrics.items():
            try:
                score = metric.evaluator(content, context)
                score = max(0.0, min(10.0, score))  # Clamp to 0-10 range
                assessment.dimension_scores[dimension] = score
                weighted_scores.append(score * metric.weight)
                
                # Check threshold
                if score < metric.min_threshold:
                    assessment.warnings.append(
                        f"{dimension.value} score ({score:.1f}) below threshold ({metric.min_threshold})"
                    )
            except Exception as e:
                assessment.warnings.append(f"Error evaluating {dimension.value}: {str(e)}")
                assessment.dimension_scores[dimension] = 0.0
        
        # Calculate overall score
        if weighted_scores:
            total_weight = sum(metric.weight for metric in self.metrics.values())
            assessment.overall_score = sum(weighted_scores) / total_weight if total_weight > 0 else 0
        
        # Determine pass/fail
        assessment.passed_threshold = (
            assessment.overall_score >= 7.0 and 
            len(assessment.warnings) == 0
        )
        
        # Generate recommendations
        assessment.recommendations = self._generate_recommendations(assessment, content, context)
        
        # Store assessment
        self.assessment_history.append(assessment)
        
        return assessment
    
    def _initialize_default_metrics(self) -> None:
        """Initialize default quality metrics for executive content."""
        
        # Strategic Relevance
        self.register_metric(QualityMetric(
            dimension=QualityDimension.STRATEGIC_RELEVANCE,
            weight=0.2,
            evaluator=self._evaluate_strategic_relevance,
            description="Alignment with strategic business objectives",
            min_threshold=7.0
        ))
        
        # Executive Appropriateness  
        self.register_metric(QualityMetric(
            dimension=QualityDimension.EXECUTIVE_APPROPRIATENESS,
            weight=0.18,
            evaluator=self._evaluate_executive_appropriateness,
            description="Appropriate tone and complexity for executive audience",
            min_threshold=7.0
        ))
        
        # Actionability
        self.register_metric(QualityMetric(
            dimension=QualityDimension.ACTIONABILITY,
            weight=0.16,
            evaluator=self._evaluate_actionability,
            description="Contains clear, actionable recommendations",
            min_threshold=6.0
        ))
        
        # Business Impact
        self.register_metric(QualityMetric(
            dimension=QualityDimension.BUSINESS_IMPACT,
            weight=0.15,
            evaluator=self._evaluate_business_impact,
            description="Addresses significant business impact and value creation",
            min_threshold=6.0
        ))
        
        # Clarity
        self.register_metric(QualityMetric(
            dimension=QualityDimension.CLARITY,
            weight=0.12,
            evaluator=self._evaluate_clarity,
            description="Clear communication and logical structure",
            min_threshold=7.0
        ))
        
        # Completeness
        self.register_metric(QualityMetric(
            dimension=QualityDimension.COMPLETENESS,
            weight=0.1,
            evaluator=self._evaluate_completeness,
            description="Comprehensive coverage of key aspects",
            min_threshold=6.0
        ))
        
        # Compliance
        self.register_metric(QualityMetric(
            dimension=QualityDimension.COMPLIANCE,
            weight=0.09,
            evaluator=self._evaluate_compliance,
            description="Adherence to regulatory and policy requirements",
            min_threshold=8.0
        ))
    
    def _evaluate_strategic_relevance(self, content: str, context: Dict) -> float:
        """Evaluate strategic relevance of content."""
        score = 5.0  # Base score
        
        strategic_terms = [
            'strategic', 'strategy', 'competitive advantage', 'market position',
            'long-term', 'vision', 'mission', 'objectives', 'goals',
            'stakeholders', 'value creation', 'transformation', 'growth'
        ]
        
        # Count strategic terminology
        strategic_count = sum(1 for term in strategic_terms if term.lower() in content.lower())
        score += min(3.0, strategic_count * 0.3)
        
        # Check for strategic frameworks
        frameworks = ['swot', 'porter', 'competitive analysis', 'market analysis', 'scenario planning']
        if any(framework in content.lower() for framework in frameworks):
            score += 1.0
        
        # Check for forward-looking perspective
        future_terms = ['forecast', 'projection', 'trend', 'outlook', 'future', 'emerging']
        if any(term in content.lower() for term in future_terms):
            score += 0.5
        
        return min(10.0, score)
    
    def _evaluate_executive_appropriateness(self, content: str, context: Dict) -> float:
        """Evaluate appropriateness for executive audience."""
        score = 5.0
        
        # Check for executive-level language
        executive_terms = [
            'recommend', 'propose', 'decision', 'leadership', 'governance',
            'oversight', 'accountability', 'responsibility', 'authority'
        ]
        exec_count = sum(1 for term in executive_terms if term.lower() in content.lower())
        score += min(2.0, exec_count * 0.2)
        
        # Check for appropriate complexity (not too technical)
        technical_terms = ['algorithm', 'implementation', 'coding', 'debugging', 'API']
        if sum(1 for term in technical_terms if term.lower() in content.lower()) > 3:
            score -= 1.0
        
        # Check for business value focus
        value_terms = ['ROI', 'revenue', 'profit', 'cost', 'investment', 'return']
        if any(term.lower() in content.lower() for term in value_terms):
            score += 1.0
        
        # Check for stakeholder perspective
        stakeholder_terms = ['board', 'shareholders', 'investors', 'customers', 'employees']
        if any(term.lower() in content.lower() for term in stakeholder_terms):
            score += 1.0
        
        return min(10.0, score)
    
    def _evaluate_actionability(self, content: str, context: Dict) -> float:
        """Evaluate actionability of recommendations."""
        score = 3.0
        
        # Look for action words
        action_words = [
            'implement', 'establish', 'develop', 'create', 'launch', 'initiate',
            'execute', 'deploy', 'adopt', 'invest', 'acquire', 'divest'
        ]
        action_count = sum(1 for word in action_words if word.lower() in content.lower())
        score += min(3.0, action_count * 0.3)
        
        # Look for structured recommendations
        if re.search(r'\d+\.\s', content) or re.search(r'•\s', content):
            score += 1.0
        
        # Look for timelines or priorities
        time_terms = ['immediate', 'short-term', 'long-term', 'Q1', 'Q2', 'Q3', 'Q4', 'month', 'year']
        if any(term.lower() in content.lower() for term in time_terms):
            score += 1.0
        
        # Look for responsibility assignments
        responsibility_terms = ['team', 'department', 'role', 'owner', 'accountable']
        if any(term.lower() in content.lower() for term in responsibility_terms):
            score += 1.0
        
        return min(10.0, score)
    
    def _evaluate_business_impact(self, content: str, context: Dict) -> float:
        """Evaluate business impact significance."""
        score = 4.0
        
        # Look for impact quantification
        if re.search(r'\$[\d,]+|\d+%|\d+\s*(million|billion)', content):
            score += 2.0
        
        # Look for impact areas
        impact_areas = [
            'revenue', 'profitability', 'market share', 'efficiency', 'cost reduction',
            'customer satisfaction', 'employee engagement', 'competitive position'
        ]
        impact_count = sum(1 for area in impact_areas if area.lower() in content.lower())
        score += min(2.0, impact_count * 0.4)
        
        # Look for risk considerations
        risk_terms = ['risk', 'threat', 'opportunity', 'challenge', 'mitigation']
        if any(term.lower() in content.lower() for term in risk_terms):
            score += 1.0
        
        return min(10.0, score)
    
    def _evaluate_clarity(self, content: str, context: Dict) -> float:
        """Evaluate clarity and readability."""
        score = 5.0
        
        sentences = content.split('.')
        if not sentences:
            return 2.0
        
        # Check average sentence length (ideal: 15-25 words)
        avg_sentence_length = sum(len(s.split()) for s in sentences if s.strip()) / len([s for s in sentences if s.strip()])
        if 15 <= avg_sentence_length <= 25:
            score += 1.0
        elif avg_sentence_length > 35:
            score -= 1.0
        
        # Check for clear structure
        if re.search(r'\n\s*\n', content):  # Paragraphs
            score += 0.5
        
        # Check for bullet points or numbering
        if re.search(r'[•\-\*]\s|^\d+\.\s', content, re.MULTILINE):
            score += 0.5
        
        # Penalize excessive jargon
        jargon_count = len(re.findall(r'\b[A-Z]{2,}\b', content))  # Acronyms
        if jargon_count > 10:
            score -= 1.0
        
        return min(10.0, score)
    
    def _evaluate_completeness(self, content: str, context: Dict) -> float:
        """Evaluate completeness of analysis."""
        score = 4.0
        
        # Check for key business analysis components
        components = [
            'current state', 'analysis', 'recommendation', 'implementation',
            'timeline', 'resources', 'risks', 'benefits', 'next steps'
        ]
        
        present_components = sum(1 for comp in components 
                               if any(word in content.lower() for word in comp.split()))
        score += min(4.0, present_components * 0.4)
        
        # Check minimum content length
        word_count = len(content.split())
        if word_count < 100:
            score -= 2.0
        elif word_count > 500:
            score += 1.0
        
        return min(10.0, score)
    
    def _evaluate_compliance(self, content: str, context: Dict) -> float:
        """Evaluate compliance considerations."""
        score = 7.0  # Default good score unless issues found
        
        # Check for compliance mentions when industry context provided
        industry = context.get('industry', '').lower()
        
        compliance_terms = ['compliance', 'regulation', 'regulatory', 'legal', 'policy']
        if industry in ['financial', 'healthcare', 'banking'] and not any(term in content.lower() for term in compliance_terms):
            score -= 2.0
        
        # Look for risk disclaimers
        if 'risk' in content.lower() and ('disclaimer' in content.lower() or 'consideration' in content.lower()):
            score += 0.5
        
        return min(10.0, score)
    
    def _generate_recommendations(self, assessment: QualityAssessment, 
                                content: str, context: Dict) -> List[str]:
        """Generate improvement recommendations based on assessment."""
        recommendations = []
        
        for dimension, score in assessment.dimension_scores.items():
            if score < 7.0:
                metric = self.metrics.get(dimension)
                if metric:
                    if dimension == QualityDimension.STRATEGIC_RELEVANCE:
                        recommendations.append("Enhance strategic focus by connecting recommendations to long-term business objectives and competitive positioning.")
                    elif dimension == QualityDimension.EXECUTIVE_APPROPRIATENESS:
                        recommendations.append("Adjust tone for executive audience - focus on business impact rather than technical details.")
                    elif dimension == QualityDimension.ACTIONABILITY:
                        recommendations.append("Add specific action items with clear timelines and responsibility assignments.")
                    elif dimension == QualityDimension.BUSINESS_IMPACT:
                        recommendations.append("Quantify business impact with specific metrics, financial projections, or KPIs.")
                    elif dimension == QualityDimension.CLARITY:
                        recommendations.append("Improve clarity with better structure, shorter sentences, and executive summaries.")
                    elif dimension == QualityDimension.COMPLETENESS:
                        recommendations.append("Ensure comprehensive analysis including risks, benefits, and implementation considerations.")
                    elif dimension == QualityDimension.COMPLIANCE:
                        recommendations.append("Address regulatory and compliance requirements relevant to your industry.")
        
        return recommendations
    
    def get_quality_trends(self, days: int = 30) -> Dict[str, float]:
        """Analyze quality trends over time."""
        cutoff_date = datetime.now().timestamp() - (days * 24 * 3600)
        recent_assessments = [
            a for a in self.assessment_history 
            if a.assessed_at.timestamp() > cutoff_date
        ]
        
        if not recent_assessments:
            return {}
        
        trends = {}
        for dimension in QualityDimension:
            scores = [a.dimension_scores.get(dimension, 0) for a in recent_assessments]
            if scores:
                trends[dimension.value] = {
                    'average': statistics.mean(scores),
                    'trend': 'improving' if len(scores) > 1 and scores[-1] > scores[0] else 'stable'
                }
        
        return trends


# Global quality validator instance
quality_validator = QualityValidator()