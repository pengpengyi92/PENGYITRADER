import matplotlib.pyplot as plt
import pandas as pd

class Visualization:
    @staticmethod
    def plot_candlestick(data, title="K 线图"):
        """
        绘制 K 线图
        :param data: pandas.DataFrame，包含 "Open", "High", "Low", "Close" 列
        :param title: 图表标题
        """
        plt.figure(figsize=(10, 6))
        plt.plot(data.index, data["Close"], label="Close Price", color="blue")
        plt.fill_between(data.index, data["Low"], data["High"], color="lightblue", alpha=0.3)
        plt.title(title)
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        plt.grid()
        plt.show()

    @staticmethod
    def plot_returns(returns, title="收益曲线"):
        """
        绘制收益曲线
        :param returns: pandas.Series，收益数据
        :param title: 图表标题
        """
        plt.figure(figsize=(10, 6))
        plt.plot(returns.index, returns, label="Returns", color="green")
        plt.title(title)
        plt.xlabel("Date")
        plt.ylabel("Returns")
        plt.legend()
        plt.grid()
        plt.show()

    @staticmethod
    def plot_factor_distribution(factor_data, title="因子分布"):
        """
        绘制因子分布图
        :param factor_data: pandas.Series，因子数据
        :param title: 图表标题
        """
        plt.figure(figsize=(10, 6))
        plt.hist(factor_data, bins=50, color="orange", alpha=0.7)
        plt.title(title)
        plt.xlabel("Factor Value")
        plt.ylabel("Frequency")
        plt.grid()
        plt.show()
