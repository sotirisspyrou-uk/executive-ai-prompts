"""
Executive AI Prompts - Usage Analytics System

This module provides comprehensive analytics and tracking for prompt performance,
usage patterns, and optimization insights for executive AI prompts.
"""

from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from collections import defaultdict
import statistics
import json

from prompt_manager import PromptExecution, IndustryType, ExecutiveRole, PromptCategory


@dataclass
class UsageMetrics:
    """Aggregated usage metrics for analytics."""
    total_executions: int = 0
    unique_users: int = 0
    average_quality_score: float = 0.0
    success_rate: float = 0.0
    average_response_time: float = 0.0
    peak_usage_hour: int = 0
    most_popular_category: str = ""
    top_industries: List[Tuple[str, int]] = field(default_factory=list)
    top_roles: List[Tuple[str, int]] = field(default_factory=list)


@dataclass 
class PerformanceInsight:
    """Insight from performance analysis."""
    category: str
    insight_type: str  # "optimization", "trend", "issue", "opportunity"
    description: str
    impact_level: str  # "low", "medium", "high", "critical"
    recommendation: str
    data_points: Dict[str, Any] = field(default_factory=dict)


class UsageAnalytics:
    """Comprehensive analytics system for executive AI prompt usage."""
    
    def __init__(self):
        self.execution_history: List[PromptExecution] = []
        self.user_sessions: Dict[str, List[datetime]] = defaultdict(list)
        self.performance_benchmarks: Dict[str, float] = {
            'min_quality_score': 7.0,
            'max_response_time': 5.0,  # seconds
            'target_success_rate': 0.85
        }
    
    def record_execution(self, execution: PromptExecution, user_id: Optional[str] = None) -> None:
        """Record a prompt execution for analytics."""
        self.execution_history.append(execution)
        
        if user_id:
            self.user_sessions[user_id].append(execution.execution_time)
    
    def get_usage_summary(self, start_date: Optional[datetime] = None,
                         end_date: Optional[datetime] = None) -> UsageMetrics:
        """Generate comprehensive usage summary."""
        filtered_executions = self._filter_executions_by_date(start_date, end_date)
        
        if not filtered_executions:
            return UsageMetrics()
        
        # Calculate basic metrics
        total_executions = len(filtered_executions)
        quality_scores = [e.quality_score for e in filtered_executions if e.quality_score is not None]
        avg_quality = statistics.mean(quality_scores) if quality_scores else 0.0
        
        # Calculate success rate (quality score >= threshold)
        successful_executions = [e for e in filtered_executions 
                               if e.quality_score and e.quality_score >= self.performance_benchmarks['min_quality_score']]
        success_rate = len(successful_executions) / total_executions if total_executions > 0 else 0.0
        
        # Analyze usage patterns
        peak_hour = self._get_peak_usage_hour(filtered_executions)
        popular_category = self._get_most_popular_category(filtered_executions)
        top_industries = self._get_top_industries(filtered_executions)
        top_roles = self._get_top_roles(filtered_executions)
        
        return UsageMetrics(
            total_executions=total_executions,
            average_quality_score=avg_quality,
            success_rate=success_rate,
            peak_usage_hour=peak_hour,
            most_popular_category=popular_category,
            top_industries=top_industries,
            top_roles=top_roles
        )
    
    def get_category_performance(self, category: Optional[PromptCategory] = None,
                               days: int = 30) -> Dict[str, Any]:
        """Analyze performance by prompt category."""
        start_date = datetime.now() - timedelta(days=days)
        filtered_executions = self._filter_executions_by_date(start_date)
        
        if category:
            # Filter by specific category (would need template lookup)
            filtered_executions = [e for e in filtered_executions if self._get_execution_category(e) == category]
        
        performance = defaultdict(list)
        
        for execution in filtered_executions:
            exec_category = self._get_execution_category(execution)
            if exec_category and execution.quality_score is not None:
                performance[exec_category.value].append(execution.quality_score)
        
        # Calculate category statistics
        category_stats = {}
        for cat, scores in performance.items():
            if scores:
                category_stats[cat] = {
                    'count': len(scores),
                    'average_score': statistics.mean(scores),
                    'min_score': min(scores),
                    'max_score': max(scores),
                    'std_dev': statistics.stdev(scores) if len(scores) > 1 else 0.0
                }
        
        return category_stats
    
    def get_industry_insights(self, industry: Optional[IndustryType] = None) -> Dict[str, Any]:
        """Generate insights for specific industry or all industries."""
        if industry:
            executions = [e for e in self.execution_history 
                         if e.context and e.context.industry == industry]
        else:
            executions = self.execution_history
        
        if not executions:
            return {}
        
        # Analyze industry-specific patterns
        industry_patterns = defaultdict(lambda: {'executions': 0, 'quality_scores': []})
        
        for execution in executions:
            if execution.context:
                ind = execution.context.industry.value
                industry_patterns[ind]['executions'] += 1
                if execution.quality_score is not None:
                    industry_patterns[ind]['quality_scores'].append(execution.quality_score)
        
        # Calculate industry statistics
        insights = {}
        for ind, data in industry_patterns.items():
            scores = data['quality_scores']
            insights[ind] = {
                'total_executions': data['executions'],
                'average_quality': statistics.mean(scores) if scores else 0.0,
                'performance_rating': self._rate_performance(statistics.mean(scores) if scores else 0.0)
            }
        
        return insights
    
    def get_role_effectiveness(self) -> Dict[str, Dict[str, float]]:
        """Analyze prompt effectiveness by executive role."""
        role_performance = defaultdict(lambda: {'scores': [], 'executions': 0})
        
        for execution in self.execution_history:
            if execution.context and execution.context.role:
                role = execution.context.role.value
                role_performance[role]['executions'] += 1
                if execution.quality_score is not None:
                    role_performance[role]['scores'].append(execution.quality_score)
        
        effectiveness = {}
        for role, data in role_performance.items():
            scores = data['scores']
            effectiveness[role] = {
                'total_executions': data['executions'],
                'average_quality': statistics.mean(scores) if scores else 0.0,
                'consistency': 1.0 - (statistics.stdev(scores) / 10.0) if len(scores) > 1 else 1.0,
                'effectiveness_rating': self._rate_effectiveness(
                    statistics.mean(scores) if scores else 0.0,
                    1.0 - (statistics.stdev(scores) / 10.0) if len(scores) > 1 else 1.0
                )
            }
        
        return effectiveness
    
    def generate_performance_insights(self, min_executions: int = 10) -> List[PerformanceInsight]:
        """Generate actionable performance insights."""
        insights = []
        
        # Quality score trends
        recent_scores = [e.quality_score for e in self.execution_history[-50:] 
                        if e.quality_score is not None]
        
        if len(recent_scores) >= min_executions:
            avg_recent = statistics.mean(recent_scores)
            if avg_recent < self.performance_benchmarks['min_quality_score']:
                insights.append(PerformanceInsight(
                    category="quality",
                    insight_type="issue",
                    description=f"Average quality score ({avg_recent:.1f}) below target ({self.performance_benchmarks['min_quality_score']})",
                    impact_level="high",
                    recommendation="Review and optimize underperforming prompt templates",
                    data_points={'current_avg': avg_recent, 'target': self.performance_benchmarks['min_quality_score']}
                ))
        
        # Usage pattern analysis
        usage_by_hour = defaultdict(int)
        for execution in self.execution_history[-100:]:  # Last 100 executions
            hour = execution.execution_time.hour
            usage_by_hour[hour] += 1
        
        if usage_by_hour:
            peak_hour = max(usage_by_hour, key=usage_by_hour.get)
            peak_usage = usage_by_hour[peak_hour]
            total_usage = sum(usage_by_hour.values())
            
            if peak_usage / total_usage > 0.3:  # More than 30% usage in single hour
                insights.append(PerformanceInsight(
                    category="usage_patterns",
                    insight_type="optimization",
                    description=f"High usage concentration at hour {peak_hour} ({peak_usage/total_usage*100:.1f}%)",
                    impact_level="medium",
                    recommendation="Consider load balancing or capacity planning for peak hours",
                    data_points={'peak_hour': peak_hour, 'concentration': peak_usage/total_usage}
                ))
        
        # Category performance analysis
        category_performance = self.get_category_performance()
        for category, stats in category_performance.items():
            if stats['count'] >= min_executions and stats['average_score'] < 6.0:
                insights.append(PerformanceInsight(
                    category="category_performance",
                    insight_type="issue",
                    description=f"Low performance in {category} category (avg: {stats['average_score']:.1f})",
                    impact_level="medium",
                    recommendation=f"Review and enhance {category} prompt templates",
                    data_points=stats
                ))
        
        return insights
    
    def export_analytics_report(self, start_date: Optional[datetime] = None,
                              end_date: Optional[datetime] = None) -> Dict[str, Any]:
        """Export comprehensive analytics report."""
        summary = self.get_usage_summary(start_date, end_date)
        category_perf = self.get_category_performance()
        industry_insights = self.get_industry_insights()
        role_effectiveness = self.get_role_effectiveness()
        performance_insights = self.generate_performance_insights()
        
        report = {
            'report_metadata': {
                'generated_at': datetime.now().isoformat(),
                'period_start': start_date.isoformat() if start_date else None,
                'period_end': end_date.isoformat() if end_date else None,
                'total_executions_analyzed': len(self.execution_history)
            },
            'usage_summary': {
                'total_executions': summary.total_executions,
                'average_quality_score': summary.average_quality_score,
                'success_rate': summary.success_rate,
                'peak_usage_hour': summary.peak_usage_hour,
                'most_popular_category': summary.most_popular_category,
                'top_industries': summary.top_industries,
                'top_roles': summary.top_roles
            },
            'category_performance': category_perf,
            'industry_insights': industry_insights,
            'role_effectiveness': role_effectiveness,
            'performance_insights': [
                {
                    'category': insight.category,
                    'type': insight.insight_type,
                    'description': insight.description,
                    'impact': insight.impact_level,
                    'recommendation': insight.recommendation,
                    'data': insight.data_points
                } for insight in performance_insights
            ],
            'recommendations': self._generate_optimization_recommendations(performance_insights)
        }
        
        return report
    
    def _filter_executions_by_date(self, start_date: Optional[datetime] = None,
                                  end_date: Optional[datetime] = None) -> List[PromptExecution]:
        """Filter executions by date range."""
        filtered = self.execution_history
        
        if start_date:
            filtered = [e for e in filtered if e.execution_time >= start_date]
        
        if end_date:
            filtered = [e for e in filtered if e.execution_time <= end_date]
        
        return filtered
    
    def _get_peak_usage_hour(self, executions: List[PromptExecution]) -> int:
        """Determine peak usage hour."""
        hourly_usage = defaultdict(int)
        for execution in executions:
            hourly_usage[execution.execution_time.hour] += 1
        
        return max(hourly_usage, key=hourly_usage.get) if hourly_usage else 0
    
    def _get_most_popular_category(self, executions: List[PromptExecution]) -> str:
        """Determine most popular prompt category."""
        category_usage = defaultdict(int)
        for execution in executions:
            category = self._get_execution_category(execution)
            if category:
                category_usage[category.value] += 1
        
        return max(category_usage, key=category_usage.get) if category_usage else ""
    
    def _get_top_industries(self, executions: List[PromptExecution]) -> List[Tuple[str, int]]:
        """Get top industries by usage."""
        industry_usage = defaultdict(int)
        for execution in executions:
            if execution.context and execution.context.industry:
                industry_usage[execution.context.industry.value] += 1
        
        return sorted(industry_usage.items(), key=lambda x: x[1], reverse=True)[:5]
    
    def _get_top_roles(self, executions: List[PromptExecution]) -> List[Tuple[str, int]]:
        """Get top roles by usage."""
        role_usage = defaultdict(int)
        for execution in executions:
            if execution.context and execution.context.role:
                role_usage[execution.context.role.value] += 1
        
        return sorted(role_usage.items(), key=lambda x: x[1], reverse=True)[:5]
    
    def _get_execution_category(self, execution: PromptExecution) -> Optional[PromptCategory]:
        """Determine category of execution (would need template lookup in real implementation)."""
        # This would typically look up the template and return its category
        # For now, we'll infer from prompt content or return None
        return None
    
    def _rate_performance(self, score: float) -> str:
        """Rate performance based on quality score."""
        if score >= 8.0:
            return "excellent"
        elif score >= 7.0:
            return "good"
        elif score >= 6.0:
            return "fair"
        else:
            return "poor"
    
    def _rate_effectiveness(self, avg_quality: float, consistency: float) -> str:
        """Rate overall effectiveness combining quality and consistency."""
        effectiveness_score = (avg_quality * 0.7) + (consistency * 10 * 0.3)
        
        if effectiveness_score >= 8.0:
            return "highly_effective"
        elif effectiveness_score >= 7.0:
            return "effective"
        elif effectiveness_score >= 6.0:
            return "moderately_effective"
        else:
            return "needs_improvement"
    
    def _generate_optimization_recommendations(self, insights: List[PerformanceInsight]) -> List[str]:
        """Generate high-level optimization recommendations."""
        recommendations = []
        
        # Categorize insights
        quality_issues = [i for i in insights if i.category == "quality"]
        usage_issues = [i for i in insights if i.category == "usage_patterns"]
        category_issues = [i for i in insights if i.category == "category_performance"]
        
        if quality_issues:
            recommendations.append("Implement systematic quality improvement program for underperforming prompts")
        
        if usage_issues:
            recommendations.append("Optimize system capacity and load distribution based on usage patterns")
        
        if category_issues:
            recommendations.append("Focus on category-specific template enhancements and training")
        
        if len(insights) > 5:
            recommendations.append("Conduct comprehensive prompt library audit and optimization")
        
        return recommendations


# Global usage analytics instance
usage_analytics = UsageAnalytics()