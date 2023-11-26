"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> sobre cada una de las asignaturas de la lista."""

def yo_estudio(asignatura: str):
    return (f"Yo estudio: {asignatura}")    


def main():
    
    asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    estudio = ""
    
    for asignatura in asignaturas:
        estudio = estudio + yo_estudio(asignatura) + '\n'
    print(estudio)

    
if __name__=="__main__":
    main()
    
