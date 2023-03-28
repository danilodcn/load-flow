from typing import Literal

import numpy as np
import pandas as pd


def new_population() -> pd.DataFrame:
    """
    Cria uma nova população vazia. População será abstraída por um DataFrame do pandas em que
    as linhas representam o indivíduos.
    As colunas serão:
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


def random_numbers(
    number: int,
    vars: int,
    max: int | None = None,
    min: int | None = None,
    type: Literal["int"] | Literal["float"] | None = None,
) -> np.ndarray:
    """
    Gera números aleatórios dependendo da entrada.

    Examples:
        >>> number = 200
        >>> vars = 3
        >>> min, max = 2, 20
        >>> numbers = random_numbers(number, vars, max, min)
        >>> len(numbers) == number
        True

    """
    max = max or 1
    min = min or 0
    assert min < max, "'min' deve ser menor do que 'max'"

    assert isinstance(vars, int), "'vars' deve ser inteiro"

    size = (number, vars)
    numbers = np.random.uniform(min, max, size=size)

    match type:
        case "int":
            numbers = np.int64(numbers)
    return numbers
