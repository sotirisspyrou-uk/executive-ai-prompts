"""
Executive AI Prompts - Performance Benchmark Analyzer

Industry benchmarking, performance gap analysis, and competitive
financial performance evaluation for executive decision-making.
"""

from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field
from enum import Enum
from prompt_manager import PromptTemplate, PromptCategory, prompt_manager
from context_adapter import context_adapter


class BenchmarkType(Enum):
    FINANCIAL = "financial_performance"
    OPERATIONAL = "operational_efficiency"
    STRATEGIC = "strategic_positioning"
    ESG = "esg_sustainability"
    DIGITAL = "digital_maturity"


class BenchmarkScope(Enum):
    INDUSTRY = "industry_peers"
    SIZE = "size_cohort"
    GEOGRAPHIC = "geographic_region"
    BEST_IN_CLASS = "best_in_class"
    HISTORICAL = "historical_performance"


@dataclass
class BenchmarkConfig:
    """Configuration for performance benchmarking analysis."""
    benchmark_types: List[BenchmarkType] = field(default_factory=lambda: [BenchmarkType.FINANCIAL])
    benchmark_scope: BenchmarkScope = BenchmarkScope.INDUSTRY
    peer_companies: List[str] = field(default_factory=list)
    time_period: str = "3 years"
    performance_metrics: List[str] = field(default_factory=list)
    gap_analysis: bool = True
    improvement_planning: bool = True
    investor_communication: bool = False


class PerformanceBenchmarkAnalyzer:
    """Advanced performance benchmarking and gap analysis generator."""
    
    def __init__(self):
        self.templates = {}
        self._initialize_templates()
    
    def _initialize_templates(self) -> None:
        """Initialize performance benchmarking templates."""
        
        # Comprehensive Benchmark Analysis
        self.templates['comprehensive_benchmark_analysis'] = PromptTemplate(
            name="Comprehensive Performance Benchmark Analysis",
            category=PromptCategory.FINANCIAL_ANALYSIS,
            base_prompt="""
As {role} conducting performance benchmarking analysis against {benchmark_scope} over a {time_period} period, evaluate our competitive position and identify performance improvement opportunities.

**PERFORMANCE BENCHMARKING FRAMEWORK:**

1. **FINANCIAL PERFORMANCE BENCHMARKING**
   
   **Profitability Metrics:**
   - Revenue growth rate vs. industry average
   - EBITDA margin vs. peer median
   - Net profit margin comparison
   - Return on Assets (ROA) percentile ranking
   - Return on Equity (ROE) peer positioning
   - Return on Invested Capital (ROIC) analysis
   
   **Efficiency Metrics:**
   - Asset turnover vs. industry benchmarks
   - Working capital efficiency comparison
   - Cash conversion cycle analysis
   - Operating leverage vs. peers
   - Cost structure benchmarking
   - Productivity metrics comparison
   
   **Financial Strength Metrics:**
   - Debt-to-equity ratio comparison
   - Interest coverage ratio benchmarking
   - Current and quick ratio analysis
   - Credit rating relative position
   - Cash flow strength vs. peers
   - Financial flexibility assessment

2. **OPERATIONAL PERFORMANCE BENCHMARKING**
   
   **Customer Metrics:**
   - Customer acquisition cost (CAC) comparison
   - Customer lifetime value (CLV) benchmarking
   - Customer retention rate analysis
   - Net Promoter Score (NPS) vs. industry
   - Customer satisfaction benchmarking
   - Market share position analysis
   
   **Operational Efficiency:**
   - Revenue per employee comparison
   - Operating expense ratios benchmarking
   - Technology spending as % of revenue
   - R&D investment vs. industry average
   - Capital intensity comparison
   - Quality and service metrics

3. **STRATEGIC POSITIONING BENCHMARKING**
   
   **Market Position:**
   - Market share and growth comparison
   - Brand strength and recognition metrics
   - Competitive advantage sustainability
   - Innovation index and patent portfolio
   - Geographic diversification analysis
   - Product portfolio breadth vs. peers
   
   **Investment and Growth:**
   - Capital allocation effectiveness
   - M&A activity and success rates
   - Digital transformation progress
   - ESG and sustainability metrics
   - Talent acquisition and retention
   - Strategic partnership development

4. **PERFORMANCE GAP ANALYSIS**
   
   **Gap Identification:**
   - Performance gaps vs. top quartile performers
   - Underperforming metric prioritization
   - Root cause analysis of performance gaps
   - Capability and resource gap assessment
   - Best practice identification and analysis
   
   **Gap Quantification:**
   - Financial impact of closing performance gaps
   - Value creation potential from improvement
   - Investment required to close gaps
   - Timeline for performance improvement
   - Risk assessment of improvement initiatives

5. **IMPROVEMENT ACTION PLANNING**
   
   **Priority Initiative Development:**
   - High-impact improvement opportunities
   - Quick wins vs. long-term initiatives
   - Resource allocation and investment requirements
   - Success metrics and performance targets
   - Implementation timeline and milestones
   
   **Performance Monitoring Framework:**
   - KPI dashboard and tracking system
   - Benchmarking refresh schedule
   - Performance review and adjustment process
   - Stakeholder reporting and communication
   - Continuous improvement integration

**STRATEGIC RECOMMENDATIONS:**
- Priority performance improvement areas
- Investment and resource allocation guidance
- Competitive positioning enhancement strategies
- Performance monitoring and governance framework
- Stakeholder communication and transparency plan

{industry_context}
{role_focus}
{regulatory_considerations}

Provide actionable insights that drive measurable performance improvement and competitive advantage.

{communication_guidance}
""",
            variables={
                "benchmark_scope": "industry peers",
                "time_period": "3 years"
            },
            context_adaptations={
                "financial_services": "Include regulatory capital efficiency, cost-to-income ratios, and credit quality metrics. Address Basel III compliance and stress testing results.",
                "technology": "Focus on innovation metrics, platform scalability, developer productivity, and cybersecurity investments. Include digital transformation benchmarks.",
                "healthcare": "Include patient outcomes, clinical quality metrics, and value-based care performance. Address regulatory compliance and safety standards.",
                "cfo": "Emphasize financial ratio analysis, capital efficiency, and investor communication implications. Focus on margin improvement and cost optimization.",
                "ceo": "Frame for board presentation with strategic positioning and competitive advantage implications. Include stakeholder value creation focus."
            },
            quality_criteria=[
                "Comprehensive multi-dimensional benchmarking analysis",
                "Quantitative performance gap identification and prioritization",
                "Actionable improvement recommendations with business cases",
                "Implementation roadmap with success metrics",
                "Stakeholder communication and transparency framework"
            ],
            tags=["benchmarking", "performance_analysis", "competitive_analysis", "improvement_planning"]
        )
        
        # Industry Benchmark Analysis
        self.templates['industry_benchmark_analysis'] = PromptTemplate(
            name="Industry Benchmark and Competitive Positioning",
            category=PromptCategory.FINANCIAL_ANALYSIS,
            base_prompt="""
Conduct comprehensive industry benchmarking analysis positioning our {company_size} {industry} organization against industry leaders and peer companies.

**INDUSTRY BENCHMARKING FRAMEWORK:**

1. **INDUSTRY LANDSCAPE ANALYSIS**
   - Industry structure and competitive dynamics
   - Market leaders and their competitive advantages
   - Industry growth trends and future outlook
   - Technology disruption and innovation trends
   - Regulatory environment and compliance requirements

2. **PEER GROUP IDENTIFICATION AND ANALYSIS**
   
   **Primary Peer Group (Direct Competitors):**
   - Similar business model and market focus
   - Comparable size and scale operations
   - Geographic overlap and market presence
   - Product/service portfolio similarity
   - Customer segment alignment
   
   **Aspirational Peer Group (Industry Leaders):**
   - Market leadership position
   - Superior financial performance
   - Best-in-class operational metrics
   - Innovation and transformation leaders
   - Strong brand and market recognition

3. **COMPREHENSIVE PERFORMANCE COMPARISON**
   
   **Financial Performance Quartiles:**
   - Revenue growth (1st, 2nd, 3rd, 4th quartile positioning)
   - Profitability margins (EBITDA, net margin benchmarking)
   - Return metrics (ROA, ROE, ROIC peer comparison)
   - Cash flow generation and quality analysis
   - Balance sheet strength and financial flexibility
   
   **Operational Excellence Metrics:**
   - Productivity and efficiency benchmarks
   - Customer satisfaction and loyalty metrics
   - Quality and service delivery standards
   - Innovation and R&D investment levels
   - Digital transformation and technology adoption

4. **COMPETITIVE ADVANTAGE ASSESSMENT**
   
   **Strengths Identification:**
   - Areas of superior performance vs. peers
   - Sustainable competitive advantages
   - Unique capabilities and resources
   - Market position and brand strength
   - Financial and operational excellence areas
   
   **Improvement Opportunities:**
   - Performance gaps vs. industry leaders
   - Underperforming metrics and root causes
   - Capability gaps and development needs
   - Strategic positioning weaknesses
   - Operational efficiency opportunities

5. **STRATEGIC POSITIONING RECOMMENDATIONS**
   - Competitive differentiation strategies
   - Performance improvement priorities
   - Investment allocation for competitive advantage
   - Market positioning and brand enhancement
   - Partnership and ecosystem development

**INVESTOR AND STAKEHOLDER COMMUNICATION:**
- Performance narrative and competitive positioning
- Industry context and market dynamics explanation
- Improvement initiative communication
- Long-term value creation strategy
- Transparency and disclosure framework

{industry_context}
{role_focus}
{regulatory_considerations}

Focus on actionable insights that enhance competitive positioning and drive superior performance.
""",
            variables={
                "company_size": "",
                "industry": ""
            },
            quality_criteria=[
                "Comprehensive industry and peer analysis",
                "Quantitative performance positioning with quartile rankings",
                "Clear competitive advantage and opportunity identification",
                "Strategic positioning recommendations",
                "Stakeholder communication framework"
            ],
            tags=["industry_analysis", "peer_benchmarking", "competitive_positioning", "strategic_analysis"]
        )
        
        # Performance Improvement Planning
        self.templates['performance_improvement_planning'] = PromptTemplate(
            name="Performance Improvement and Value Creation Planning",
            category=PromptCategory.FINANCIAL_ANALYSIS,
            base_prompt="""
Develop comprehensive performance improvement strategy based on benchmarking analysis, targeting {improvement_areas} with quantified value creation potential.

**PERFORMANCE IMPROVEMENT FRAMEWORK:**

1. **PERFORMANCE GAP PRIORITIZATION**
   
   **Gap Assessment Matrix:**
   - Performance gap size and significance
   - Financial impact and value creation potential
   - Implementation complexity and feasibility
   - Resource requirements and investment needs
   - Time horizon and achievement timeline
   
   **Priority Ranking Methodology:**
   - High impact, low complexity (quick wins)
   - High impact, high complexity (strategic initiatives)
   - Medium impact opportunities (efficiency gains)
   - Long-term transformation initiatives
   - Defensive improvement necessities

2. **VALUE CREATION QUANTIFICATION**
   
   **Financial Impact Analysis:**
   - Revenue enhancement opportunities and sizing
   - Cost reduction potential and implementation costs
   - Margin improvement and profitability impact
   - Cash flow generation and timing analysis
   - Return on investment and payback analysis
   
   **Strategic Value Assessment:**
   - Competitive advantage creation and sustainability
   - Market position improvement and brand enhancement
   - Capability building and platform development
   - Option value and future opportunity creation
   - Risk reduction and business resilience

3. **IMPROVEMENT INITIATIVE DEVELOPMENT**
   
   **Revenue Enhancement Initiatives:**
   - Customer acquisition and retention improvement
   - Pricing optimization and revenue management
   - Product/service portfolio enhancement
   - Market expansion and channel development
   - Cross-selling and upselling optimization
   
   **Operational Excellence Initiatives:**
   - Process automation and digitization
   - Supply chain optimization and efficiency
   - Quality improvement and error reduction
   - Productivity enhancement and skill development
   - Cost structure optimization and rationalization
   
   **Strategic Transformation Initiatives:**
   - Digital transformation and technology upgrade
   - Business model innovation and development
   - Organizational design and culture change
   - Partnership and ecosystem development
   - Innovation and R&D capability building

4. **IMPLEMENTATION ROADMAP AND GOVERNANCE**
   
   **Phased Implementation Plan:**
   - Phase 1: Quick wins and foundational improvements (0-6 months)
   - Phase 2: Core improvement initiatives (6-18 months)
   - Phase 3: Strategic transformation projects (18+ months)
   - Resource allocation and capability development
   - Risk management and mitigation planning
   
   **Performance Monitoring and Control:**
   - KPI framework and measurement system
   - Performance tracking and reporting cadence
   - Course correction and adjustment mechanisms
   - Success celebration and learning integration
   - Continuous improvement culture development

5. **STAKEHOLDER ENGAGEMENT AND COMMUNICATION**
   - Leadership alignment and commitment
   - Employee engagement and change management
   - Customer communication and expectation management
   - Investor relations and progress reporting
   - Board oversight and governance framework

**VALUE CREATION SUMMARY:**
- Total value creation potential quantification
- Investment requirements and resource allocation
- Implementation timeline and milestone planning
- Success metrics and performance targets
- Risk assessment and mitigation strategies

{industry_context}
{role_focus}
{improvement_areas} specific implementation guidance and best practices.

Provide comprehensive performance improvement strategy with clear business case and implementation roadmap.
""",
            variables={
                "improvement_areas": "operational efficiency and customer satisfaction"
            },
            quality_criteria=[
                "Comprehensive performance gap analysis with quantification",
                "Clear value creation business case with financial modeling",
                "Detailed implementation roadmap with phasing and milestones",
                "Robust performance monitoring and governance framework",
                "Stakeholder engagement and change management strategy"
            ],
            tags=["performance_improvement", "value_creation", "operational_excellence", "transformation_planning"]
        )
        
        # Register templates
        for template in self.templates.values():
            prompt_manager.register_template(template)
    
    def generate_benchmark_analysis_prompt(self, config: BenchmarkConfig,
                                         context: Dict[str, Any]) -> str:
        """Generate comprehensive benchmark analysis prompt."""
        template = self.templates['comprehensive_benchmark_analysis']
        
        variables = {
            'benchmark_scope': config.benchmark_scope.value.replace('_', ' '),
            'time_period': config.time_period
        }
        
        prompt = template.base_prompt
        for key, value in variables.items():
            prompt = prompt.replace(f"{{{key}}}", str(value))
        
        adapted_prompt = context_adapter.adapt_prompt(prompt, context.get('prompt_context'))
        
        return adapted_prompt
    
    def generate_industry_benchmark_prompt(self, company_size: str, industry: str,
                                         context: Dict[str, Any]) -> str:
        """Generate industry benchmark analysis prompt."""
        template = self.templates['industry_benchmark_analysis']
        
        variables = {
            'company_size': company_size,
            'industry': industry
        }
        
        prompt = template.base_prompt
        for key, value in variables.items():
            prompt = prompt.replace(f"{{{key}}}", str(value))
        
        adapted_prompt = context_adapter.adapt_prompt(prompt, context.get('prompt_context'))
        
        return adapted_prompt
    
    def generate_improvement_planning_prompt(self, improvement_areas: str,
                                           context: Dict[str, Any]) -> str:
        """Generate performance improvement planning prompt."""
        template = self.templates['performance_improvement_planning']
        
        variables = {
            'improvement_areas': improvement_areas
        }
        
        prompt = template.base_prompt
        for key, value in variables.items():
            prompt = prompt.replace(f"{{{key}}}", str(value))
        
        adapted_prompt = context_adapter.adapt_prompt(prompt, context.get('prompt_context'))
        
        return adapted_prompt
    
    def get_industry_benchmark_metrics(self) -> Dict[str, List[str]]:
        """Generate comprehensive industry benchmarking metrics by category."""
        return {
            'financial_performance': [
                'Revenue growth rate (3-year CAGR)',
                'EBITDA margin',
                'Net profit margin',
                'Return on Assets (ROA)',
                'Return on Equity (ROE)',
                'Return on Invested Capital (ROIC)',
                'Free cash flow margin',
                'Cash conversion cycle',
                'Debt-to-equity ratio',
                'Interest coverage ratio'
            ],
            'operational_efficiency': [
                'Revenue per employee',
                'Operating expense ratio',
                'Asset turnover',
                'Inventory turnover',
                'Receivables turnover',
                'Working capital efficiency',
                'Capacity utilization',
                'Quality metrics (defect rates)',
                'Customer acquisition cost',
                'Customer lifetime value'
            ],
            'growth_and_investment': [
                'R&D as % of revenue',
                'Capital expenditure as % of revenue',
                'Technology spending ratio',
                'Employee training investment',
                'Innovation pipeline strength',
                'Time to market metrics',
                'Market share growth',
                'Geographic expansion rate',
                'New product revenue %',
                'Digital transformation progress'
            ],
            'customer_and_market': [
                'Customer satisfaction scores',
                'Net Promoter Score (NPS)',
                'Customer retention rate',
                'Market share position',
                'Brand recognition metrics',
                'Customer complaint rates',
                'Service quality metrics',
                'Cross-selling effectiveness',
                'Customer engagement metrics',
                'Pricing premium ability'
            ],
            'esg_and_sustainability': [
                'Carbon footprint intensity',
                'Energy efficiency metrics',
                'Waste reduction performance',
                'Diversity and inclusion metrics',
                'Employee engagement scores',
                'Community investment ratio',
                'Governance rating scores',
                'Regulatory compliance record',
                'Stakeholder satisfaction',
                'Sustainability reporting quality'
            ]
        }
    
    def generate_performance_gap_framework(self) -> Dict[str, Any]:
        """Generate performance gap analysis framework."""
        return {
            'gap_assessment_methodology': {
                'data_collection': [
                    'Public financial data analysis',
                    'Industry reports and surveys',
                    'Management consulting benchmarks',
                    'Credit rating agency reports',
                    'Investor presentations and calls'
                ],
                'gap_calculation': [
                    'Absolute gap (our metric - benchmark)',
                    'Relative gap (our metric / benchmark)',
                    'Percentile ranking position',
                    'Standard deviations from mean',
                    'Quartile positioning analysis'
                ]
            },
            'gap_prioritization_criteria': {
                'financial_impact': {
                    'weight': 0.35,
                    'measurement': 'NPV of closing gap',
                    'scale': '1-10'
                },
                'competitive_importance': {
                    'weight': 0.25,
                    'measurement': 'Strategic significance',
                    'scale': '1-10'
                },
                'implementation_feasibility': {
                    'weight': 0.20,
                    'measurement': 'Ease of execution',
                    'scale': '1-10'
                },
                'resource_requirements': {
                    'weight': 0.20,
                    'measurement': 'Investment needed',
                    'scale': '1-10 (inverse)'
                }
            },
            'improvement_target_setting': [
                'Top quartile performance target',
                'Best-in-class aspiration level',
                'Phased improvement milestones',
                'Time-bound achievement timeline',
                'Risk-adjusted target ranges'
            ]
        }
    
    def generate_benchmarking_governance_framework(self) -> Dict[str, Any]:
        """Generate benchmarking governance and monitoring framework."""
        return {
            'governance_structure': {
                'steering_committee': {
                    'composition': 'C-suite executives',
                    'frequency': 'Quarterly',
                    'responsibilities': [
                        'Strategic direction and priorities',
                        'Resource allocation decisions',
                        'Performance target approval',
                        'Major initiative oversight'
                    ]
                },
                'working_groups': {
                    'composition': 'Functional leaders and analysts',
                    'frequency': 'Monthly',
                    'responsibilities': [
                        'Data collection and analysis',
                        'Best practice identification',
                        'Improvement initiative development',
                        'Progress monitoring and reporting'
                    ]
                }
            },
            'monitoring_framework': {
                'data_refresh_cycle': 'Quarterly with annual comprehensive update',
                'reporting_cadence': 'Monthly dashboard, quarterly deep dive',
                'escalation_triggers': [
                    'Performance deterioration vs. benchmarks',
                    'New competitive threats identified',
                    'Industry best practices evolution',
                    'Regulatory or market changes'
                ],
                'continuous_improvement': [
                    'Benchmarking methodology refinement',
                    'Peer group composition updates',
                    'Metric relevance and validity review',
                    'Stakeholder feedback integration'
                ]
            }
        }


# Global performance benchmark analyzer instance
performance_benchmark_analyzer = PerformanceBenchmarkAnalyzer()