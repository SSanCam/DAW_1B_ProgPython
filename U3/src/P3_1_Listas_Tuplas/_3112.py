"""Escribir un programa que almacene las matrices A=(123456) y B=(−100111) en una lista y muestre por pantalla su producto. Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista."""

def nueva_matriz(matriz1: list, matriz2: list) -> list: 
    
    matriz3 = [[],[],[]]
    
    for fila in range(3):
        for columna in range(2):
            
            matriz3[fila].append(matriz1[fila][columna] * matriz2[fila][columna])

    return  matriz3




def main():
    
    matriz1 = [[1,2],[3,4],[5,6]]
    matriz2 = [[1,0],[0,1],[1,1]]
    
    matriz3 = print(nueva_matriz(matriz1, matriz2))
    
    return matriz3

if __name__=="__main__":
    main()

"""
matriz1 =
matriz2= 
matriz3 = []

for fila in range(3):
    matriz3[fila].append(list)
    #crea el espacio en blanco
    for columna in range(2):
        matriz3[fila].append( matriz1[fila][columna] * matriz2[fila][columna] )
        #agrega el resultado de multiplicar las posiciones homonimas de las dos primeras matrices

la creacion de la lista de listas dice q es cutre
matriz3 = [[],[],[]]        
for fila in range(3):
    matriz3[fila].append(list)
#crea el espacio en blanco
    for columna in range(2):
        matriz3[fila].append( matriz1[fila][columna] * matriz2[fila][columna] )
        #agrega el resultado de multiplicar las posiciones homonimas de las dos primeras matrices
        
"""