import pandas as pd
import numpy as np
from scipy.stats import zscore

class FactorUtils:
    @staticmethod
    def cross_sectional_zscore(factor_data):
        """
        截面 Z-Score 标准化
        :param factor_data: pandas.DataFrame，某一时点的因子值，index 为标的代码，columns 为因子名称
        :return: 标准化后的因子值
        """
        return factor_data.apply(zscore)  # 对每一列（因子）进行 Z-Score 标准化

    @staticmethod
    def time_series_zscore(factor_data):
        """
        时序 Z-Score 标准化
        :param factor_data: pandas.DataFrame，某一标的的因子值，index 为时间，columns 为因子名称
        :return: 标准化后的因子值
        """
        return factor_data.apply(zscore)  # 对每一列（因子）进行 Z-Score 标准化

    @staticmethod
    def rank(factor_data):
        """
        Rank 排序，将因子值转换为 0 到 1 的等比例分布
        :param factor_data: pandas.DataFrame，某一时点的因子值，index 为标的代码，columns 为因子名称
        :return: 排序后的因子值（0 到 1）
        """
        return factor_data.rank(pct=True)  # 对每一列（因子）进行 Rank 排序

    @staticmethod
    def neutralize(factor_data, industry_data):
        """
        行业中性化处理
        :param factor_data: pandas.DataFrame，某一时点的因子值，index 为标的代码，columns 为因子名称
        :param industry_data: pandas.Series，标的代码对应的行业分类
        :return: 中性化后的因子值
        """
        neutralized_data = factor_data.copy()
        for industry in industry_data.unique():
            industry_mask = industry_data == industry
            neutralized_data[industry_mask] = FactorUtils.cross_sectional_zscore(factor_data[industry_mask])
        return neutralized_data
