"""Encapsúlalo en una función llamada cuenta, y hazla genérica de tal modo que pueda aceptar una cadena y una letra como argumentos.

palabra = 'banana'
contador = 0
for letra in palabra:
    if letra == 'a':
        contador = contador + 1
print(contador)
"""
def cuenta(palabra, letra) -> str:
    
    contador = 0 
    
    for caracter in palabra:
        
        if (caracter == letra):
            contador += 1
            
    return contador 
    
