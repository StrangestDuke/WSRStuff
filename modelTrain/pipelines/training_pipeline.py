import logging
from zenml import pipelines
import pandas as pd
from ..steps.cleaning_data import clean_df
from ..steps.igest_data import ingest_df
from ..steps.model_train import train_model
from ..steps.evaluate import evaluate_model


@pipelines()
def train_pipeline(data_path: str):
    df = ingest_df(data_path)
    clean_df(df)
    train_model(df)
    evaluate_model(df)