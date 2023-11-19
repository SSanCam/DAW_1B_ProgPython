"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario."""

def mostrar_notas(asignaturas: list, notas: list) -> str:
    
    for i in range(1,len(asignaturas)):
        asignatura = asignaturas[i]
        nota = notas[i]
        print(f"En {asignatura} has sacado: {nota}")   
            
    return notas 

def main(): 
    
    notas = []
    asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    
    for asignatura in asignaturas:
        
        nota = int(input(f"Que nota has sacado en {asignatura}: "))
        notas.append(nota)
        
    mostrar_notas(asignaturas, notas)
    
    
if __name__=="__main__":
    main()