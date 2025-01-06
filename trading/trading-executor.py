import time
import logging
from utils.time_utils import TimeUtils

class TradeExecutor:
    def __init__(self, api_client):
        """
        初始化交易执行器
        :param api_client: 交易所 API 客户端
        """
        self.api_client = api_client
        logging.basicConfig(filename='trade/logs/trade_executor.log', level=logging.INFO)

    def execute_trade(self, symbol, action, quantity):
        """
        执行交易
        :param symbol: 交易标的（如 "AAPL"）
        :param action: 交易动作（"buy" 或 "sell"）
        :param quantity: 交易数量
        """
        try:
            if action == "buy":
                order = self.api_client.place_order(symbol, "buy", quantity)
            elif action == "sell":
                order = self.api_client.place_order(symbol, "sell", quantity)
            else:
                raise ValueError("Invalid action. Must be 'buy' or 'sell'.")

            logging.info(f"Executed {action} order for {quantity} shares of {symbol} at {TimeUtils.datetime_to_str(time.gmtime())}")
            return order
        except Exception as e:
            logging.error(f"Failed to execute {action} order for {symbol}: {e}")
            raise
