import pandas as pd

class DataDealer:
    def __init__(self):
        pass

    def clean_data(self, data):
        """
        清洗数据：处理缺失值、异常值等
        :param data: pandas.DataFrame
        :return: pandas.DataFrame
        """
        try:
            # 填充缺失值（前向填充）
            data.fillna(method='ffill', inplace=True)
            # 删除仍然包含缺失值的行
            data.dropna(inplace=True)
            return data
        except Exception as e:
            print(f"Error cleaning data: {e}")
            return pd.DataFrame()  # 返回空 DataFrame
