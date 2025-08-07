"""
Customer Insight Synthesizer
Simple working implementation for portfolio demonstration
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Tuple
import json
from datetime import datetime
from collections import Counter
import statistics


@dataclass
class CustomerSegment:
    """Customer segment profile and characteristics."""
    name: str
    size: int = 0
    revenue_contribution: float = 0.0
    growth_rate: float = 0.0
    satisfaction_score: float = 7.0  # 1-10 scale
    churn_rate: float = 0.05  # 5% annual churn
    avg_lifetime_value: float = 0.0
    key_characteristics: List[str] = field(default_factory=list)
    pain_points: List[str] = field(default_factory=list)
    preferences: List[str] = field(default_factory=list)


@dataclass
class CustomerFeedback:
    """Individual customer feedback data point."""
    segment: str
    channel: str  # "survey", "interview", "review", "support"
    sentiment: str  # "positive", "neutral", "negative"
    category: str  # "product", "service", "pricing", "experience"
    feedback_text: str
    importance_score: float = 5.0  # 1-10 scale
    date: datetime = field(default_factory=datetime.now)


@dataclass
class InsightAnalysis:
    """Customer insight analysis results."""
    segment_analysis: List[CustomerSegment]
    key_insights: List[str] = field(default_factory=list)
    sentiment_analysis: Dict[str, float] = field(default_factory=dict)
    priority_issues: List[str] = field(default_factory=list)
    opportunities: List[str] = field(default_factory=list)
    recommendations: List[str] = field(default_factory=list)
    customer_journey_insights: Dict[str, List[str]] = field(default_factory=dict)


class CustomerInsightSynthesizer:
    """Analyze customer data to generate actionable business insights."""
    
    def __init__(self):
        self.sentiment_keywords = {
            'positive': ['excellent', 'great', 'love', 'amazing', 'perfect', 'outstanding', 'satisfied', 'happy', 'recommend'],
            'negative': ['terrible', 'awful', 'hate', 'worst', 'disappointed', 'frustrated', 'angry', 'poor', 'bad'],
            'neutral': ['okay', 'average', 'decent', 'fine', 'acceptable']
        }
    
    def analyze_sentiment(self, text: str) -> str:
        """Simple sentiment analysis based on keywords."""
        text_lower = text.lower()
        
        positive_count = sum(1 for word in self.sentiment_keywords['positive'] if word in text_lower)
        negative_count = sum(1 for word in self.sentiment_keywords['negative'] if word in text_lower)
        
        if positive_count > negative_count:
            return 'positive'
        elif negative_count > positive_count:
            return 'negative'
        else:
            return 'neutral'
    
    def extract_themes(self, feedback_list: List[CustomerFeedback]) -> Dict[str, int]:
        """Extract common themes from customer feedback."""
        # Common business themes and keywords
        themes = {
            'pricing': ['price', 'cost', 'expensive', 'cheap', 'value', 'pricing', 'affordable'],
            'product_quality': ['quality', 'defect', 'broken', 'durable', 'reliable', 'functionality'],
            'customer_service': ['service', 'support', 'staff', 'representative', 'help', 'response'],
            'user_experience': ['experience', 'interface', 'easy', 'difficult', 'intuitive', 'confusing'],
            'delivery': ['shipping', 'delivery', 'fast', 'slow', 'delayed', 'on-time'],
            'features': ['feature', 'functionality', 'capability', 'missing', 'need', 'want'],
            'performance': ['speed', 'slow', 'fast', 'performance', 'efficiency', 'lag'],
            'communication': ['communication', 'information', 'updates', 'notification', 'inform']
        }
        
        theme_counts = {}
        
        for theme, keywords in themes.items():
            count = 0
            for feedback in feedback_list:
                text_lower = feedback.feedback_text.lower()
                if any(keyword in text_lower for keyword in keywords):
                    count += 1
            theme_counts[theme] = count
        
        return theme_counts
    
    def analyze_segment_performance(self, segments: List[CustomerSegment]) -> Dict[str, Any]:
        """Analyze performance metrics across customer segments."""
        if not segments:
            return {}
        
        total_customers = sum(s.size for s in segments)
        total_revenue = sum(s.revenue_contribution for s in segments)
        
        analysis = {
            'total_customers': total_customers,
            'total_revenue': total_revenue,
            'segment_performance': [],
            'top_performers': [],
            'at_risk_segments': [],
            'growth_opportunities': []
        }
        
        for segment in segments:
            # Calculate key metrics
            revenue_per_customer = segment.revenue_contribution / segment.size if segment.size > 0 else 0
            customer_share = (segment.size / total_customers) * 100 if total_customers > 0 else 0
            revenue_share = (segment.revenue_contribution / total_revenue) * 100 if total_revenue > 0 else 0
            
            segment_metrics = {
                'name': segment.name,
                'customer_share_pct': customer_share,
                'revenue_share_pct': revenue_share,
                'revenue_per_customer': revenue_per_customer,
                'satisfaction_score': segment.satisfaction_score,
                'churn_rate_pct': segment.churn_rate * 100,
                'growth_rate_pct': segment.growth_rate * 100,
                'lifetime_value': segment.avg_lifetime_value
            }
            
            analysis['segment_performance'].append(segment_metrics)
            
            # Categorize segments
            if segment.satisfaction_score >= 8.0 and segment.churn_rate <= 0.05:
                analysis['top_performers'].append(segment.name)
            
            if segment.churn_rate >= 0.15 or segment.satisfaction_score <= 6.0:
                analysis['at_risk_segments'].append(segment.name)
            
            if segment.growth_rate >= 0.20 and segment.satisfaction_score >= 7.0:
                analysis['growth_opportunities'].append(segment.name)
        
        return analysis
    
    def identify_priority_issues(self, feedback_list: List[CustomerFeedback],
                               segments: List[CustomerSegment]) -> List[str]:
        """Identify priority issues based on feedback frequency and segment impact."""
        priority_issues = []
        
        # Analyze feedback themes
        themes = self.extract_themes(feedback_list)
        
        # Get negative feedback themes
        negative_feedback = [f for f in feedback_list if f.sentiment == 'negative']
        negative_themes = self.extract_themes(negative_feedback)
        
        # Priority based on frequency and negative sentiment
        for theme, count in themes.items():
            negative_count = negative_themes.get(theme, 0)
            
            if count >= len(feedback_list) * 0.2:  # Mentioned in 20%+ of feedback
                if negative_count >= count * 0.4:  # 40%+ negative mentions
                    priority_issues.append(f"High negative sentiment around {theme} ({negative_count}/{count} negative)")
                else:
                    priority_issues.append(f"Frequently mentioned {theme} needs attention ({count} mentions)")
        
        # Add segment-specific issues
        for segment in segments:
            if segment.churn_rate >= 0.15:
                priority_issues.append(f"High churn rate in {segment.name} segment ({segment.churn_rate*100:.1f}%)")
            
            if segment.satisfaction_score <= 6.0:
                priority_issues.append(f"Low satisfaction in {segment.name} segment (score: {segment.satisfaction_score:.1f})")
        
        return priority_issues
    
    def identify_opportunities(self, feedback_list: List[CustomerFeedback],
                             segments: List[CustomerSegment]) -> List[str]:
        """Identify growth and improvement opportunities."""
        opportunities = []
        
        # Positive feedback themes indicate strengths to leverage
        positive_feedback = [f for f in feedback_list if f.sentiment == 'positive']
        positive_themes = self.extract_themes(positive_feedback)
        
        top_positive_themes = sorted(positive_themes.items(), key=lambda x: x[1], reverse=True)[:3]
        
        for theme, count in top_positive_themes:
            if count >= len(positive_feedback) * 0.3:
                opportunities.append(f"Leverage strength in {theme} for competitive advantage")
        
        # High-value segment opportunities
        high_value_segments = [s for s in segments if s.avg_lifetime_value > 0 and s.growth_rate > 0.15]
        for segment in high_value_segments:
            opportunities.append(f"Expand in high-growth {segment.name} segment (growth: {segment.growth_rate*100:.1f}%)")
        
        # Feature requests and suggestions
        feature_requests = [f for f in feedback_list if 'need' in f.feedback_text.lower() or 'want' in f.feedback_text.lower()]
        if len(feature_requests) >= len(feedback_list) * 0.15:
            opportunities.append(f"Product enhancement opportunities identified from {len(feature_requests)} customer requests")
        
        # Cross-selling opportunities in high-satisfaction segments
        satisfied_segments = [s for s in segments if s.satisfaction_score >= 8.0]
        for segment in satisfied_segments:
            opportunities.append(f"Cross-selling potential in satisfied {segment.name} segment")
        
        return opportunities
    
    def generate_recommendations(self, analysis_results: Dict[str, Any]) -> List[str]:
        """Generate actionable recommendations based on analysis."""
        recommendations = []
        
        # Address priority issues
        if 'priority_issues' in analysis_results and analysis_results['priority_issues']:
            recommendations.append("Immediate action required: Address top customer pain points to prevent churn")
        
        # Segment-specific recommendations
        segment_perf = analysis_results.get('segment_performance', {})
        
        if segment_perf.get('at_risk_segments'):
            recommendations.append(f"Implement retention programs for at-risk segments: {', '.join(segment_perf['at_risk_segments'][:2])}")
        
        if segment_perf.get('growth_opportunities'):
            recommendations.append(f"Increase investment in high-growth segments: {', '.join(segment_perf['growth_opportunities'][:2])}")
        
        if segment_perf.get('top_performers'):
            recommendations.append(f"Scale successful strategies from top-performing segments: {', '.join(segment_perf['top_performers'][:2])}")
        
        # Sentiment-based recommendations
        sentiment_analysis = analysis_results.get('sentiment_analysis', {})
        negative_pct = sentiment_analysis.get('negative', 0) * 100
        
        if negative_pct > 30:
            recommendations.append("Urgent: Implement comprehensive customer experience improvement program")
        elif negative_pct > 20:
            recommendations.append("Focus on service quality improvements to reduce negative sentiment")
        
        # Opportunity-based recommendations
        opportunities = analysis_results.get('opportunities', [])
        if opportunities:
            recommendations.append("Prioritize top growth opportunities for competitive advantage")
        
        # Data quality recommendations
        feedback_volume = analysis_results.get('total_feedback', 0)
        if feedback_volume < 100:
            recommendations.append("Increase customer feedback collection to improve insight quality")
        
        return recommendations
    
    def synthesize_insights(self, segments: List[CustomerSegment],
                          feedback_list: List[CustomerFeedback]) -> InsightAnalysis:
        """Perform comprehensive customer insight analysis."""
        
        # Analyze segment performance
        segment_performance = self.analyze_segment_performance(segments)
        
        # Calculate overall sentiment distribution
        sentiment_counts = Counter(f.sentiment for f in feedback_list)
        total_feedback = len(feedback_list)
        
        sentiment_analysis = {}
        if total_feedback > 0:
            sentiment_analysis = {
                'positive': sentiment_counts.get('positive', 0) / total_feedback,
                'neutral': sentiment_counts.get('neutral', 0) / total_feedback,
                'negative': sentiment_counts.get('negative', 0) / total_feedback
            }
        
        # Identify themes and issues
        themes = self.extract_themes(feedback_list)
        priority_issues = self.identify_priority_issues(feedback_list, segments)
        opportunities = self.identify_opportunities(feedback_list, segments)
        
        # Generate key insights
        key_insights = []
        
        if segments:
            top_segment = max(segments, key=lambda s: s.revenue_contribution)
            key_insights.append(f"Top revenue segment: {top_segment.name} contributes ${top_segment.revenue_contribution:,.0f}")
            
            if segment_performance.get('at_risk_segments'):
                key_insights.append(f"At-risk segments identified: {len(segment_performance['at_risk_segments'])} segments need immediate attention")
        
        if sentiment_analysis:
            key_insights.append(f"Customer sentiment: {sentiment_analysis.get('positive', 0)*100:.1f}% positive, {sentiment_analysis.get('negative', 0)*100:.1f}% negative")
        
        if themes:
            top_theme = max(themes, key=themes.get)
            key_insights.append(f"Most discussed topic: {top_theme} mentioned in {themes[top_theme]} feedback items")
        
        # Compile results
        analysis_results = {
            'segment_performance': segment_performance,
            'sentiment_analysis': sentiment_analysis,
            'priority_issues': priority_issues,
            'opportunities': opportunities,
            'total_feedback': total_feedback
        }
        
        recommendations = self.generate_recommendations(analysis_results)
        
        # Customer journey insights (simplified)
        journey_insights = {
            'awareness': ['Brand recognition needs improvement', 'Digital marketing effectiveness varies by segment'],
            'consideration': ['Product comparison tools requested', 'Pricing transparency important'],
            'purchase': ['Checkout process optimization needed', 'Payment options expansion requested'],
            'onboarding': ['Simplified setup process desired', 'Training materials effectiveness varies'],
            'engagement': ['Regular communication preferred', 'Self-service options important'],
            'support': ['Response time critical', 'Multi-channel support expected'],
            'renewal': ['Value demonstration crucial', 'Loyalty programs effective']
        }
        
        return InsightAnalysis(
            segment_analysis=segments,
            key_insights=key_insights,
            sentiment_analysis=sentiment_analysis,
            priority_issues=priority_issues,
            opportunities=opportunities,
            recommendations=recommendations,
            customer_journey_insights=journey_insights
        )
    
    def export_analysis(self, analysis: InsightAnalysis, filename: str = None) -> str:
        """Export customer insight analysis to JSON."""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"customer_insights_{timestamp}.json"
        
        # Convert to serializable format
        export_data = {
            'analysis_date': datetime.now().isoformat(),
            'segments': [
                {
                    'name': seg.name,
                    'size': seg.size,
                    'revenue_contribution': seg.revenue_contribution,
                    'growth_rate': seg.growth_rate,
                    'satisfaction_score': seg.satisfaction_score,
                    'churn_rate': seg.churn_rate,
                    'avg_lifetime_value': seg.avg_lifetime_value,
                    'key_characteristics': seg.key_characteristics,
                    'pain_points': seg.pain_points,
                    'preferences': seg.preferences
                } for seg in analysis.segment_analysis
            ],
            'key_insights': analysis.key_insights,
            'sentiment_analysis': analysis.sentiment_analysis,
            'priority_issues': analysis.priority_issues,
            'opportunities': analysis.opportunities,
            'recommendations': analysis.recommendations,
            'customer_journey_insights': analysis.customer_journey_insights
        }
        
        with open(filename, 'w') as f:
            json.dump(export_data, f, indent=2)
        
        return filename


def demo_usage():
    """Demonstrate the customer insight synthesizer."""
    print("👥 Customer Insight Synthesizer Demo")
    print("=" * 50)
    
    # Initialize synthesizer
    synthesizer = CustomerInsightSynthesizer()
    
    # Define customer segments
    segments = [
        CustomerSegment(
            name="Enterprise Clients",
            size=145,
            revenue_contribution=2800000,
            growth_rate=0.12,
            satisfaction_score=8.2,
            churn_rate=0.08,
            avg_lifetime_value=85000,
            key_characteristics=["Large organizations", "Complex needs", "Budget authority"],
            pain_points=["Long implementation times", "Integration complexity"],
            preferences=["Dedicated support", "Custom solutions", "Proven ROI"]
        ),
        CustomerSegment(
            name="Mid-Market",
            size=320,
            revenue_contribution=1950000,
            growth_rate=0.18,
            satisfaction_score=7.6,
            churn_rate=0.12,
            avg_lifetime_value=35000,
            key_characteristics=["Growing businesses", "Efficiency focused", "Technology adopters"],
            pain_points=["Limited IT resources", "Cost sensitivity"],
            preferences=["Easy setup", "Scalable solutions", "Good value"]
        ),
        CustomerSegment(
            name="Small Business",
            size=1250,
            revenue_contribution=1200000,
            growth_rate=0.25,
            satisfaction_score=7.1,
            churn_rate=0.18,
            avg_lifetime_value=12000,
            key_characteristics=["Resource constrained", "Simple needs", "Price sensitive"],
            pain_points=["Learning curve", "Support availability"],
            preferences=["Self-service", "Affordable pricing", "Quick results"]
        ),
        CustomerSegment(
            name="Startups",
            size=890,
            revenue_contribution=450000,
            growth_rate=0.42,
            satisfaction_score=6.8,
            churn_rate=0.25,
            avg_lifetime_value=8500,
            key_characteristics=["Innovation focused", "Rapid growth", "Limited budget"],
            pain_points=["Changing requirements", "Cash flow concerns"],
            preferences=["Flexible terms", "Growth potential", "Modern features"]
        )
    ]
    
    # Sample customer feedback
    feedback_data = [
        CustomerFeedback("Enterprise Clients", "survey", "positive", "service", "Excellent customer support and dedicated account management", 9.0),
        CustomerFeedback("Enterprise Clients", "interview", "negative", "product", "Integration with our ERP system was very complex and time-consuming", 8.5),
        CustomerFeedback("Mid-Market", "review", "positive", "product", "Great features and easy to use interface, good value for money", 7.0),
        CustomerFeedback("Mid-Market", "survey", "neutral", "pricing", "Pricing is reasonable but would like more flexibility in packages", 6.0),
        CustomerFeedback("Small Business", "support", "negative", "service", "Response time is too slow, need faster support for critical issues", 8.0),
        CustomerFeedback("Small Business", "review", "positive", "experience", "Simple setup process, was up and running quickly", 6.5),
        CustomerFeedback("Startups", "survey", "negative", "pricing", "Too expensive for a startup, need more affordable options", 7.5),
        CustomerFeedback("Startups", "interview", "positive", "product", "Love the modern interface and innovative features", 6.0),
        CustomerFeedback("Enterprise Clients", "survey", "neutral", "product", "Product functionality is good but missing some advanced features we need", 7.0),
        CustomerFeedback("Mid-Market", "support", "positive", "service", "Support team was very helpful in resolving our technical issue", 6.5),
        CustomerFeedback("Small Business", "review", "negative", "experience", "Learning curve was steeper than expected, need better onboarding", 7.0),
        CustomerFeedback("Startups", "survey", "positive", "product", "Excellent product that scales with our growing business needs", 8.0)
    ]
    
    # Auto-detect sentiment for demo
    for feedback in feedback_data:
        detected_sentiment = synthesizer.analyze_sentiment(feedback.feedback_text)
        # Use detected sentiment if not specified
        if not hasattr(feedback, 'sentiment') or not feedback.sentiment:
            feedback.sentiment = detected_sentiment
    
    # Perform analysis
    analysis = synthesizer.synthesize_insights(segments, feedback_data)
    
    # Display results
    print(f"\n📊 Customer Segment Analysis")
    print(f"Total Segments: {len(analysis.segment_analysis)}")
    
    total_customers = sum(s.size for s in segments)
    total_revenue = sum(s.revenue_contribution for s in segments)
    print(f"Total Customers: {total_customers:,}")
    print(f"Total Revenue: ${total_revenue:,.0f}")
    
    print(f"\n🎯 Segment Performance:")
    print(f"{'Segment':<15} {'Customers':<10} {'Revenue':<12} {'Satisfaction':<12} {'Churn':<8} {'Growth':<8}")
    print("-" * 75)
    
    for segment in segments:
        print(f"{segment.name:<15} {segment.size:<10,} ${segment.revenue_contribution:<11,.0f} {segment.satisfaction_score:<11.1f} {segment.churn_rate*100:<7.1f}% {segment.growth_rate*100:<7.1f}%")
    
    # Sentiment Analysis
    print(f"\n😊 Customer Sentiment Analysis")
    for sentiment, percentage in analysis.sentiment_analysis.items():
        print(f"  {sentiment.title()}: {percentage*100:.1f}%")
    
    # Key Insights
    print(f"\n💡 Key Insights")
    for i, insight in enumerate(analysis.key_insights, 1):
        print(f"  {i}. {insight}")
    
    # Priority Issues
    if analysis.priority_issues:
        print(f"\n⚠️ Priority Issues")
        for i, issue in enumerate(analysis.priority_issues, 1):
            print(f"  {i}. {issue}")
    
    # Opportunities
    if analysis.opportunities:
        print(f"\n🚀 Growth Opportunities")
        for i, opportunity in enumerate(analysis.opportunities[:5], 1):
            print(f"  {i}. {opportunity}")
    
    # Recommendations
    print(f"\n📋 Strategic Recommendations")
    for i, recommendation in enumerate(analysis.recommendations, 1):
        print(f"  {i}. {recommendation}")
    
    # Theme Analysis
    themes = synthesizer.extract_themes(feedback_data)
    print(f"\n📈 Top Feedback Themes")
    top_themes = sorted(themes.items(), key=lambda x: x[1], reverse=True)[:5]
    for theme, count in top_themes:
        print(f"  {theme.replace('_', ' ').title()}: {count} mentions")
    
    # Export analysis
    filename = synthesizer.export_analysis(analysis)
    print(f"\n📄 Analysis exported to: {filename}")


if __name__ == "__main__":
    demo_usage()