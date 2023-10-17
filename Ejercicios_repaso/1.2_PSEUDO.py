"""Muestra la relación entre dos numeros que introduce el usuario.

Inicio

    Escribe "Introduce dos numeros: "
    Lee numero1
    Lee numero2
    
    Si (numero1 == numero2) entonces
        Escribe "numero1 y numero2 son iguales."
    Sino 
        Si (numero1 > numero2) entonces
            Escribe "numero1 es mayor que numero2."
        Sino 
            Escribe "numero2 es mayor que numero1."
Fin
"""

print("Introduce dos numeros: ")
numero1 = int(input)
numero2 = int(input())

if (numero1 == numero2):
    print(f"{numero1} y {numero2} son iguales.")
else:
    if (numero1 > numero2):
        print (f"{numero1} es mayor que {numero2}.")
    else:
        print(f"{numero2} es mayor que {numero1}.")