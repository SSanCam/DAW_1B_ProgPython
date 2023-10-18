"""
Escribe un programa en Python que lea una palabra y la encripte:

    1. Pedir la palabra hasta que cumpla que tiene un mínimo de 8 letras.
    
    2. Después, transformar o encriptar la palabra de la siguiente manera:
        - Sin bucles, pero escribiendo varias instrucciones si lo necesitáis.
        - Eliminar espacios.
        - Consonantes a mayúsculas
        - La vocal a pasa a ser una @.
        - La vocal e pasa a ser un 3.
        - La vocal i pasa a ser un 1.
        - El resto de vocales serán minúsculas.
        - Si tiene solo 8 letras, añade un * al principio y un # al final.

    3. Ejemplos:

    > Introduzca una palabra: Pedro PAblO    1984
    > Su palabra encriptada es P3DRoP@BLo1984

    > Introduzca una palabra: ArIADNa2
    > Su palabra encriptada es *@R1@DN@2#

    > Introduzca una palabra: USER       89
    > Introduzca una palabra *mínimo 8 letras*: USER  893465
    > Su palabra encriptada es uS3R893465

"""
palabra_pedida = str(input("Introduce una palabra de 8 letras: "))

while len(palabra_pedida) != 8:
    palabra_pedida = str(input("ERROR.\nDebes introducir una palabra de 8 letras: "))
    
#- Consonantes a mayúsculas //PASO TODO A MAYÚSCULAS PARA QUE SEA MÁS FÁCIL CONTROLAR LUEGO LAS DOS VOCALES RESTANTES.
palabra_pedida.upper()
"""
- La vocal a pasa a ser una @.
- La vocal e pasa a ser un 3.
- La vocal i pasa a ser un 1.
"""
palabra_formateada = (((palabra_pedida.replace("A","@")).replace("E","3")).replace("I","1"))

#- El resto de vocales serán minúsculas.
palabra_encriptada = (palabra_formateada.replace("O","o")).replace("U","u")

#- Si tiene solo 8 letras, añade un * al principio y un # al final.
if len(palabra_encriptada) == 8 :
    print(f"Tu palabra encriptada es: *{palabra_encriptada}#")