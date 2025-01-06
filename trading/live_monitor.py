import time
import logging
from utils.visualization import Visualization

class LiveMonitor:
    def __init__(self, strategy, portfolio):
        """
        初始化实时监控器
        :param strategy: 策略实例
        :param portfolio: 投资组合实例
        """
        self.strategy = strategy
        self.portfolio = portfolio
        logging.basicConfig(filename='trade/logs/live_monitor.log', level=logging.INFO)

    def monitor(self):
        """
        实时监控策略表现
        """
        while True:
            try:
                # 获取当前收益
                returns = self.portfolio.calculate_returns()
                logging.info(f"Current portfolio returns: {returns:.2%}")

                # 绘制收益曲线
                Visualization.plot_returns(returns)

                # 检查风险
                if self.portfolio.check_risk():
                    logging.warning("Risk threshold exceeded. Stopping strategy.")
                    break

                time.sleep(60)  # 每分钟检查一次
            except Exception as e:
                logging.error(f"Error in live monitoring: {e}")
                raise
