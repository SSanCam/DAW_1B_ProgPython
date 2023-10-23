import pytest
from cadenaCaracteres import cadena

@pytest.mark.parametrize(
    "contrasenia, expected",
    [
        ("aytortilla","La contraseña es correcta."),
        ("AYtortilla","La contraseña es correcta."),
        ("ayTORTILLA","La contraseña es correcta."),
        ("nohaytortilla","Contraseña incorrecta."),
        ("tortilla","Contraseña incorrecta."),
        ("tortillasincebolla","Contraseña incorrecta.")
    ]
)
def test_cadena(contrasenia,expected):
    assert cadena() == expected