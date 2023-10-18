"""1.11 => recibe un número y retorna una cadena de caracteres con el resultado de la función.
"""
def cadena_caracteres():
    
    n = int(input("Introduce un numero entero: "))
    suma = (n * (n + 1)//2)
    return f"La suma total es de {suma}"

print(cadena_caracteres())