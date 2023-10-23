import pytest
from cadenaCaracteres import cadena

"""def test_cadenaCaracteres():
    assert cadena("aytortilla") == "La contraseña es correcta."
    assert cadena("aytortilla") == "La contraseña es correcta."
"""
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