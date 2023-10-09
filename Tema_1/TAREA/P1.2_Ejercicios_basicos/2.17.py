"""Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e 
imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido."""
nombre = str(input("Introduce tu nombre: "))
numero_veces = int(input("Introduce el numero de veces que quieres ver tu nombre: "))

for i in range(1,numero_veces+1):
    print(nombre)