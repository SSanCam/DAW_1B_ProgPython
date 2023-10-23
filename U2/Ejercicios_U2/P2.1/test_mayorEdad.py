import pytest
from mayorEdad import edad

@pytest.mark.parametrize(
    "anios, expected",
    [
      (18, "Eres mayor de edad"),
      (20, "Eres mayor de edad"),
      (16, "Eres menor de edad."),
      (200, "Relaja Nosferatus.")
    ]
  )

def test_edad (anios,expected):
    assert edad(18) == ("Eres mayor de edad")
