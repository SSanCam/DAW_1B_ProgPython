import pytest 
from src.P3_0._304 import contar_letras

@pytest.mark.parametrize(
    'palabra, letra, expected',
    [
        ('banana', 'a', 3),
        ('banana', 'b', 1)
    ]
)

def test_304(palabra, letra, expected):
    assert contar_letras(palabra, letra) == expected