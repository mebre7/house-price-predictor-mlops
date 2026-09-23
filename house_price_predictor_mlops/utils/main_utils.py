import os
import sys

import numpy as np
import dill
import yaml
from pandas import DataFrame

from house_price_predictor_mlops.exception import HousePricePredictorException
from house_price_predictor_mlops.logger import logging


def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise HousePricePredictorException(e, sys) from e

def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.dump(content, file)
    except Exception as e:
        raise HousePricePredictorException(e, sys) from e

def load_object(file_path: str) -> object:
    logging.info("Entered the load_object method of utils")

    try:

        with open(file_path, "rb") as file_obj:
            obj = dill.load(file_obj)

        logging.info("Exited the load_object method of utils")

        return obj

    except Exception as e:
        raise HousePricePredictorException(e, sys) from e



def save_numpy_array_data(file_path: str, array: np.ndarray):
    """
    Save numpy array data to file
    file_path: str location of file to save
    array: np.array data to save
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise HousePricePredictorException(e, sys) from e
    

def load_numpy_array_data(file_path: str) -> np.ndarray:
    """
    load numpy array data from file
    file_path: str location of file to load
    return: np.array data loaded
    """
    try:
        with open(file_path, 'rb') as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise HousePricePredictorException(e, sys) from e


def save_object(file_path: str, obj: object) -> None:
    logging.info("Entered the save_object method of utils")

    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

        logging.info("Exited the save_object method of utils")

    except Exception as e:
        raise HousePricePredictorException(e, sys) from e

def drop_columns(df: DataFrame, cols: list)-> DataFrame:

    """
    drop the columns form a pandas DataFrame
    df: pandas DataFrame
    cols: list of columns to be dropped
    """
    logging.info("Entered drop_columns methon of utils")

    try:
        df = df.drop(columns=cols, axis=1)

        logging.info("Exited the drop_columns method of utils")
        
        return df
    except Exception as e:
        raise HousePricePredictorException(e, sys) from e

# data_ingestion
def get_db_engine():
    pass
def read_table_as_dataframe():
    pass

def dataframe_to_table():
    pass
# data_validation, data_transformation
def get_missing_value_ratio():
    pass
def get_dataframe_schema():
    pass
def validate_schema():
    pass
def is_null_present():
    pass
def get_outlier_report():
    pass
# model_trainer, model_evaluation, model_pusher
def evaluate_model():
    pass
# model_training
def get_best_model_score():
    pass
def log_metrics_to_mlflow():
    pass
def log_params_to_mlflow():
    pass
def get_timestamp_string():
    pass
def ensure_dir():
    pass
def get_size_in_mb():
    pass