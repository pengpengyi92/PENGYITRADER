import pandas as pd
from utils.factor_utils import FactorUtils

class BacktestStrategy:
    def __init__(self, strategy, data):
        """
        初始化策略回测
        :param strategy: 策略实例
        :param data: pandas.DataFrame，包含因子数据和价格数据
        """
        self.strategy = strategy
        self.data = data

    def run(self):
        """
        运行回测
        :return: pandas.Series，策略收益
        """
        signals = self.strategy.generate_signals(self.data)
        returns = self.data['Close'].pct_change().shift(-1)  # 下一期收益率
        strategy_returns = (signals * returns).sum(axis=1)  # 策略收益
        return strategy_returns.dropna()

    def evaluate(self, strategy_returns):
        """
        评估策略表现
        :param strategy_returns: pandas.Series，策略收益
        """
        cumulative_returns = (1 + strategy_returns).cumprod()
        annualized_return = (cumulative_returns.iloc[-1] ** (252 / len(strategy_returns))) - 1
        max_drawdown = (cumulative_returns / cumulative_returns.cummax() - 1).min()

        print(f"Annualized Return: {annualized_return:.2%}")
        print(f"Max Drawdown: {max_drawdown:.2%}")
