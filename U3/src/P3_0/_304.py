"""Hay un método de cadenas llamado count que es similar a find. Lee la documentación de este método en: * Métodos en ingles * Métodos en castellano

y escribe el código necesario para invocar a este método y contar el número de veces que una letra aparece en “banana”."""

def contar_letras(palabra: str, letra: str) -> int:
    
    resultado = palabra.count(letra)
    return resultado

