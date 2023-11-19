"""Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

limite numeros: 1-49
limite reintegro: 1-9
TAMPOCO PUDEN METERSE NUMEROS REPETIDOS 
"""

def pedir_numeros():
    
    try: 
        
        indice = 1
        numeros = []
        
        for num in range(6):
            numero = int(input(f'{indice}.- '))
            
            while (numero not in range(1,50) or (numero in numeros)):
                print('El numero debe ser entre 1-49 y no repetirse.')
                numero = int(input(f'{indice}.- '))
        
            numeros.append(numero)
            indice += 1
            
        numeros.sort()
        
        return numeros
        
    except Exception:
        
        return print('ERROR - 404')
        
def pedir_reintegro():
 
    try:

        reintegro = int(input('Reintegro -> '))
        
        while (reintegro <1 or reintegro > 9):
            print('Tu reintegro debe ser un numero entre 1-9.')
            reintegro = int(input('Reintegro -> '))
        
        return reintegro
        
    except Exception:
        print('ERROR - 404')

def main():

    print('Introduce los 6 numeros de tu boleto: ')
    numeros = pedir_numeros()
    
    print('Para tu reintegro, debes introducir un numero entre 1-9')
    reintegro = pedir_reintegro()
    
    resultado = print(f'Tu boleto ordenado es: {numeros} - R - {reintegro}')
    
    return (resultado)

if __name__=="__main__":
    main()
