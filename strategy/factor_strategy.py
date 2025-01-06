import pandas as pd
from strategy.base_strategy import BaseStrategy

class FactorStrategy(BaseStrategy):
    def __init__(self, factor_name, top_n=10, rebalance_freq=1):
        """
        初始化因子选股策略
        :param factor_name: 因子名称
        :param top_n: 选股数量（默认前 10 只）
        :param rebalance_freq: 换仓频率（默认每天换仓）
        """
        self.factor_name = factor_name
        self.top_n = top_n
        self.rebalance_freq = rebalance_freq

    def generate_signals(self, data):
        """
        生成交易信号
        :param data: pandas.DataFrame，包含因子数据和价格数据
        :return: pandas.DataFrame，交易信号
        """
        signals = pd.DataFrame(index=data.index, columns=data['Symbol'].unique())
        for date, group in data.groupby('Date'):
            if (pd.to_datetime(date).day - 1) % self.rebalance_freq == 0:  # 换仓日
                top_stocks = group.nlargest(self.top_n, self.factor_name)['Symbol']
                signals.loc[date, top_stocks] = 1  # 买入信号
            else:
                signals.loc[date] = 0  # 持仓不动
        return signals

    def execute_trades(self, signals):
        """
        执行交易
        :param signals: pandas.DataFrame，交易信号
        """
        # 这里可以添加具体的交易逻辑，如调用交易 API
        print("Executing trades based on signals:")
        print(signals)
