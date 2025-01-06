import pandas as pd
import os

class DataStorage:
    def __init__(self, storage_path="data/historical_data"):
        self.storage_path = storage_path
        # 如果存储路径不存在，则创建
        if not os.path.exists(self.storage_path):
            os.makedirs(self.storage_path)

    def save_to_csv(self, data, filename):
        """
        将数据保存为 CSV 文件
        :param data: pandas.DataFrame
        :param filename: 文件名（如 "AAPL.csv"）
        """
        try:
            file_path = os.path.join(self.storage_path, filename)
            data.to_csv(file_path)
            print(f"Data saved to {file_path}")
        except Exception as e:
            print(f"Error saving data to CSV: {e}")

    def load_from_csv(self, filename):
        """
        从 CSV 文件加载数据
        :param filename: 文件名（如 "AAPL.csv"）
        :return: pandas.DataFrame
        """
        try:
            file_path = os.path.join(self.storage_path, filename)
            data = pd.read_csv(file_path, index_col=0, parse_dates=True)
            return data
        except Exception as e:
            print(f"Error loading data from CSV: {e}")
            return pd.DataFrame()  # 返回空 DataFrame
