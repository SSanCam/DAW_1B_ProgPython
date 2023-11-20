"""Escribir un programa que almacene el abecedario en una lista, 
elimine de la lista las letras que ocupen posiciones múltiplos de 3, 
y muestre por pantalla la lista resultante."""

def abecedario():
    
    try:
        
        abecedario = [chr(i) for i in range(ord('a'), ord('z')+1)]

        for letra in abecedario[::3]:
            abecedario.remove(letra)
            
        return abecedario
        
    except Exception:
        return ('ERROR - 404')
    
    
    
def main():
    
    abc_mult_3 = abecedario()
    
    return print(abc_mult_3)
    
if __name__=="__main__":
    main()