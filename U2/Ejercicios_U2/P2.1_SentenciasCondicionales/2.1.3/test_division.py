import pytest
from division import operacion_div

def test_operacion_div():
    assert operacion_div() == 2.00
    assert operacion_div() == ZeroDivisionError