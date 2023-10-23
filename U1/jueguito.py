"""Pedir un numero entre -100..100
crear "piramide" donde cada linea sea serie_fila numeropedido = 0+1+2+3+..+numeropedido = suma de todos sus numeros"""

def jueguito ():
    numero_pedido = int(input("Introduce un numero entre -100 y 100: "))

    while (numero_pedido < -100 or numero_pedido > 100):
        numero_pedido = int(input("ERROR.\nDebes introducir un numero entre -100 y 100.\nIngresa otro número: "))
    
    suma = 0
    cont = 0 
    serie = ""
    
    while ( cont < numero_pedido):
        suma += cont
        serie = serie + str(cont) + " + "
        cont += 1
        
        if (cont == numero_pedido):
            suma += cont
            serie = serie + str(cont) + " = " + str(suma) + "\n"
            numero_pedido = numero_pedido -1
            cont = 0
            suma = 0
            
    return serie  
"""_____________________________________________________________________________________________________"""

print(jueguito())
