from factors.factor_model import FactorModel
from factors.factor_backtester import FactorBacktester
from data.datacollector import DataCollector
from data.datadealer import DataDealer

def main():
    # 获取数据
    collector = DataCollector()
    data = collector.fetch_data("AAPL", "2020-01-01", "2023-01-01")
    dealer = DataDealer()
    cleaned_data = dealer.clean_data(data)

    # 计算因子
    momentum = FactorCalculator.calculate_momentum(cleaned_data)
    volatility = FactorCalculator.calculate_volatility(cleaned_data)
    market_cap = FactorCalculator.calculate_market_cap(cleaned_data)

    # 构建因子数据
    factors = pd.DataFrame({
        "Momentum": momentum,
        "Volatility": volatility,
        "MarketCap": market_cap
    }).dropna()

    # 计算收益率
    returns = cleaned_data['Close'].pct_change().dropna()

    # 训练模型并优化因子权重
    factor_model = FactorModel()
    factor_weights = factor_model.optimize_factor_weights(factors, returns)
    print("Optimized Factor Weights:\n", factor_weights)

    # 回测因子模型
    portfolio_returns = factor_model.backtest_factor_model(factors, returns)
    print("Portfolio Returns:", portfolio_returns)

if __name__ == "__main__":
    main()
