"""Ejercicio 1.28
Realiza un algoritmo con PSEUDOCÓDIGO y pásalo a un programa en Python que :
lea dos números enteros, muestre cuál es el menor de los dos y cuantos números existen entre ellos dos.
El segundo número no puede ser igual, si es así, debe mostrar el error: "Los números no pueden ser iguales".
Si los números son diferentes, por ejemplo 5 y 12 debe mostrar la frase "El número menor es el 5 y entre ellos existen 7 números enteros".
El pseudocódigo debes incluirlo como comentarios en el programa de Python."""

"""PSEUDOCÓDIGO:
Inicio
    Lee numero1
    Lee numero2 
    
    Si (numero1 == numero2) entonces
        Escribe "Los números no pueden ser iguales" 
        
        
    Si (numero1 != numero2) entonces
        ////
        contador = 0
        Para numero en (numero1..numero2) entonces
            contador = contador + 1
        ////
        cantidad_numeros = numero1 - numero2
        Si (numero1 > numero2) entonces
            Escribe numero1 + " es mayor que " + numero2 + " y entre ellos existen " + contador + " números enteros."
            Sino
            Escribe numero1 + " es menor que " + numero2 + " y entre ellos existen " + contador + " números enteros."
Fin
"""
#Leo los dos números necesarios para el programa:
numero1 = int(input("Introduce un número entero: "))
numero2 = int(input("Introduce otro número entero: "))

#Vamos a escribir un mensaje si los dos números introducidos son iguales:
if (numero1 == numero2) :
    print("Los números no pueden ser iguales.")

#Si los números son distintos, vamos a contar cuantas cifras hay entre uno y otro 
Cantidac_numeros = abs(numero1 - numero2)

#Si los números son distintos vamos imprimir cúal es mayor y cual es menor:
if (numero1 != numero2):
    if (numero1 > numero2):
        print(f"{numero1} es mayor que {numero2} y entre ellos existen {Cantidac_numeros} números entre ellos.")
    else:
        print(f"{numero1} es menor que {numero2} y entre ellos existen {Cantidac_numeros} números entre ellos.")