"""Ejercicio 2.1.2
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas."""
def iniciarSesion(cadena: str):
    contraseña = "aytortilla"
    
    if (cadena.replace(" ","").lower() == contraseña):
        return ("Contraseña correcta!")
        
    else:
        return ("Contraseña incorrecta.")
        
        
def main():
    print("Introduce la contraseña: ")
    cadena =str(input())
    
    iniciarSesion(cadena)
        
if __name__=="__main__":
    main()