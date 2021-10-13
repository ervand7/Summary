# Открыть файл по абсолютному пути
import os

with open(f"{os.path.abspath('repository_of_candidates_ids.csv')}", newline='') as file:
    pass
