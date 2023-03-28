import numpy as np
import pytest
from faker import Faker

from pso.pso import random_numbers

fake = Faker()


@pytest.fixture
def random_speeds():
    def get_speeds(min=2, max=30):
        number = 30
        vars = 3
        numbers = random_numbers(
            number=number,
            vars=vars,
            max=max,
            min=min,
        )
        return numbers

    return get_speeds


def test_criar_velocidades_representadas_por_números_reais_entre_min_e_max(random_speeds):
    min, max = 2, 200
    numbers = random_speeds(min, max)

    assert np.min(numbers) > min
    assert np.max(numbers) < max


def test_todas_as_posições_devem_ser_números_inteiros():
    number = 30
    vars = 3
    min, max = 2, 200
    numbers = random_numbers(number=number, vars=vars, max=max, min=min, type="int")

    assert numbers.dtype == np.int64
