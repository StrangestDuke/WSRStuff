import sys

sys.path.append('../')

import pandas as pd
import logging
from zenml import step

from src.model_dev import LinearRegressionModel
from steps.config import ModelNameConfig
from sklearn.base import RegressorMixin
@step
def train_model(
        X_train: pd.DataFrame,
        X_test: pd.DataFrame,
        Y_train: pd.DataFrame,
        Y_test: pd.DataFrame,
        config: ModelNameConfig,
) -> LinearRegressionModel:
    """
    Trains the model on ingested data
    """
    try:
        model = None
        if config.model_name == "LinearRegression":
            model = LinearRegressionModel()
            trained_model = model.train(X_train, Y_train)
            return trained_model
        else:
            raise ValueError("Model {} not supported".format(config.model_name))
    except Exception as e:
        logging.error("Error in training model: {}".format(e))
        raise e