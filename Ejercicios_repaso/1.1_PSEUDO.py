""" Realiza un algoritmo que lea dos números y muestre cuál es el mayor.
Inicio

    Escribe "Introduce dos números: "
    Lee numero1
    Lee numero2
    
    Si (numero1 > numero2) entonces
        Escribe "numero1 es mayor que numero2."
    Sino
        Escribe "numero2 es mayor que numero1."
        
Fin
"""
print("Introduce dos números: ")
numero1 = int(input())
numero2 = int(input())

if (numero1 > numero2):
        print(f"{numero1} es mayor que {numero2}.")
else:
    print(f"{numero2} es mayor que {numero1}.")