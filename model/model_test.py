import pandas as pd
import numpy as np
from factors.factor_calculator import FactorCalculator
from factors.factor_model import FactorModel

def test_factor_model():
    # 生成测试数据
    dates = pd.date_range("2023-01-01", periods=100)
    prices = np.cumsum(np.random.randn(100)) + 100
    data = pd.DataFrame({
        "Close": prices,
        "MarketCap": np.random.randint(1e9, 1e10, size=100)
    }, index=dates)

    # 计算因子
    momentum = FactorCalculator.calculate_momentum(data)
    volatility = FactorCalculator.calculate_volatility(data)
    market_cap = FactorCalculator.calculate_market_cap(data)

    # 构建因子数据
    factors = pd.DataFrame({
        "Momentum": momentum,
        "Volatility": volatility,
        "MarketCap": market_cap
    }).dropna()

    # 计算收益率
    returns = data['Close'].pct_change().dropna()

    # 训练模型并优化因子权重
    factor_model = FactorModel()
    factor_weights = factor_model.optimize_factor_weights(factors, returns)
    print("Optimized Factor Weights:\n", factor_weights)

    # 回测因子模型
    portfolio_returns = factor_model.backtest_factor_model(factors, returns)
    print("Portfolio Returns:", portfolio_returns)

if __name__ == "__main__":
    test_factor_model()
