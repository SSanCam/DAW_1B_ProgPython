import pytest 
from src.P3_0._303 import cuenta

@pytest.mark.parametrize(
    'palabra, letra, expected',
    [
        ('banana', 'a', 3)
    ]
)

def test_303(palabra, letra, expected):
    assert cuenta(palabra, letra) == expected 
    