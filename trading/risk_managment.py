import logging

class RiskManager:
    def __init__(self, max_loss_per_trade=0.02, max_drawdown=0.1):
        """
        初始化风险管理器
        :param max_loss_per_trade: 单笔交易最大亏损比例（默认 2%）
        :param max_drawdown: 最大回撤比例（默认 10%）
        """
        self.max_loss_per_trade = max_loss_per_trade
        self.max_drawdown = max_drawdown
        logging.basicConfig(filename='trade/logs/risk_manager.log', level=logging.INFO)

    def check_risk(self, portfolio):
        """
        检查风险
        :param portfolio: 当前投资组合
        :return: 是否需要止损
        """
        current_value = portfolio.current_value
        initial_value = portfolio.initial_value
        drawdown = (initial_value - current_value) / initial_value

        if drawdown >= self.max_drawdown:
            logging.warning(f"Max drawdown reached: {drawdown:.2%}")
            return True  # 需要止损
        return False
