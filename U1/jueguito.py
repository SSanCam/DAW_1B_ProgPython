"""Pedir un numero entre -100..100
crear "piramide" donde cada linea sea serie_fila numeropedido = 0+1+2+3+..+numeropedido = suma de todos sus numeros"""

def jueguito ():
    numero_pedido = int(input("Introduce un numero entre -100 y 100: "))

    while (numero_pedido < -100 or numero_pedido > 100):
        numero_pedido = int(input("ERROR.\nDebes introducir un numero entre -100 y 100.\nIngresa otro número: "))
    #INICIALIZO LAS VARIABLES
    suma = 0
    cont = 0 
    serie = ""
    
    while ( cont < numero_pedido):
        #COMIENZA A CREARSE EL PRIMER NIVEL DE LA SERIE:
        suma += cont
        serie = serie + str(cont) + " + "
        cont += 1
                
        if (cont == numero_pedido):
            #SI EL NIVEL ACABA LA SERIE, ACABA CON LA SUMA DE LOS NUMEROS Y UNA TABULACION PARA EL SIGUIENTE NIVEL, SI LO HUBIESE.
            suma += cont
            serie = serie + str(cont) + " = " + str(suma) + "\n"
            fin_serie = "0 + 0 = 0"
            
            #SI NO HA LLEGADO AL NIVEL FINAL, REINICIO VARIABLES Y ACTUALIZO EL VALOR DEL NUMERO PEDIDO
            numero_pedido = numero_pedido -1
            cont = 0
            suma = 0
            serie_completa = serie + fin_serie
            
    return serie_completa  
"""_____________________________________________________________________________________________________"""

print(jueguito())
