"""Ejercicios 1.30
Realiza un algoritmo con PSEUDOCÓDIGO y pásalo a un programa en Python que pida un número de inicio, 
un incremento y un total de la serie.
El incremento y el total deben ser mayor que cero, sino el programa debe finalizar con un error u 
obligar a que introduzcan un valor correcto de ambos (os lo dejo a vuestra elección, la primera opción es más fácil, 
aunque el mundo está lleno de valientes)
Por ejemplo, si introducen los valores 1, 1 y 10, el programa mostrará en consola exactamente 
lo siguiente: SERIE => 1-2..3..4..5..6..7..8..9-10
El pseudocódigo debes incluirlo como comentarios en el programa de Python."""

"""PSEUDOCÓDIGO
Inicio
    Lee numero_inicio
    Lee incremento
    Lee numero_total_serie
    
    Mientras (numero_inicio <= 0) hacer
        Escribir ("El numero pedido debe ser mayor de 0.")
        Leer numero_inicio
        
    Mientras (numero_total_serie <= 0) hacer
        Escribir ("El numero total de la serie debe ser mayor de 0.")
        Leer numero_total_serie
    
    Serie = str(numero_inicio)
    contador = numero_total_serie - 1
    
    Si (numero_inicio > 0) y (numero_total_serie > 0) entonces 
        Mientras (contador != 0) hacer
            contador = contador - 1
            numero_inicio + incremento
            serie = serie + (numero + incremento)
            
    ultimo numero = numero_total_serie + incremento  
    serie = serie + "-" + ultimo_numero
         
    Escribir serie
Fin
"""

# Inicio
# Lee numero_inicio
numero_inicio = int(input("Introduce el número con el que comenzará la serie: "))
# Lee incremento
incremento = int(input("Introduce la cantidad a incrementar en cada número de la serie: "))
# Lee numero_total_serie
numero_total_serie = int(input("Introduce cuántas cifras tendrá en total tu serie: "))

# Mientras (numero_inicio <= 0) hacer
while numero_inicio <= 0:
    # Escribir "El número pedido debe ser mayor de 0."
    print("El número pedido debe ser mayor de 0.")
    # Leer numero_inicio
    numero_inicio = int(input("Introduce el número con el que comenzará la serie: "))

# Mientras (numero_total_serie <= 0) hacer
while numero_total_serie <= 0:
    # Escribir "El número total de la serie debe ser mayor de 0."
    print("El número total de la serie debe ser mayor de 0.")
    # Leer numero_total_serie
    numero_total_serie = int(input("Introduce cuántas cifras tendrá en total tu serie: "))

# Serie = str(numero_inicio)
serie = str(numero_inicio) + "-"
# contador = numero_total_serie
contador = (numero_total_serie - 1)

# Si (numero_inicio > 0) y (numero_total_serie > 0) entonces
if numero_inicio > 0 and numero_total_serie > 0:
    # Mientras (contador != 1) hacer
    while contador != 1:
        #contador = contador - 1
        contador -= 1
        #numero_inicio = numero_inicio + incremento
        numero_inicio += incremento
        serie = serie + str(numero_inicio) + ".." 
    # Agrega el último número
    ultimo_numero = numero_inicio + incremento
    #serie = serie + ultimo_numero
    serie = serie[:-2] + "-" + str(ultimo_numero)

# Escribir serie
print(serie)
# Fin
