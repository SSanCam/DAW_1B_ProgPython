"""1.1 => recibe un nombre y retorna una cadena de caracteres con el resultado.

"""
def saludo() :
    nombre = str(input("Escribe tu nombre: "))
    return nombre

print (f"Hola, {saludo()}")