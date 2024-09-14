from estudiante import Estudiante
from curso import Curso

curso1 = Curso("ProgramacionAv", 123, "Eder")
curso2 = Curso("Mecanica", 456, "Calderon")
curso3 = Curso("Mecanismos", 789, "José Gerardo")

estudiante1 = Estudiante("Alexis", 20, 1)
estudiante2 = Estudiante("Osvaldo", 24, 2)

estudiante1.agregar_curso(curso1)
estudiante2.agregar_curso(curso2)

def buscar_id(id_estudiante):
    if estudiante1.id_estudiante == id_estudiante:
        return estudiante1
    elif estudiante2.id_estudiante == id_estudiante:
        return estudiante2
    else:
        return

while True:
    print("---------------------------------------------")
    print("Elige una opcion")
    print("1. Mostrar datos de un alumno")
    print("2. Agregar Curso")
    print("3. Salir")
    print("---------------------------------------------")
    opcion = int(input("Elige una opcion: "))
    print("---------------------------------------------")
    
    if opcion == 1:
        id_estudiante = int(input("Intrduce el ID de algun estudiante: "))
        print("---------------------------------------------")
        estudiante_elegido = buscar_id(id_estudiante)
        if estudiante_elegido:
            estudiante_elegido.mostrar_info_estudiante()
        else:
            print("El estudiante no fue encontrado")
            
    elif opcion == 2:
        id_estudiante = int(input("Intrduce el ID de algun estudiante: "))
        print("---------------------------------------------")
        estudiante_elegido = buscar_id(id_estudiante)
        if estudiante_elegido:
            nombre_curso = input("Introduce el nombre del curso a agregar: ")
            instructor = input("Introduce el instructor del Curso: ")
            codigo_curso = int(input("Introduce el codigo del curso: "))
            nuevo_curso = Curso(nombre_curso, codigo_curso, instructor)
            estudiante_elegido.agregar_curso(nuevo_curso)
            
        else:
            print("El estudiante no fue localizado")
            
    elif opcion == 3:
        print("Saliste del programa")
        break
    
    else:
        print("Esta opcion no es valida, vuelve a intentarlo")
            