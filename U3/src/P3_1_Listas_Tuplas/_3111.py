"""Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) 
en dos listas y muestre por pantalla su producto escalar."""

def producto_escalar(vector1: list, vector2: list) -> list:
    try:
        vector3 = []
        pos = 0 
        
        for i in range(3):
            vector3.append(vector1[pos] * vector2[pos])
            pos += 1

        return vector3
    except Exception:
        return ('ERROR - 404')

def main():
    
    vector_1 = [1,2,3]
    vector_2 = [4,5,6]
    
    vector_3 = print(producto_escalar(vector_1, vector_2))
    
    return vector_3

if __name__=="__main__":
    main()