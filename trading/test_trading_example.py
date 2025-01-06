from trade.trade_executor import TradeExecutor
from trade.order_manager import OrderManager
from trade.risk_manager import RiskManager
from trade.live_monitor import LiveMonitor
from strategy.factor_strategy import FactorStrategy
from data.datacollector import DataCollector
from data.datadealer import DataDealer

def main():
    # 获取实时数据
    collector = DataCollector()
    data = collector.fetch_live_data("AAPL")
    dealer = DataDealer()
    cleaned_data = dealer.clean_data(data)

    # 初始化策略
    strategy = FactorStrategy(factor_name="Momentum", top_n=1, rebalance_freq=5)

    # 初始化交易模块
    api_client = ...  # 交易所 API 客户端
    trade_executor = TradeExecutor(api_client)
    order_manager = OrderManager(api_client)
    risk_manager = RiskManager()
    live_monitor = LiveMonitor(strategy, portfolio)

    # 运行策略
    while True:
        try:
            signals = strategy.generate_signals(cleaned_data)
            for symbol, action in signals.items():
                if action == "buy":
                    trade_executor.execute_trade(symbol, "buy", quantity=100)
                elif action == "sell":
                    trade_executor.execute_trade(symbol, "sell", quantity=100)

            # 实时监控
            live_monitor.monitor()

            time.sleep(60)  # 每分钟运行一次
        except Exception as e:
            print(f"Error in main loop: {e}")
            break

if __name__ == "__main__":
    main()
