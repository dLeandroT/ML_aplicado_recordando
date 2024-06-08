from dvc import api
import pandas as pd
from io import StringIO
import sys




# Cargar los datos desde DVC
movie_data_path = api.read('data/raw/X_opening.csv', remote='dataset-track')
movie_data = pd.read_csv(StringIO(movie_data_path))

# Guardar para su uso
movie_data.to_csv("data/processed/lista_para_entrenar.csv", index=False)

