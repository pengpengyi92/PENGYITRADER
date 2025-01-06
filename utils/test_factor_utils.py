import pandas as pd
import numpy as np
from factor_utils import FactorUtils

def test_factor_utils():
    # 创建测试数据
    dates = pd.date_range("2023-01-01", periods=5)
    symbols = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]
    factor_data = pd.DataFrame(
        np.random.randn(5, 5),  # 5 个标的，5 个时间点的因子值
        index=symbols,
        columns=dates
    )

    # 测试截面 Z-Score 标准化
    print("Cross-sectional Z-Score:")
    print(FactorUtils.cross_sectional_zscore(factor_data))

    # 测试时序 Z-Score 标准化
    print("Time-series Z-Score:")
    print(FactorUtils.time_series_zscore(factor_data.T).T)  # 转置以测试时序标准化

    # 测试 Rank 排序
    print("Rank:")
    print(FactorUtils.rank(factor_data))

    # 测试行业中性化
    industry_data = pd.Series(["Tech", "Tech", "Tech", "Retail", "Auto"], index=symbols)
    print("Neutralized Factors:")
    print(FactorUtils.neutralize(factor_data, industry_data))

if __name__ == "__main__":
    test_factor_utils()
