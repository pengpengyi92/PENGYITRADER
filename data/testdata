from datacollector import DataCollector
from datadealer import DataDealer
from datastorage import DataStorage
import pandas as pd

def test_data_module():
    # 初始化模块
    collector = DataCollector()
    dealer = DataDealer()
    storage = DataStorage()

    # 获取腾讯股票（HK:0700）过去三年的数据
    symbol = "0700.HK"  # 腾讯股票的 Yahoo Finance 代码
    end_date = pd.Timestamp.today().strftime("%Y-%m-%d")  # 今天作为结束日期
    start_date = (pd.Timestamp.today() - pd.DateOffset(years=3)).strftime("%Y-%m-%d")  # 三年前作为开始日期

    print(f"Fetching data for {symbol} from {start_date} to {end_date}...")

    # 获取数据
    raw_data = collector.fetch_data(symbol, start_date, end_date)
    print("Raw data:")
    print(raw_data.head())

    # 清洗数据
    cleaned_data = dealer.clean_data(raw_data)
    print("Cleaned data:")
    print(cleaned_data.head())

    # 存储数据
    filename = f"{symbol}.csv"
    storage.save_to_csv(cleaned_data, filename)
    print(f"Data saved to {filename}")

    # 加载数据
    loaded_data = storage.load_from_csv(filename)
    print("Loaded data:")
    print(loaded_data.head())

    # 检查数据是否一致
    if cleaned_data.equals(loaded_data):
        print("Test passed: Data is consistent!")
    else:
        print("Test failed: Data is inconsistent!")

if __name__ == "__main__":
    test_data_module()
