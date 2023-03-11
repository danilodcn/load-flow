import numpy as np
import pandas as pd

NUMERO_BARRAS = 33
DIMENSAO = 3
N_INDIVIDUOS = 200


def random_population(population: pd.DataFrame) -> pd.DataFrame:
    """
    funcao
    """
    size = (3, 200)

    posicoes = np.random.uniform(0, high=NUMERO_BARRAS, size=size)
    velocidades = np.random.uniform(size=size)

    return posicoes, velocidades


def new_population() -> pd.DataFrame:
    """
    Cria uma nova população vazia. População será abstraída por um DataFrame do pandas em que
    as linhas representam o indivíduos e as colunas serão:
     - speed: velocidade da partícula
     - position: posição da partícula no espaço
     - best_position: melhor posição da partícula
     - objective: valor da função objetivo
    >>> p = new_population()
    >>> isinstance(p, pd.DataFrame)
    True
    >>> p.empty
    True
    """
    population = pd.DataFrame(
        columns=["speed", "position", "best_position", "objective"],
        data=[],
    )
    return population
