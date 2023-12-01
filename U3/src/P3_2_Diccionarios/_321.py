"""Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario."""

def divisa(simbolo: str) -> str :
    try:
        divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
        
        if (simbolo in divisas):
            return (divisas[simbolo])

    except KeyError:
        return 'ERROR - 404'
        
def main():
    
    dato_correcto = True 
    
    while dato_correcto:
        
        print('De qué divisa quieres ver el símbolo?(No se permiten números): ')
        simbolo_divisa = input().title()
        dato_correcto = True
        
        try:
            float(simbolo_divisa)
            
        except ValueError:
            
            if (simbolo_divisa.strip() == ''):
                print('Por favor, ingresa un valor no vacío.')
            else:
                print('No tenemos ésa divisa en nuestra base de datos.\nInténtelo de nuevo: ')

        
    return print(divisa(simbolo_divisa))
    
if __name__=="__main__":
    main()