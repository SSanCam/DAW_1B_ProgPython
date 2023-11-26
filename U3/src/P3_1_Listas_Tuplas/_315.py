"""Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas."""
def cuenta_atras() -> list:
    lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    lista_reves = []
    
    for numero in reversed(lista_numeros):
        lista_reves.append(numero)
    
    return lista_reves
    
    
def main():
    
    return print(cuenta_atras())
    
if __name__=="__main__":
    main()