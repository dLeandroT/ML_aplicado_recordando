from sklearn.pipeline import Pipeline
from joblib import dump

def update_model(model: Pipeline) -> True:
    dump(model, 'models/model.pkl')