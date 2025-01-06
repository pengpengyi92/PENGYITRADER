import pandas as pd
from datetime import datetime, timedelta

class TimeUtils:
    @staticmethod
    def str_to_datetime(date_str, format="%Y-%m-%d"):
        """
        将字符串转换为 datetime 对象
        :param date_str: 日期字符串（如 "2023-01-01"）
        :param format: 日期格式（默认 "%Y-%m-%d"）
        :return: datetime 对象
        """
        return datetime.strptime(date_str, format)

    @staticmethod
    def datetime_to_str(date, format="%Y-%m-%d"):
        """
        将 datetime 对象转换为字符串
        :param date: datetime 对象
        :param format: 日期格式（默认 "%Y-%m-%d"）
        :return: 日期字符串
        """
        return date.strftime(format)

    @staticmethod
    def time_delta(start_date, end_date, unit="days"):
        """
        计算两个时间点之间的差值
        :param start_date: 开始时间（datetime 对象或字符串）
        :param end_date: 结束时间（datetime 对象或字符串）
        :param unit: 时间单位（"days", "hours", "minutes", "seconds"）
        :return: 时间差值
        """
        if isinstance(start_date, str):
            start_date = TimeUtils.str_to_datetime(start_date)
        if isinstance(end_date, str):
            end_date = TimeUtils.str_to_datetime(end_date)
        delta = end_date - start_date
        if unit == "days":
            return delta.days
        elif unit == "hours":
            return delta.total_seconds() / 3600
        elif unit == "minutes":
            return delta.total_seconds() / 60
        elif unit == "seconds":
            return delta.total_seconds()
        else:
            raise ValueError("Unsupported unit")

    @staticmethod
    def rolling_window(dates, window_size, step=1):
        """
        生成滚动时间窗口
        :param dates: 时间序列（list 或 pandas.DatetimeIndex）
        :param window_size: 窗口大小（天数）
        :param step: 步长（天数）
        :return: 滚动时间窗口的起始和结束时间
        """
        windows = []
        for i in range(0, len(dates) - window_size + 1, step):
            start = dates[i]
            end = dates[i + window_size - 1]
            windows.append((start, end))
        return windows
