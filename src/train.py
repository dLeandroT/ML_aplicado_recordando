from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_validate
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import GradientBoostingRegressor

import sys
import numpy as np
import pandas as pd

from model_utils import update_model
from model_utils import save_simple_metrics_report
from model_utils import get_model_performance_test_set


# Cargar Datos
data = pd.read_csv('data/processed/lista_para_entrenar.csv')

# Modelo
model = Pipeline([
    ('imputer', SimpleImputer(strategy='mean', missing_values=np.nan)),
    ('core_model', GradientBoostingRegressor())
])

# Seopara variable objetivo
X = data.drop('worldwide_gross', axis=1)
y = data['worldwide_gross']

# Separar datos 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state=1562)

# Parametros a optimizar
param_tuning = {'core_model__n_estimators': range(20, 301, 20)}

# Modelo para optimizacion
grid_search = GridSearchCV(model, param_tuning, scoring='r2', cv=5)
grid_search.fit(X_train, y_train)


# Resultados
resultados = cross_validate(grid_search.best_estimator_, X_train, y_train, return_train_score=True, cv=5)

train_score = np.mean(resultados['train_score'])
test_score = np.mean(resultados['test_score'])

assert train_score > 0.7
assert test_score > 0.65


# actualizar modelo 
update_model(grid_search.best_estimator_)


# Guardar reporte de metricas 
validation_score = grid_search.best_estimator_.score(X_test, y_test)
save_simple_metrics_report(train_score, test_score, validation_score, grid_search.best_estimator_)


# Graficar
y_test_pred = grid_search.best_estimator_.predict(X_test)
get_model_performance_test_set(y_test, y_test_pred)