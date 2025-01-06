from data.datacollector import DataCollector
from data.datadealer import DataDealer
from factors.factor_calculator import FactorCalculator
from strategy.factor_strategy import FactorStrategy
from strategy.backtest_strategy import BacktestStrategy

def main():
    # 获取数据
    collector = DataCollector()
    data = collector.fetch_data("AAPL", "2020-01-01", "2023-01-01")
    dealer = DataDealer()
    cleaned_data = dealer.clean_data(data)

    # 计算因子
    momentum = FactorCalculator.calculate_momentum(cleaned_data)

    # 构建因子数据
    factor_data = pd.DataFrame({
        "Date": cleaned_data.index,
        "Symbol": "AAPL",
        "Close": cleaned_data["Close"],
        "Momentum": momentum
    })

    # 初始化策略
    strategy = FactorStrategy(factor_name="Momentum", top_n=1, rebalance_freq=5)

    # 回测策略
    backtest = BacktestStrategy(strategy, factor_data)
    strategy_returns = backtest.run()
    backtest.evaluate(strategy_returns)

if __name__ == "__main__":
    main()
