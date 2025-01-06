import pandas as pd
from utils.factor_utils import FactorUtils

class FactorBacktester:
    @staticmethod
    def group_backtest(factor, returns, num_groups=5):
        """
        分组回测：根据因子值将股票分组，计算每组的收益率
        :param factor: pandas.Series，因子值
        :param returns: pandas.Series，股票收益率
        :param num_groups: 分组数量（默认 5 组）
        :return: pandas.DataFrame，每组的平均收益率
        """
        factor_rank = FactorUtils.rank(factor)
        group_labels = pd.qcut(factor_rank, num_groups, labels=False)
        group_returns = returns.groupby(group_labels).mean()
        return group_returns

    @staticmethod
    def factor_portfolio_backtest(factor, returns):
        """
        因子组合回测：构建因子组合，计算组合的收益率
        :param factor: pandas.Series，因子值
        :param returns: pandas.Series，股票收益率
        :return: pandas.Series，因子组合的收益率
        """
        factor_rank = FactorUtils.rank(factor)
        portfolio_returns = factor_rank * returns
        return portfolio_returns.mean()
