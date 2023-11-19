"""Escribe un bucle while que comience con el último carácter en la cadena y 
haga un recorrido hacia atrás hasta el primer carácter en la cadena, 
imprimiendo cada letra en una línea independiente"""

def cadena_reves(cadena: str) -> str:
    import os 
    def clear_terminal():
        os.system('cls')
    
    clear_terminal()
    try :
        resultado = ''
        
        for letra in cadena[::-1]:
            resultado = resultado + letra + '\n'
            
        return resultado
         
    except Exception:
        return ('ERROR - 404')

print(cadena_reves('banana'))