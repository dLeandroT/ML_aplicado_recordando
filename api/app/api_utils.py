from pandas import DataFrame
import os 
from io import BytesIO

from sklearn.pipeline import Pipeline
from joblib import load
from pydantic import BaseModel


def get_model() -> Pipeline:
    model_path = os.environ.get('MODEL_PATH', 'models/model.pkl')
    with open(model_path, 'rb') as model_file:
        model = load(BytesIO(model_file.read()))
    
    return model


def transform_to_dataframe(class_model: BaseModel) -> DataFrame:
    transition_dictionary = {key:[value] for key, value in class_model.model_dump().items()}
    return DataFrame(transition_dictionary)