import pytest
from division import operacion_div

@pytest.mark.parametrize(
    "num1, num2, expected",
    [
        (10,5,2.00),
        (20,5,4.00),
        (6,0,"ERROR.\nNo puede dividirse entre 0.")
    ]
)

def operacion_div():
    assert operacion_div(10,5) == 2.00
    assert operacion_div(20,5) == 4.00
    assert operacion_div(456,11) == 41,45
    
    with pytest.reaises(ZeroDivisionError):
        operacion_div(6,0)