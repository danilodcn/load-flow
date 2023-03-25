import numpy as np
import pandas as pd

NUMERO_BARRAS = 33
DIMENSAO = 3
N_INDIVIDUOS = 200


def random_positions(population: pd.DataFrame) -> pd.DataFrame:
    """
    Gera posições e velocidades aleatórias para uma data população
    Examples:
        >>> p = new_population()
        >>> r = random_positions(p)
        >>> len(r)
        2
        >>> positions, speeds = r
        >>> len(positions) == N_INDIVIDUOS
        True
        >>> positions.size == N_INDIVIDUOS * DIMENSAO
        True
        >>> len(speeds) == N_INDIVIDUOS
        True
        >>> speeds.size == N_INDIVIDUOS * DIMENSAO
        True
    """
    size = (200, 3)

    positions = np.random.uniform(0, high=NUMERO_BARRAS, size=size)
    speeds = np.random.uniform(size=size)

    return positions, speeds


def new_population() -> pd.DataFrame:
    """
    Cria uma nova população vazia. População será abstraída por um DataFrame do pandas em que
    as linhas representam o indivíduos e as colunas serão:
     - speed: velocidade da partícula
     - position: posição da partícula no espaço
     - best_position: melhor posição da partícula
     - objective: valor da função objetivo

    Examples:
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
