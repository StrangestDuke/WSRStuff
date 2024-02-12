import logging
from abc import ABC, abstractmethod
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
class Evaluation(ABC):
    @abstractmethod
    def calculate_scores(self, y_true: np.ndarray, y_pred: np.ndarray):
        pass
class MSE(Evaluation):
    def calculate_scores(self, y_true: np.ndarray, y_pred: np.ndarray):
        try:
            logging.info("Calculating MSE")
            mse = mean_squared_error(y_true, y_pred)
            logging.info("MSE: {}".format(mse))
            return mse
        except Exception as e:
            logging.info("Error in calculatin MSE: {}".format(e))
            raise e


class R2(Evaluation):
    """
    Evaluation Strategy that uses R2 Score
    """
    def calculate_scores(self, y_true: np.ndarray, y_pred: np.ndarray):
        try:
            logging.info("Calculating R2 score")
            r2 = r2_score(y_true, y_pred)
            logging.info("R2 Score {}".format(r2))
            return r2
        except Exception as e:
            logging.info("Error in calculating R2 Score {}".format(e))
            raise e

class RMSE(Evaluation):
    """
    Evaluation Strategy that uses Root Mean Squared Error
    """
    def calculate_scores(self, y_true: np.ndarray, y_pred: np.ndarray):
        try:
            logging.info("Calculating RMSE")
            rmse = mean_squared_error(y_true, y_pred, squared=False)
            logging.info("RMSE: {}".format(rmse))
            return rmse
        except Exception as e:
            logging.error("Error in calculatin RMSE: {}".format(e))
            raise e
