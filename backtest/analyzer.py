import pandas as pd
from utils.visualization import Visualization

class FactorAnalyzer:
    @staticmethod
    def analyze_returns(factor, returns):
        """
        分析因子收益率
        :param factor: pandas.Series，因子值
        :param returns: pandas.Series，股票收益率
        :return: 因子收益率
        """
        factor_returns = factor * returns
        return factor_returns.mean()

    @staticmethod
    def analyze_correlation(factors):
        """
        分析因子相关性
        :param factors: pandas.DataFrame，包含多个因子
        :return: pandas.DataFrame，因子相关性矩阵
        """
        return factors.corr()

    @staticmethod
    def plot_factor_distribution(factor):
        """
        绘制因子分布图
        :param factor: pandas.Series，因子值
        """
        Visualization.plot_factor_distribution(factor)
