"""
Financial Forecast Analyzer
Simple working implementation for portfolio demonstration
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Tuple
import json
from datetime import datetime, timedelta
import math
import random


@dataclass
class HistoricalData:
    """Historical financial data point."""
    period: str  # "2023-Q1", "2023-12", etc.
    revenue: float
    expenses: float
    ebitda: float
    cash_flow: float


@dataclass
class ForecastAssumptions:
    """Key assumptions for financial forecasting."""
    revenue_growth_rate: float = 0.10  # 10% annual growth
    expense_ratio: float = 0.75  # Expenses as % of revenue
    seasonal_factor: Dict[int, float] = field(default_factory=lambda: {1: 0.9, 2: 0.95, 3: 1.0, 4: 1.15})
    market_conditions: str = "stable"  # "growth", "stable", "decline"
    confidence_interval: float = 0.80  # 80% confidence


@dataclass
class ForecastResult:
    """Financial forecast analysis result."""
    forecast_periods: List[str]
    revenue_forecast: List[float]
    expense_forecast: List[float]
    ebitda_forecast: List[float]
    cash_flow_forecast: List[float]
    confidence_bands: Dict[str, List[Tuple[float, float]]]
    scenario_analysis: Dict[str, Dict[str, List[float]]]
    key_metrics: Dict[str, float]
    risks_opportunities: List[str]


class FinancialForecastAnalyzer:
    """Advanced financial forecasting with scenario analysis."""
    
    def __init__(self):
        self.forecast_horizon_quarters = 8  # 2 years quarterly forecast
        self.monte_carlo_simulations = 1000
    
    def analyze_historical_trends(self, historical_data: List[HistoricalData]) -> Dict[str, Any]:
        """Analyze historical data to identify trends and patterns."""
        if not historical_data:
            return {'growth_rate': 0.0, 'seasonality': {}, 'volatility': 0.0}
        
        # Calculate growth rates
        revenues = [d.revenue for d in historical_data]
        growth_rates = []
        
        for i in range(1, len(revenues)):
            if revenues[i-1] > 0:
                growth_rate = (revenues[i] - revenues[i-1]) / revenues[i-1]
                growth_rates.append(growth_rate)
        
        avg_growth_rate = sum(growth_rates) / len(growth_rates) if growth_rates else 0.0
        
        # Calculate volatility (standard deviation of growth rates)
        if len(growth_rates) > 1:
            mean_growth = avg_growth_rate
            variance = sum((g - mean_growth) ** 2 for g in growth_rates) / (len(growth_rates) - 1)
            volatility = math.sqrt(variance)
        else:
            volatility = 0.0
        
        # Identify seasonality patterns (simplified)
        seasonality = {}
        if len(historical_data) >= 4:
            avg_revenue = sum(revenues) / len(revenues)
            for i, data in enumerate(historical_data):
                quarter = (i % 4) + 1
                if quarter not in seasonality:
                    seasonality[quarter] = []
                seasonality[quarter].append(data.revenue / avg_revenue)
            
            # Average seasonal factors
            for quarter in seasonality:
                seasonality[quarter] = sum(seasonality[quarter]) / len(seasonality[quarter])
        
        return {
            'growth_rate': avg_growth_rate,
            'seasonality': seasonality,
            'volatility': volatility,
            'avg_revenue': sum(revenues) / len(revenues),
            'avg_margin': sum(d.ebitda / d.revenue for d in historical_data if d.revenue > 0) / len(historical_data)
        }
    
    def generate_base_forecast(self, historical_data: List[HistoricalData],
                              assumptions: ForecastAssumptions) -> Dict[str, List[float]]:
        """Generate base case financial forecast."""
        
        if not historical_data:
            # Default baseline if no historical data
            last_revenue = 1000000  # $1M baseline
            last_ebitda_margin = 0.20
        else:
            last_revenue = historical_data[-1].revenue
            last_ebitda_margin = historical_data[-1].ebitda / historical_data[-1].revenue if historical_data[-1].revenue > 0 else 0.20
        
        trends = self.analyze_historical_trends(historical_data)
        
        # Generate quarterly forecasts
        forecast = {
            'revenue': [],
            'expenses': [],
            'ebitda': [],
            'cash_flow': [],
            'periods': []
        }
        
        base_date = datetime.now()
        current_revenue = last_revenue
        
        for quarter in range(1, self.forecast_horizon_quarters + 1):
            # Calculate forecast date
            forecast_date = base_date + timedelta(days=90 * quarter)
            period = f"{forecast_date.year}-Q{((forecast_date.month - 1) // 3) + 1}"
            forecast['periods'].append(period)
            
            # Apply growth rate (quarterly)
            quarterly_growth = assumptions.revenue_growth_rate / 4
            current_revenue *= (1 + quarterly_growth)
            
            # Apply seasonality
            season_quarter = ((forecast_date.month - 1) // 3) + 1
            seasonal_multiplier = assumptions.seasonal_factor.get(season_quarter, 1.0)
            seasonal_revenue = current_revenue * seasonal_multiplier
            
            # Apply market conditions adjustment
            market_multiplier = {
                'growth': 1.05,
                'stable': 1.0,
                'decline': 0.95
            }.get(assumptions.market_conditions, 1.0)
            
            final_revenue = seasonal_revenue * market_multiplier
            
            # Calculate expenses and other metrics
            expenses = final_revenue * assumptions.expense_ratio
            ebitda = final_revenue - expenses
            
            # Simple cash flow approximation (EBITDA - working capital change - capex)
            cash_flow = ebitda * 0.85  # Simplified cash conversion
            
            forecast['revenue'].append(final_revenue)
            forecast['expenses'].append(expenses)
            forecast['ebitda'].append(ebitda)
            forecast['cash_flow'].append(cash_flow)
        
        return forecast
    
    def generate_scenario_analysis(self, base_forecast: Dict[str, List[float]],
                                 assumptions: ForecastAssumptions) -> Dict[str, Dict[str, List[float]]]:
        """Generate optimistic and pessimistic scenarios."""
        
        scenarios = {}
        
        # Optimistic scenario (20% higher growth, better margins)
        optimistic = {
            'revenue': [r * 1.15 for r in base_forecast['revenue']],
            'expenses': [e * 0.92 for e in base_forecast['expenses']],  # Better cost control
            'ebitda': [],
            'cash_flow': []
        }
        
        for i in range(len(optimistic['revenue'])):
            ebitda = optimistic['revenue'][i] - optimistic['expenses'][i]
            optimistic['ebitda'].append(ebitda)
            optimistic['cash_flow'].append(ebitda * 0.90)  # Better cash conversion
        
        scenarios['optimistic'] = optimistic
        
        # Pessimistic scenario (lower growth, margin pressure)
        pessimistic = {
            'revenue': [r * 0.85 for r in base_forecast['revenue']],
            'expenses': [e * 1.05 for e in base_forecast['expenses']],  # Cost inflation
            'ebitda': [],
            'cash_flow': []
        }
        
        for i in range(len(pessimistic['revenue'])):
            ebitda = pessimistic['revenue'][i] - pessimistic['expenses'][i]
            pessimistic['ebitda'].append(ebitda)
            pessimistic['cash_flow'].append(ebitda * 0.75)  # Worse cash conversion
        
        scenarios['pessimistic'] = pessimistic
        
        # Conservative scenario (modest growth)
        conservative = {
            'revenue': [r * 0.95 for r in base_forecast['revenue']],
            'expenses': [e for e in base_forecast['expenses']],
            'ebitda': [],
            'cash_flow': []
        }
        
        for i in range(len(conservative['revenue'])):
            ebitda = conservative['revenue'][i] - conservative['expenses'][i]
            conservative['ebitda'].append(ebitda)
            conservative['cash_flow'].append(ebitda * 0.82)
        
        scenarios['conservative'] = conservative
        
        return scenarios
    
    def calculate_confidence_bands(self, base_forecast: Dict[str, List[float]],
                                 assumptions: ForecastAssumptions) -> Dict[str, List[Tuple[float, float]]]:
        """Calculate confidence bands using Monte Carlo simulation."""
        
        confidence_bands = {
            'revenue': [],
            'ebitda': [],
            'cash_flow': []
        }
        
        # Simplified Monte Carlo - vary key assumptions
        for quarter in range(len(base_forecast['revenue'])):
            simulations = {
                'revenue': [],
                'ebitda': [],
                'cash_flow': []
            }
            
            # Run simulations
            for _ in range(100):  # Reduced for demo
                # Vary growth rate and expense ratio
                growth_variance = random.uniform(-0.05, 0.05)  # ±5% variance
                expense_variance = random.uniform(-0.03, 0.03)  # ±3% variance
                
                # Apply variance to base forecast
                sim_revenue = base_forecast['revenue'][quarter] * (1 + growth_variance)
                sim_expenses = base_forecast['expenses'][quarter] * (1 + expense_variance)
                sim_ebitda = sim_revenue - sim_expenses
                sim_cash_flow = sim_ebitda * random.uniform(0.75, 0.95)
                
                simulations['revenue'].append(sim_revenue)
                simulations['ebitda'].append(sim_ebitda)
                simulations['cash_flow'].append(sim_cash_flow)
            
            # Calculate confidence intervals
            confidence_level = assumptions.confidence_interval
            lower_percentile = (1 - confidence_level) / 2
            upper_percentile = 1 - lower_percentile
            
            for metric in ['revenue', 'ebitda', 'cash_flow']:
                values = sorted(simulations[metric])
                lower_idx = int(len(values) * lower_percentile)
                upper_idx = int(len(values) * upper_percentile)
                
                lower_bound = values[lower_idx] if lower_idx < len(values) else values[0]
                upper_bound = values[upper_idx] if upper_idx < len(values) else values[-1]
                
                confidence_bands[metric].append((lower_bound, upper_bound))
        
        return confidence_bands
    
    def identify_risks_opportunities(self, forecast_data: Dict[str, Any],
                                   assumptions: ForecastAssumptions) -> List[str]:
        """Identify key risks and opportunities based on forecast."""
        risks_opps = []
        
        # Revenue growth analysis
        revenue_growth = [(forecast_data['base']['revenue'][i] / forecast_data['base']['revenue'][i-1] - 1) * 4 
                         for i in range(1, len(forecast_data['base']['revenue']))]
        avg_growth = sum(revenue_growth) / len(revenue_growth) if revenue_growth else 0
        
        if avg_growth > 0.20:
            risks_opps.append("OPPORTUNITY: High revenue growth projected - ensure operational scalability")
        elif avg_growth < 0.05:
            risks_opps.append("RISK: Low revenue growth - consider market expansion strategies")
        
        # Margin analysis
        margins = [forecast_data['base']['ebitda'][i] / forecast_data['base']['revenue'][i] 
                  for i in range(len(forecast_data['base']['revenue'])) 
                  if forecast_data['base']['revenue'][i] > 0]
        avg_margin = sum(margins) / len(margins) if margins else 0
        
        if avg_margin < 0.15:
            risks_opps.append("RISK: Low EBITDA margins - focus on cost optimization")
        elif avg_margin > 0.30:
            risks_opps.append("OPPORTUNITY: Strong margins - potential for increased investment")
        
        # Cash flow analysis
        negative_cf_quarters = sum(1 for cf in forecast_data['base']['cash_flow'] if cf < 0)
        if negative_cf_quarters > 0:
            risks_opps.append(f"RISK: {negative_cf_quarters} quarters with negative cash flow - monitor liquidity")
        
        # Market conditions
        if assumptions.market_conditions == "decline":
            risks_opps.append("RISK: Declining market conditions - develop defensive strategies")
        elif assumptions.market_conditions == "growth":
            risks_opps.append("OPPORTUNITY: Growing market - consider aggressive expansion")
        
        return risks_opps
    
    def generate_forecast(self, historical_data: List[HistoricalData],
                         assumptions: ForecastAssumptions) -> ForecastResult:
        """Generate comprehensive financial forecast."""
        
        # Generate base forecast
        base_forecast = self.generate_base_forecast(historical_data, assumptions)
        
        # Generate scenarios
        scenarios = self.generate_scenario_analysis(base_forecast, assumptions)
        scenarios['base'] = base_forecast
        
        # Calculate confidence bands
        confidence_bands = self.calculate_confidence_bands(base_forecast, assumptions)
        
        # Calculate key metrics
        total_revenue = sum(base_forecast['revenue'])
        total_ebitda = sum(base_forecast['ebitda'])
        avg_margin = (total_ebitda / total_revenue) * 100 if total_revenue > 0 else 0
        
        final_revenue = base_forecast['revenue'][-1] if base_forecast['revenue'] else 0
        initial_revenue = base_forecast['revenue'][0] if base_forecast['revenue'] else 1
        cagr = ((final_revenue / initial_revenue) ** (1/2) - 1) * 100 if initial_revenue > 0 else 0  # 2-year CAGR
        
        key_metrics = {
            'total_revenue_forecast': total_revenue,
            'total_ebitda_forecast': total_ebitda,
            'avg_margin_percent': avg_margin,
            'revenue_cagr_percent': cagr,
            'final_quarter_revenue': final_revenue,
            'cash_flow_total': sum(base_forecast['cash_flow'])
        }
        
        # Identify risks and opportunities
        risks_opportunities = self.identify_risks_opportunities(scenarios, assumptions)
        
        return ForecastResult(
            forecast_periods=base_forecast['periods'],
            revenue_forecast=base_forecast['revenue'],
            expense_forecast=base_forecast['expenses'],
            ebitda_forecast=base_forecast['ebitda'],
            cash_flow_forecast=base_forecast['cash_flow'],
            confidence_bands=confidence_bands,
            scenario_analysis=scenarios,
            key_metrics=key_metrics,
            risks_opportunities=risks_opportunities
        )
    
    def export_forecast(self, result: ForecastResult, company_name: str = "Company") -> str:
        """Export forecast analysis to JSON."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"financial_forecast_{company_name.lower().replace(' ', '_')}_{timestamp}.json"
        
        # Convert tuples to lists for JSON serialization
        confidence_bands_serializable = {}
        for metric, bands in result.confidence_bands.items():
            confidence_bands_serializable[metric] = [[lower, upper] for lower, upper in bands]
        
        export_data = {
            'company_name': company_name,
            'forecast_date': datetime.now().isoformat(),
            'forecast_periods': result.forecast_periods,
            'base_forecast': {
                'revenue': result.revenue_forecast,
                'expenses': result.expense_forecast,
                'ebitda': result.ebitda_forecast,
                'cash_flow': result.cash_flow_forecast
            },
            'scenario_analysis': result.scenario_analysis,
            'confidence_bands': confidence_bands_serializable,
            'key_metrics': result.key_metrics,
            'risks_opportunities': result.risks_opportunities
        }
        
        with open(filename, 'w') as f:
            json.dump(export_data, f, indent=2)
        
        return filename


def demo_usage():
    """Demonstrate the financial forecast analyzer."""
    print("📈 Financial Forecast Analyzer Demo")
    print("=" * 50)
    
    # Initialize analyzer
    analyzer = FinancialForecastAnalyzer()
    
    # Sample historical data (quarterly)
    historical_data = [
        HistoricalData("2022-Q1", 850000, 680000, 170000, 140000),
        HistoricalData("2022-Q2", 920000, 720000, 200000, 165000),
        HistoricalData("2022-Q3", 980000, 750000, 230000, 195000),
        HistoricalData("2022-Q4", 1100000, 825000, 275000, 230000),
        HistoricalData("2023-Q1", 950000, 750000, 200000, 170000),
        HistoricalData("2023-Q2", 1050000, 800000, 250000, 210000),
        HistoricalData("2023-Q3", 1150000, 850000, 300000, 255000),
        HistoricalData("2023-Q4", 1300000, 975000, 325000, 270000),
    ]
    
    # Define forecast assumptions
    assumptions = ForecastAssumptions(
        revenue_growth_rate=0.15,  # 15% annual growth
        expense_ratio=0.72,        # 72% expense ratio
        seasonal_factor={1: 0.88, 2: 0.98, 3: 1.05, 4: 1.18},  # Q4 strong, Q1 weak
        market_conditions="growth",
        confidence_interval=0.80
    )
    
    # Generate forecast
    result = analyzer.generate_forecast(historical_data, assumptions)
    
    # Display results
    print(f"\n📊 Forecast Summary (Next {len(result.forecast_periods)} Quarters)")
    print(f"Key Metrics:")
    print(f"  Total Revenue Forecast: ${result.key_metrics['total_revenue_forecast']:,.0f}")
    print(f"  Total EBITDA Forecast:  ${result.key_metrics['total_ebitda_forecast']:,.0f}")
    print(f"  Average EBITDA Margin:  {result.key_metrics['avg_margin_percent']:.1f}%")
    print(f"  Revenue CAGR:          {result.key_metrics['revenue_cagr_percent']:.1f}%")
    print(f"  Final Quarter Revenue: ${result.key_metrics['final_quarter_revenue']:,.0f}")
    
    # Quarterly breakdown
    print(f"\n📅 Quarterly Forecast Breakdown:")
    print(f"{'Period':<8} {'Revenue':<12} {'EBITDA':<12} {'Margin':<8} {'Cash Flow':<12}")
    print("-" * 55)
    
    for i, period in enumerate(result.forecast_periods):
        revenue = result.revenue_forecast[i]
        ebitda = result.ebitda_forecast[i]
        margin = (ebitda / revenue * 100) if revenue > 0 else 0
        cash_flow = result.cash_flow_forecast[i]
        
        print(f"{period:<8} ${revenue:<11,.0f} ${ebitda:<11,.0f} {margin:<7.1f}% ${cash_flow:<11,.0f}")
    
    # Scenario comparison
    print(f"\n🎯 Scenario Analysis (Total Revenue):")
    scenarios = ['pessimistic', 'conservative', 'base', 'optimistic']
    for scenario in scenarios:
        if scenario in result.scenario_analysis:
            total_revenue = sum(result.scenario_analysis[scenario]['revenue'])
            print(f"  {scenario.title():<12}: ${total_revenue:,.0f}")
    
    # Risks and opportunities
    if result.risks_opportunities:
        print(f"\n⚠️ 💡 Risks & Opportunities:")
        for item in result.risks_opportunities:
            icon = "⚠️" if item.startswith("RISK") else "💡"
            print(f"  {icon} {item}")
    
    # Export forecast
    filename = analyzer.export_forecast(result, "TechCorp Inc")
    print(f"\n📄 Forecast exported to: {filename}")


if __name__ == "__main__":
    demo_usage()