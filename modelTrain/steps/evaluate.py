import logging
from zenml import step
import pandas as pd

from sklearn.base import RegressorMixin

from modelTrain.src.evaluation import MSE, RMSE, R2
@step
def evaluate_model(model: RegressorMixin,
                   X_test: pd.DataFrame,
                   Y_test: pd.DataFrame
    ) -> None:
    """
    evaluates the model on the ingested data

    I dont know how, but guy in the video somehow dont have any errors with that code.
    """
    try:
        prediction = model.predict(X_test)
        mse_class = MSE()
        mse =  mse_class.calculate_scores(Y_test, prediction)

        r2_class = R2()
        r2 =  r2_class.calculate_scores(Y_test, prediction)


        rmse_class = RMSE()
        rmse =  rmse_class.calculate_scores(Y_test, prediction)

        return r2, rmse
    except Exception as e:
        logging.error("Error in model evaluation: {}".format(e))
        raise e