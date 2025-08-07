"""
Competitive Landscape Assessor
Simple working implementation for portfolio demonstration
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Tuple
import json
from datetime import datetime
import math


@dataclass
class Competitor:
    """Individual competitor profile."""
    name: str
    market_share: float = 0.0
    revenue: float = 0.0
    growth_rate: float = 0.0
    strength_score: float = 5.0  # 1-10 scale
    threat_level: str = "medium"  # "low", "medium", "high", "critical"
    key_strengths: List[str] = field(default_factory=list)
    key_weaknesses: List[str] = field(default_factory=list)
    strategic_moves: List[str] = field(default_factory=list)


@dataclass
class CompetitivePosition:
    """Our competitive position analysis."""
    market_share: float = 0.0
    relative_strength: float = 5.0
    competitive_advantages: List[str] = field(default_factory=list)
    vulnerabilities: List[str] = field(default_factory=list)
    differentiation_factors: List[str] = field(default_factory=list)


@dataclass
class MarketAnalysis:
    """Overall market analysis results."""
    market_size: float = 0.0
    growth_rate: float = 0.0
    concentration_ratio: float = 0.0  # HHI or CR4
    competitive_intensity: str = "moderate"
    barriers_to_entry: List[str] = field(default_factory=list)
    market_trends: List[str] = field(default_factory=list)


@dataclass
class CompetitiveAssessment:
    """Complete competitive landscape assessment."""
    our_position: CompetitivePosition
    competitors: List[Competitor]
    market_analysis: MarketAnalysis
    strategic_recommendations: List[str] = field(default_factory=list)
    threat_matrix: Dict[str, List[str]] = field(default_factory=dict)
    opportunity_analysis: List[str] = field(default_factory=list)


class CompetitiveLandscapeAssessor:
    """Analyze competitive landscape and strategic positioning."""
    
    def __init__(self):
        self.competitive_factors = [
            "market_share", "brand_strength", "product_quality", "pricing",
            "distribution", "innovation", "financial_resources", "customer_loyalty"
        ]
    
    def calculate_competitive_strength(self, competitor: Competitor,
                                     factor_scores: Dict[str, float] = None) -> float:
        """Calculate overall competitive strength score."""
        if not factor_scores:
            # Use basic scoring if no detailed factors provided
            market_share_score = min(10, competitor.market_share * 20)  # Scale market share
            growth_score = min(10, max(0, competitor.growth_rate * 20 + 5))
            return (market_share_score + growth_score + competitor.strength_score) / 3
        
        # Weighted scoring based on competitive factors
        weights = {
            "market_share": 0.20,
            "brand_strength": 0.15,
            "product_quality": 0.15,
            "pricing": 0.10,
            "distribution": 0.10,
            "innovation": 0.15,
            "financial_resources": 0.10,
            "customer_loyalty": 0.05
        }
        
        weighted_score = sum(factor_scores.get(factor, 5.0) * weight 
                           for factor, weight in weights.items())
        
        return weighted_score
    
    def analyze_market_concentration(self, competitors: List[Competitor]) -> Dict[str, Any]:
        """Analyze market concentration and competitive structure."""
        if not competitors:
            return {'hhi': 0, 'cr4': 0, 'concentration_level': 'unknown'}
        
        # Sort competitors by market share
        sorted_competitors = sorted(competitors, key=lambda x: x.market_share, reverse=True)
        
        # Calculate Herfindahl-Hirschman Index (HHI)
        hhi = sum((comp.market_share * 100) ** 2 for comp in competitors)
        
        # Calculate Concentration Ratio (CR4 - top 4 firms)
        cr4 = sum(comp.market_share for comp in sorted_competitors[:4]) * 100
        
        # Determine concentration level
        if hhi < 1500:
            concentration_level = "low"
            competitive_intensity = "high"
        elif hhi < 2500:
            concentration_level = "moderate"
            competitive_intensity = "moderate"
        else:
            concentration_level = "high"
            competitive_intensity = "low"
        
        return {
            'hhi': hhi,
            'cr4': cr4,
            'concentration_level': concentration_level,
            'competitive_intensity': competitive_intensity,
            'market_leaders': sorted_competitors[:3]
        }
    
    def identify_competitive_threats(self, competitors: List[Competitor],
                                   our_position: CompetitivePosition) -> Dict[str, List[str]]:
        """Identify and categorize competitive threats."""
        threat_matrix = {
            'immediate_threats': [],
            'emerging_threats': [],
            'potential_disruptors': [],
            'market_leaders': []
        }
        
        for competitor in competitors:
            strength = self.calculate_competitive_strength(competitor)
            
            # Immediate threats - strong competitors with aggressive moves
            if (competitor.threat_level in ["high", "critical"] and 
                strength >= 7.0 and competitor.growth_rate > 0.10):
                threat_matrix['immediate_threats'].append(competitor.name)
            
            # Emerging threats - growing competitors
            elif (competitor.growth_rate > 0.20 and strength >= 6.0):
                threat_matrix['emerging_threats'].append(competitor.name)
            
            # Market leaders - high market share
            elif competitor.market_share >= 0.15:
                threat_matrix['market_leaders'].append(competitor.name)
            
            # Potential disruptors - innovative but smaller players
            elif ("innovation" in [s.lower() for s in competitor.key_strengths] and
                  competitor.growth_rate > 0.15):
                threat_matrix['potential_disruptors'].append(competitor.name)
        
        return threat_matrix
    
    def analyze_competitive_gaps(self, our_position: CompetitivePosition,
                               competitors: List[Competitor]) -> List[str]:
        """Identify competitive gaps and improvement opportunities."""
        gaps = []
        
        if not competitors:
            return ["Insufficient competitor data for gap analysis"]
        
        # Market share gap
        max_market_share = max(comp.market_share for comp in competitors)
        if our_position.market_share < max_market_share * 0.7:
            gaps.append(f"Market share gap: Leading competitor has {max_market_share*100:.1f}% vs our {our_position.market_share*100:.1f}%")
        
        # Growth rate comparison
        avg_growth = sum(comp.growth_rate for comp in competitors) / len(competitors)
        if len([comp for comp in competitors if comp.growth_rate > 0.15]) >= 2:
            gaps.append("Multiple competitors showing strong growth - need to accelerate growth initiatives")
        
        # Competitive strength analysis
        competitor_strengths = set()
        for comp in competitors:
            competitor_strengths.update(comp.key_strengths)
        
        our_advantages = set(our_position.competitive_advantages)
        missing_capabilities = competitor_strengths - our_advantages
        
        if missing_capabilities:
            gaps.append(f"Capability gaps identified: {', '.join(list(missing_capabilities)[:3])}")
        
        return gaps
    
    def generate_strategic_recommendations(self, assessment_data: Dict[str, Any]) -> List[str]:
        """Generate strategic recommendations based on competitive analysis."""
        recommendations = []
        
        our_position = assessment_data['our_position']
        competitors = assessment_data['competitors']
        market_analysis = assessment_data['market_analysis']
        threat_matrix = assessment_data['threat_matrix']
        
        # Market position recommendations
        if our_position.market_share < 0.10:
            recommendations.append("Focus on market share growth through targeted customer acquisition and retention strategies")
        elif our_position.market_share > 0.25:
            recommendations.append("Defend market leadership position while exploring adjacent market opportunities")
        
        # Competitive response recommendations
        if threat_matrix['immediate_threats']:
            recommendations.append(f"Develop immediate response strategies for key threats: {', '.join(threat_matrix['immediate_threats'][:2])}")
        
        if threat_matrix['emerging_threats']:
            recommendations.append("Monitor emerging competitors and consider preemptive strategic moves")
        
        # Market structure recommendations
        if market_analysis.competitive_intensity == "high":
            recommendations.append("Focus on differentiation and customer loyalty to reduce price competition")
        elif market_analysis.competitive_intensity == "low":
            recommendations.append("Consider market expansion or new product development to drive growth")
        
        # Innovation and differentiation
        innovation_competitors = [comp for comp in competitors 
                                if "innovation" in [s.lower() for s in comp.key_strengths]]
        if len(innovation_competitors) >= 2:
            recommendations.append("Accelerate innovation initiatives to maintain competitive differentiation")
        
        # Partnership and M&A opportunities
        if len(competitors) > 10 and market_analysis.concentration_ratio < 40:
            recommendations.append("Evaluate consolidation opportunities through strategic acquisitions")
        
        return recommendations
    
    def perform_swot_analysis(self, our_position: CompetitivePosition,
                            competitors: List[Competitor],
                            market_trends: List[str]) -> Dict[str, List[str]]:
        """Perform SWOT analysis based on competitive landscape."""
        swot = {
            'strengths': our_position.competitive_advantages.copy(),
            'weaknesses': our_position.vulnerabilities.copy(),
            'opportunities': [],
            'threats': []
        }
        
        # Identify opportunities from market trends
        growth_trends = [trend for trend in market_trends if any(keyword in trend.lower() 
                        for keyword in ['growth', 'expanding', 'increasing', 'new'])]
        swot['opportunities'].extend(growth_trends[:3])
        
        # Add market-based opportunities
        weak_competitors = [comp for comp in competitors if comp.strength_score < 5.0]
        if weak_competitors:
            swot['opportunities'].append(f"Market share opportunity from weaker competitors: {', '.join([c.name for c in weak_competitors[:2]])}")
        
        # Identify threats from competitors
        strong_competitors = [comp for comp in competitors if comp.strength_score >= 8.0]
        for comp in strong_competitors[:3]:
            swot['threats'].append(f"Strong competitor threat: {comp.name} with key strengths in {', '.join(comp.key_strengths[:2])}")
        
        # Technology and disruption threats
        disruptive_trends = [trend for trend in market_trends if any(keyword in trend.lower() 
                           for keyword in ['disruptive', 'technology', 'digital', 'ai', 'automation'])]
        swot['threats'].extend(disruptive_trends[:2])
        
        return swot
    
    def assess_competitive_landscape(self, our_position: CompetitivePosition,
                                   competitors: List[Competitor],
                                   market_size: float = 1000000000,
                                   market_growth_rate: float = 0.05) -> CompetitiveAssessment:
        """Perform comprehensive competitive landscape assessment."""
        
        # Analyze market concentration
        concentration_analysis = self.analyze_market_concentration(competitors)
        
        # Create market analysis
        market_analysis = MarketAnalysis(
            market_size=market_size,
            growth_rate=market_growth_rate,
            concentration_ratio=concentration_analysis['cr4'],
            competitive_intensity=concentration_analysis['competitive_intensity'],
            barriers_to_entry=[
                "Capital requirements",
                "Brand recognition",
                "Customer relationships",
                "Regulatory compliance",
                "Technology expertise"
            ],
            market_trends=[
                "Digital transformation acceleration",
                "Increased customer expectations",
                "Sustainability focus",
                "Remote work adoption",
                "AI and automation integration"
            ]
        )
        
        # Identify threats
        threat_matrix = self.identify_competitive_threats(competitors, our_position)
        
        # Identify opportunities
        gaps = self.analyze_competitive_gaps(our_position, competitors)
        opportunities = [
            "Market expansion in underserved segments",
            "Product innovation and differentiation",
            "Strategic partnerships and alliances",
            "Digital channel development",
            "Customer experience enhancement"
        ]
        
        # Compile assessment data for recommendations
        assessment_data = {
            'our_position': our_position,
            'competitors': competitors,
            'market_analysis': market_analysis,
            'threat_matrix': threat_matrix
        }
        
        # Generate recommendations
        strategic_recommendations = self.generate_strategic_recommendations(assessment_data)
        
        return CompetitiveAssessment(
            our_position=our_position,
            competitors=competitors,
            market_analysis=market_analysis,
            strategic_recommendations=strategic_recommendations,
            threat_matrix=threat_matrix,
            opportunity_analysis=opportunities
        )
    
    def export_assessment(self, assessment: CompetitiveAssessment, filename: str = None) -> str:
        """Export competitive assessment to JSON."""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"competitive_assessment_{timestamp}.json"
        
        # Convert to serializable format
        export_data = {
            'assessment_date': datetime.now().isoformat(),
            'our_position': {
                'market_share': assessment.our_position.market_share,
                'relative_strength': assessment.our_position.relative_strength,
                'competitive_advantages': assessment.our_position.competitive_advantages,
                'vulnerabilities': assessment.our_position.vulnerabilities,
                'differentiation_factors': assessment.our_position.differentiation_factors
            },
            'competitors': [
                {
                    'name': comp.name,
                    'market_share': comp.market_share,
                    'revenue': comp.revenue,
                    'growth_rate': comp.growth_rate,
                    'strength_score': comp.strength_score,
                    'threat_level': comp.threat_level,
                    'key_strengths': comp.key_strengths,
                    'key_weaknesses': comp.key_weaknesses,
                    'strategic_moves': comp.strategic_moves
                } for comp in assessment.competitors
            ],
            'market_analysis': {
                'market_size': assessment.market_analysis.market_size,
                'growth_rate': assessment.market_analysis.growth_rate,
                'concentration_ratio': assessment.market_analysis.concentration_ratio,
                'competitive_intensity': assessment.market_analysis.competitive_intensity,
                'barriers_to_entry': assessment.market_analysis.barriers_to_entry,
                'market_trends': assessment.market_analysis.market_trends
            },
            'strategic_recommendations': assessment.strategic_recommendations,
            'threat_matrix': assessment.threat_matrix,
            'opportunity_analysis': assessment.opportunity_analysis
        }
        
        with open(filename, 'w') as f:
            json.dump(export_data, f, indent=2)
        
        return filename


def demo_usage():
    """Demonstrate the competitive landscape assessor."""
    print("🏟️ Competitive Landscape Assessor Demo")
    print("=" * 50)
    
    # Initialize assessor
    assessor = CompetitiveLandscapeAssessor()
    
    # Define our position
    our_position = CompetitivePosition(
        market_share=0.12,  # 12% market share
        relative_strength=7.2,
        competitive_advantages=[
            "Superior customer service",
            "Advanced technology platform",
            "Strong brand recognition",
            "Efficient operations"
        ],
        vulnerabilities=[
            "Limited international presence",
            "Higher price point",
            "Smaller R&D budget"
        ],
        differentiation_factors=[
            "Premium quality",
            "Personalized solutions",
            "Industry expertise"
        ]
    )
    
    # Define competitor profiles
    competitors = [
        Competitor(
            name="Market Leader Corp",
            market_share=0.28,
            revenue=450000000,
            growth_rate=0.08,
            strength_score=8.5,
            threat_level="high",
            key_strengths=["Market dominance", "Financial resources", "Global presence"],
            key_weaknesses=["Slow innovation", "Legacy systems"],
            strategic_moves=["Acquired two startups", "Launched new product line"]
        ),
        Competitor(
            name="Innovation Inc",
            market_share=0.08,
            revenue=120000000,
            growth_rate=0.35,
            strength_score=7.8,
            threat_level="critical",
            key_strengths=["Cutting-edge technology", "Rapid innovation", "Strong talent"],
            key_weaknesses=["Limited resources", "Brand recognition"],
            strategic_moves=["Raised $50M Series C", "Patent filing surge"]
        ),
        Competitor(
            name="Value Solutions",
            market_share=0.15,
            revenue=240000000,
            growth_rate=0.12,
            strength_score=6.5,
            threat_level="medium",
            key_strengths=["Cost leadership", "Operational efficiency", "Wide distribution"],
            key_weaknesses=["Low margins", "Commodity positioning"],
            strategic_moves=["Price reduction campaign", "Geographic expansion"]
        ),
        Competitor(
            name="Regional Player",
            market_share=0.06,
            revenue=95000000,
            growth_rate=0.18,
            strength_score=5.8,
            threat_level="medium",
            key_strengths=["Local expertise", "Customer relationships", "Agility"],
            key_weaknesses=["Limited scale", "Technology gaps"],
            strategic_moves=["Strategic partnership", "Digital transformation"]
        ),
        Competitor(
            name="New Entrant",
            market_share=0.02,
            revenue=30000000,
            growth_rate=0.85,
            strength_score=6.2,
            threat_level="high",
            key_strengths=["Disruptive model", "VC backing", "Fresh approach"],
            key_weaknesses=["Unproven scale", "Limited experience"],
            strategic_moves=["Aggressive hiring", "Market penetration pricing"]
        )
    ]
    
    # Perform assessment
    assessment = assessor.assess_competitive_landscape(
        our_position=our_position,
        competitors=competitors,
        market_size=1600000000,  # $1.6B market
        market_growth_rate=0.11   # 11% annual growth
    )
    
    # Display results
    print(f"\n📊 Market Overview")
    print(f"Market Size: ${assessment.market_analysis.market_size:,.0f}")
    print(f"Market Growth Rate: {assessment.market_analysis.growth_rate*100:.1f}%")
    print(f"Concentration Ratio (CR4): {assessment.market_analysis.concentration_ratio:.1f}%")
    print(f"Competitive Intensity: {assessment.market_analysis.competitive_intensity.title()}")
    
    print(f"\n🎯 Our Competitive Position")
    print(f"Market Share: {assessment.our_position.market_share*100:.1f}%")
    print(f"Relative Strength: {assessment.our_position.relative_strength:.1f}/10")
    print(f"Key Advantages: {', '.join(assessment.our_position.competitive_advantages[:3])}")
    
    print(f"\n🏢 Competitor Analysis")
    sorted_competitors = sorted(assessment.competitors, key=lambda x: x.market_share, reverse=True)
    print(f"{'Competitor':<20} {'Share':<8} {'Growth':<8} {'Strength':<10} {'Threat':<10}")
    print("-" * 65)
    
    for comp in sorted_competitors:
        strength_score = assessor.calculate_competitive_strength(comp)
        print(f"{comp.name:<20} {comp.market_share*100:<7.1f}% {comp.growth_rate*100:<7.1f}% {strength_score:<9.1f} {comp.threat_level.title():<10}")
    
    print(f"\n⚠️ Threat Matrix")
    for threat_type, companies in assessment.threat_matrix.items():
        if companies:
            print(f"  {threat_type.replace('_', ' ').title()}: {', '.join(companies)}")
    
    print(f"\n💡 Strategic Recommendations")
    for i, recommendation in enumerate(assessment.strategic_recommendations, 1):
        print(f"  {i}. {recommendation}")
    
    print(f"\n🚀 Key Opportunities")
    for i, opportunity in enumerate(assessment.opportunity_analysis[:5], 1):
        print(f"  {i}. {opportunity}")
    
    # Generate SWOT analysis
    swot = assessor.perform_swot_analysis(
        our_position, competitors, assessment.market_analysis.market_trends
    )
    
    print(f"\n📋 SWOT Analysis Summary")
    print(f"  Strengths: {len(swot['strengths'])} identified")
    print(f"  Weaknesses: {len(swot['weaknesses'])} identified") 
    print(f"  Opportunities: {len(swot['opportunities'])} identified")
    print(f"  Threats: {len(swot['threats'])} identified")
    
    # Export assessment
    filename = assessor.export_assessment(assessment)
    print(f"\n📄 Assessment exported to: {filename}")


if __name__ == "__main__":
    demo_usage()