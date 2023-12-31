"""
Crea un algoritmo en pseudocódigo y pásalo también a un programa en Python que pida los días totales trabajados en la vida laboral y te transforme esos días a años, meses y días.

Para este programa vamos a considerar que todos los años tienen 360
 días y todos los meses 30 días.

Debe cumplir lo siguiente:

- La palabra año, mes y día irá en plural o singular dependiendo de su cantidad.

- No puede introducir un valor negativo para los días. Si lo hace, debéis dar un mensaje de error y volver a pedir los días trabajados hasta que introduzca un número positivo (el 0 también es válido).

Ejemplo 1:

> Introduzca los días trabajados: 1347
> Ha cotizado 3 años, 8 meses y 12 días.

Ejemplo 2:

> Introduzca los días trabajados: 31
> Ha cotizado 0 años, 1 mes y 1 día.

Ejemplo 3:

> Introduzca los días trabajados: -230
> *** Error - el valor no puede ser negativo ***
> Introduzca los días trabajados: -33
> *** Error - el valor no puede ser negativo ***
> Introduzca los días trabajados: 0
> Ha cotizado 0 años, 0 meses y 0 días.


Inicio

    
Fin
"""
dias = int(input("Introduce los dias totales que has trabajado: "))

#Voy a pedir número de días hasta que tenga un número positivo
while (dias < 0 ):
    dias = int(input("ERROR.\nDebes introducir valores positivos a partir de 0: "))

if (dias >= 0):
    #años completos
    anios = dias // 360

    #meses completos
    meses = (dias % 360
    ) // 30
    #dias restantes
    dias = (dias % 360
    )  % 30
    
    if (dias == 30):  
        meses += 1
        dias -= 30
        
    if (meses == 12):
        anios += 1
        meses -= 12
    
        
#Plural / singular segun el numero 
#dias
if (dias == 1):
    dia_plusing = "día"
else:
    dia_plusing = "días"
    
#meses
if (meses == 1):
    mes_plusing = "mes"
else:
    mes_plusing = "meses"
    
#año
if (anios == 1):
    annos_plusing = "año"
else:
    annos_plusing = "años"
    
print(f"Ha cotizado {anios} {annos_plusing}, {meses} {mes_plusing} y {dias} {dia_plusing}.")