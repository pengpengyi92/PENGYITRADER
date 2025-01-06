import pandas as pd
from utils.factor_utils import FactorUtils

class FactorCalculator:
    @staticmethod
    def calculate_momentum(data, window=20):
        """
        计算动量因子：过去 window 天的收益率
        :param data: pandas.DataFrame，包含股票价格数据
        :param window: 时间窗口（默认 20 天）
        :return: pandas.Series，动量因子
        """
        return data['Close'].pct_change(window)

    @staticmethod
    def calculate_volatility(data, window=20):
        """
        计算波动率因子：过去 window 天的收益率标准差
        :param data: pandas.DataFrame，包含股票价格数据
        :param window: 时间窗口（默认 20 天）
        :return: pandas.Series，波动率因子
        """
        return data['Close'].pct_change().rolling(window).std()

    @staticmethod
    def calculate_market_cap(data):
        """
        计算市值因子：股票的市值
        :param data: pandas.DataFrame，包含股票市值数据
        :return: pandas.Series，市值因子
        """
        return data['MarketCap']
