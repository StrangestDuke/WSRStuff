import logging
from abc import ABC, abstractmethod

from sklearn.linear_model import LinearRegression

class Model(ABC):
    """
    Abstract class for all models
    """
    @abstractmethod
    def train(self, X_train,Y_train):
        """
        Trains the model
        args:
            param X_train:
            param Y_train:
        return:
            None
        """
        pass

class LinearRegressionModel(Model):
    """
    Linear Regression model
    """

    def __init__(self):
        self.model = LinearRegression()

    def train(self, X_train, Y_train, **kwargs):
        """
        Trains the model
        args:
            param X_train:
            param Y_train:
        return:
            None
        """
        try:
            reg = LinearRegression(**kwargs)
            reg.fit(X_train, Y_train)
            logging.info("Model trained")
            return reg
        except Exception as e:
            logging.error("Error occured in proccess of model training: {}".format(e))
            raise e
