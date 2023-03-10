import pandas as pd
import numpy as np
import abc

NUMERO_BARRAS = 33
DIMENSAO = 3
N_INDIVIDUOS = 200


def random_population(population: pd.DataFrame) -> pd.DataFrame:
    size = (3, 200)

    posicoes = np.random.uniform(0, high=NUMERO_BARRAS, size=size)
    velocidades = np.random.uniform(size=size)

    return posicoes, velocidades

def new_population() -> pd.DataFrame:
    population = pd.DataFrame(columns=[
        "speed", "position", "best_position", "objective"
    ])
