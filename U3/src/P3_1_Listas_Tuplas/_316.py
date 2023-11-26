"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir."""

def asignaturas_aprobadas(asignaturas: list) -> list:
    try:
                
        for asignatura in asignaturas[::-1]:
            
            print(f'Que nota has sacado en {asignatura}?')
            nota = int(input())
            
            if (nota >= 5):
                asignaturas.remove(asignatura)
                #del asignaturas[asignatura]
            
        print('Debes recuperar las siguientes asignaturas:\n')
        return asignaturas
    
    except Exception:
        return ('ERROR - 404')
    



def main():
    
    asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']

    suspendidas = asignaturas_aprobadas(asignaturas)
    
    return print(suspendidas)
    
if __name__=="__main__":
    main()