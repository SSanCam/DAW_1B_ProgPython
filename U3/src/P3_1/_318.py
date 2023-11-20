"""Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo."""

def pasa_palindromo(palabra: str) -> str:
    
    try:

        if (palabra[::-1] == palabra):
            palindromo = 'Tu palabra es un palindromo.'
            return palindromo
        
        else:
            no_palindromo = 'Tu palabra no es palindromo'
            
        return no_palindromo
    
    except ValueError:
        return ('ERROR - 404')
    
    
def main():
    try:
        print('introduce una palabra: ')
        palabra = str(input())
        
        palindromo = pasa_palindromo(palabra)
        
        return print(palindromo)
        
    except Exception:
        return ('ERROR - 404')
    
if __name__=="__main__":
    main()