"""Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

limite numeros: 1-49
limite reintegro: 1-9
TAMPOCO PUDEN METERSE NUMEROS REPETIDOS 

"""
def pedir_numeros(lista_numeros) -> list:
    
    try:
        lista_numeros = []
        cont = 1
        print("Introduce los números de tu boleto: ")
        
        for num in range(1,7):
            
            numero = int(input(f"{cont}.- " ))
            lista_numeros.append(numero)
            
            while (numero not in range(1,50)) and (numero not in lista_numeros):
                numero = int(input(f"{cont}: "))
                
                lista_numeros.append(numero)
            cont += 1
            
        return print(lista_numeros)
    
    except ValueError: 
        print("**ERROR**")
    
    return lista_numeros
############################################################################
def pedir_reintegro():

    try:
        
        print("Introduce tu reintegro: ")
        reintegro = int(input())
        
        while (reintegro not in range(1,10)):
            reintegro = int(input("Debes introducir un numero entre 1-9: "))

        return reintegro
    
    except ValueError:
        print("**ERROR**")
    
############################################################################
def loteria_primitiva(lista_numeros: list, reintegro: int) -> str:
    
    lista_numeros.sort()
    orden_boleto = print(f"Tu boleto ordenado es: {lista_numeros.sort()} - {reintegro}")
    
    return (orden_boleto)

############################################################################
def main():
    
    try:

        resultado = loteria_primitiva(pedir_numeros(), pedir_reintegro())
        
        return resultado
        
                
    except ValueError :
        print("Error.")
    
    
if __name__=="__main__":
    main()
    