class BaseStrategy:
    def __init__(self):
        pass

    def generate_signals(self, data):
        """
        生成交易信号
        :param data: pandas.DataFrame，包含因子数据和价格数据
        :return: pandas.DataFrame，交易信号
        """
        raise NotImplementedError

    def execute_trades(self, signals):
        """
        执行交易
        :param signals: pandas.DataFrame，交易信号
        """
        raise NotImplementedError
