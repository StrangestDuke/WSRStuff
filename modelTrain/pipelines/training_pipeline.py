import logging
from zenml import pipeline
import pandas as pd
from modelTrain.steps.cleaning_data import clean_df
from modelTrain.steps.igest_data import ingest_df
from modelTrain.steps.model_train import train_model
from modelTrain.steps.evaluate import evaluate_model


@pipeline()
def train_pipeline(data_path: str):
    df = ingest_df(data_path)
    clean_df(df)
    train_model(df)
    evaluate_model(df)