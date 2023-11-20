"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> sobre cada una de las asignaturas de la lista."""

def yoEstudio():
    
    from  U3.src.P3_1_311 import almacenarAsignaturas
    
    return almacenarAsignaturas()


        
def main():
    
    matricula = yoEstudio()
    
    for asignatura in matricula :
       print (f"Yo estudio: {asignatura}")
    
if __name__=="__main__":
    main()
        