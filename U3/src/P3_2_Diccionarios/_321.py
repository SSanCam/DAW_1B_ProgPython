"""Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario."""

def divisa(simbolo: str) -> str :
    try:
        divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
        
        if (simbolo in divisas):
            return (divisas[simbolo])
        
        if (simbolo not in divisas):
            return 'Esa divisa no la conocemos.'
        
        else:
            raise ValueError ('ERROR - 404')
        
    except Exception:
        print('ERROR - 404')
        
        
        
def main():
    
    print('De que divisa quieres ver el simbolo?: ')
    simbolo_divisa = input().title()
    
    return print(divisa(simbolo_divisa))
    
if __name__=="__main__":
    main()