import yfinance as yf
import pandas as pd

class DataCollector:
    def __init__(self):
        pass

    def fetch_data(self, symbol, start_date, end_date):
        """
        从 Yahoo Finance 获取股票历史数据
        :param symbol: 股票代码（如 "AAPL"）
        :param start_date: 开始日期（格式："YYYY-MM-DD"）
        :param end_date: 结束日期（格式："YYYY-MM-DD"）
        :return: pandas.DataFrame
        """
        try:
            data = yf.download(symbol, start=start_date, end=end_date)
            return data
        except Exception as e:
            print(f"Error fetching data: {e}")
            return pd.DataFrame()  # 返回空 DataFrame
