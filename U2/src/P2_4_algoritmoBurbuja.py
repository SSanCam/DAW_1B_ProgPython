def ordenacionAlgoritmoBurbuja(listaNumeros: list) -> list:
    #HAY QUE AGREGAR DOS NUEVAS VARIABLES QUE VAYAN PILLANDO LOS VALORES ITERATIVOS DE i Y j 
    #PARA PODER HACER LA COMPARACION DE VALORES Y ORDENARLOS 
    
    cont = len(listaNumeros)
    cadenaLista = str(listaNumeros)
    
    for buclePadre in range(1,len(listaNumeros)):
        

    return listaNumeros



def main():
    
    try:
        
        lista_numeros = []
        numero = int(input("Ingresa todos los numeros enteros positivos que quieres incluir en la lista.\nIngresa 0 para finalizar:  "))
        
        while (numero != 0):
            numero = int(input())
            lista_numeros.append(numero)
            
        resultado = ordenacionAlgoritmoBurbuja(lista_numeros)
        return print(resultado)
    
    except Exception:
        return "ERROR - 404"
    
    
if __name__=="__main__":
    main()