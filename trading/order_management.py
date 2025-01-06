import logging

class OrderManager:
    def __init__(self, api_client):
        """
        初始化订单管理器
        :param api_client: 交易所 API 客户端
        """
        self.api_client = api_client
        logging.basicConfig(filename='trade/logs/order_manager.log', level=logging.INFO)

    def create_order(self, symbol, action, quantity):
        """
        创建订单
        :param symbol: 交易标的
        :param action: 交易动作
        :param quantity: 交易数量
        :return: 订单 ID
        """
        try:
            order_id = self.api_client.create_order(symbol, action, quantity)
            logging.info(f"Created {action} order for {quantity} shares of {symbol}. Order ID: {order_id}")
            return order_id
        except Exception as e:
            logging.error(f"Failed to create order for {symbol}: {e}")
            raise

    def cancel_order(self, order_id):
        """
        撤销订单
        :param order_id: 订单 ID
        """
        try:
            self.api_client.cancel_order(order_id)
            logging.info(f"Cancelled order {order_id}")
        except Exception as e:
            logging.error(f"Failed to cancel order {order_id}: {e}")
            raise
