from zenml import pipeline
from cleaning_data import clean_df
from igest_data import ingest_df
from model_train import train_model
from evaluate import evaluate_model


@pipeline
def train_pipeline(data_path: str):
    df = ingest_df(data_path)
    clean_df(df)
    train_model(df)
    evaluate_model(df)