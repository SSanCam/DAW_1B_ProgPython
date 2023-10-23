"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
"""
def edad():
    edad = int(input("Ingresa qué edad tienes: "))

    if (edad > 18):
        edad = ("Eres mayor de edad.")
    else:
        edad = ("Eres menor de edad.")
    
    return edad