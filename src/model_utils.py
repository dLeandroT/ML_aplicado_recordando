import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.pipeline import Pipeline
from joblib import dump

def update_model(model: Pipeline) -> True:
    dump(model, 'models/model.pkl')


def save_simple_metrics_report(train_score:float, test_score: float, validation_score: float, model:Pipeline) -> None:
    with open('reports/report.txt', 'w') as report_file:
        report_file.write('# Model Pipeline Descrption')

        for key, value in model.named_steps.items():
            report_file.write(f'### {key}:{value.__repr__()}'+'\n')

        report_file.write(f'## Train Score: {train_score}'+'\n')
        report_file.write(f'## Test Score: {test_score}'+'\n')
        report_file.write(f'## Validation Score: {validation_score}'+'\n')


def get_model_performance_test_set(y_real: pd.Series, y_pred: pd.Series) -> None:
    plt.figure(figsize=(8, 8))
    sns.regplot(x=y_pred, y=y_real, scatter_kws={'alpha':0.5})
    plt.xlabel('Predicted Worldwide Gross')
    plt.ylabel('Real Worldwide Gross')
    plt.title('R2')
    plt.savefig('reports/figures/prediction_r2.png')