from curso import Curso

class Estudiante:
    nombre = ""
    edad = 0
    id_estudiante = 0
    curso = []
    
    def __init__(self, nombre, edad, id_estudiante):
        self.nombre = nombre
        self.edad = edad
        self.id_estudiante = id_estudiante
        self.cursos = []
        
    def agregar_curso(self, agregar_curso):
        self.cursos.append(agregar_curso)
           
    def mostrar_info_estudiante(self):
        print("Nombre: ", self.nombre, "\nEdad: ", self.edad, "\nID del Estudiante: ", self.id_estudiante)
        
        if self.cursos:
            print("Cursos: ")
            for curso in self.cursos:
                curso.mostrar_info_curso()
                
        else:
            print("No tiene cursos asignados")
                
                