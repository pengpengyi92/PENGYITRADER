import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from utils.factor_utils import FactorUtils
from factors.factor_backtester import FactorBacktester

class FactorModel:
    def __init__(self):
        self.model = None

    def train_linear_model(self, factors, returns):
        """
        训练线性回归模型
        :param factors: pandas.DataFrame，因子数据
        :param returns: pandas.Series，收益率数据
        """
        X_train, X_test, y_train, y_test = train_test_split(factors, returns, test_size=0.2, random_state=42)
        self.model = LinearRegression()
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        print(f"Linear Regression MSE: {mse}")

    def train_random_forest(self, factors, returns):
        """
        训练随机森林模型
        :param factors: pandas.DataFrame，因子数据
        :param returns: pandas.Series，收益率数据
        """
        X_train, X_test, y_train, y_test = train_test_split(factors, returns, test_size=0.2, random_state=42)
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        print(f"Random Forest MSE: {mse}")

    def predict_returns(self, factors):
        """
        预测收益率
        :param factors: pandas.DataFrame，因子数据
        :return: pandas.Series，预测的收益率
        """
        if self.model is None:
            raise ValueError("Model has not been trained yet.")
        return pd.Series(self.model.predict(factors), index=factors.index)

    def optimize_factor_weights(self, factors, returns):
        """
        优化因子权重
        :param factors: pandas.DataFrame，因子数据
        :param returns: pandas.Series，收益率数据
        :return: pandas.Series，优化后的因子权重
        """
        self.train_linear_model(factors, returns)
        factor_weights = pd.Series(self.model.coef_, index=factors.columns)
        return factor_weights

    def backtest_factor_model(self, factors, returns):
        """
        回测因子模型
        :param factors: pandas.DataFrame，因子数据
        :param returns: pandas.Series，收益率数据
        :return: pandas.Series，回测结果
        """
        predicted_returns = self.predict_returns(factors)
        portfolio_returns = FactorBacktester.factor_portfolio_backtest(predicted_returns, returns)
        return portfolio_returns
