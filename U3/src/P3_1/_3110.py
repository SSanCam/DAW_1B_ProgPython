"""Escribir un programa que almacene en una lista los siguientes precios: 
50, 75, 46, 22, 80, 65, 8 y muestre por pantalla el menor y el mayor de los precios."""

def lista_precios(precios: list) -> str:
    
    min_precio = min(precios)
    max_precio = max(precios)
    
    resultado = f'El numero mayor es {max_precio} y el menor {min_precio}'
    
    return resultado
    
    
    
def main():
    
    precios = [50, 75, 46, 22, 80, 65, 8]
    
    max_min = lista_precios(precios)
    
    return print(max_min)


if __name__=="__main__":
    main()