"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla."""
def almacenarAsignaturas ():
    
    listaAsignaturas = ("Matemáticas", "Física", "Química", "Historia", "Lengua")
    
    return listaAsignaturas
        
def main():
    
   asignaturas = almacenarAsignaturas()
   
   for asignatura in asignaturas :
       print (asignatura)

    
if __name__=="__main__":
    main()