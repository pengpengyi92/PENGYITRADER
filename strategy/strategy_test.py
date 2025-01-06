import pandas as pd
import numpy as np
from strategy.factor_strategy import FactorStrategy
from strategy.backtest_strategy import BacktestStrategy

def test_factor_strategy():
    # 生成测试数据
    dates = pd.date_range("2023-01-01", periods=100)
    symbols = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]
    data = pd.DataFrame({
        "Date": np.repeat(dates, len(symbols)),
        "Symbol": np.tile(symbols, len(dates)),
        "Close": np.random.randn(len(dates) * len(symbols)).cumsum() + 100,
        "Momentum": np.random.randn(len(dates) * len(symbols))
    })

    # 初始化策略
    strategy = FactorStrategy(factor_name="Momentum", top_n=2, rebalance_freq=5)

    # 回测策略
    backtest = BacktestStrategy(strategy, data)
    strategy_returns = backtest.run()
    backtest.evaluate(strategy_returns)

if __name__ == "__main__":
    test_factor_strategy()
