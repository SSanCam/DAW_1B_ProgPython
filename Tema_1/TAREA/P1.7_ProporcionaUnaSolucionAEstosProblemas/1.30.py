"""Ejercicios 1.30
Realiza un algoritmo con PSEUDOCÓDIGO y pásalo a un programa en Python que pida un número de inicio, un incremento y un total de la serie.
El incremento y el total deben ser mayor que cero, sino el programa debe finalizar con un error u obligar a que introduzcan un valor correcto de ambos (os lo dejo a vuestra elección, la primera opción es más fácil, aunque el mundo está lleno de valientes)
Por ejemplo, si introducen los valores 1, 1 y 10, el programa mostrará en consola exactamente lo siguiente: SERIE => 1-2..3..4..5..6..7..8..9-10
El pseudocódigo debes incluirlo como comentarios en el programa de Python."""

"""PSEUDOCÓDIGO
Inicio
    Lee numero1
    Lee incremento
    Lee numero_total_serie
    
    Mientras (numero1 == 0) hacer
        Escribir ("El numero pedido debe ser mayor de 0.")
        Leer numero1
        
    Mientras (numero_total_serie == 0) hacer
        Escribir ("El numero total de la serie debe ser mayor de 0.")
        Leer numero_total_serie
    
    Serie = ""
    contador = numero_total_serie
    
    Si (numero1 > 0) y (numero_total_serie > 0) entonces 
        Mientras (contador != 0) hacer
            contador = contador - 1
            serie = numero1 + incremento
            
    Escribir serie
Fin
"""

#Inicio
#Lee numero1
numero_inicial = int(input("Introduce un número inicial: "))
#Lee incremento
incremento = int(input("Introduce el incremento que recibirá el número inicial: "))
#Lee numero_total_serie
numero_total_serie = int(input("Introcuce la cantidad de cifras que va a tener tu serie: "))   

#Mientras (numero1 == 0) hacer
while (numero_inicial == 0):
    #Escribir ("El numero pedido debe ser mayor de 0.")
    print("El numero pedido debe ser mayor de 0.")
    #Leer numero1
    numero1 = int(input("Introduce un número inicial: "))
    
#Mientras (numero_total_serie == 0) hacer
while (numero_total_serie == 0):
    #Escribir ("El numero total de la serie debe ser mayor de 0.")
    print("El numero total de la serie debe ser mayor de 0.")
    #Leer numero_total_serie
    numero_total_serie = int(input("Introcuce la cantidad de cifras que va a tener tu serie: "))   
    
numero1 = numero_inicial

#contador = numero_total_serie
contador = numero_total_serie

#Si (numero1 > 0) y (numero_total_serie > 0) entonces
if (numero_inicial > 0) and (numero_total_serie > 0): 
    #Serie = ""
    serie = ""
    #Para numero en (numero1..numero_total_serie) hacer
    while (contador != 0) : 
        #serie = numero1 + incremento
        contador -= 1
        serie =  serie + str(numero_inicial + incremento) + ".."
        numero_inicial += incremento     
        
print (f"{numero_inicial}-{serie}")       
    #Escribir serie
    #print (serie)

#Fin