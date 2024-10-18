from typing import List
from estudiantes.estudiante import Estudiante
from materias.materia import Materia
from random import randint

class Grupo:
    id_grupo: str
    estudiantes: List[Estudiante] = []
    materia: List[Materia] = []
    tipo: chr 
    id_semestre: str

    def __init__(self, tipo: chr, id_semestre: str):
        self.id_grupo = self.generar_id(tipo)
        self.tipo = tipo
        self.id_semestre = id_semestre
        
    def generar_id(self, tipo: chr) -> str:
        return f"{tipo}-{randint(0,10000000)}-{randint(0,100000)}"

    def mostrar_info_grupo(self):
        info = f"ID del grupo:  {self.id_grupo}\nTipo: {self.tipo}\nID del semestre: {self.id_semestre}\n"
        return info

    def registrar_estudiante(self, estudiante:Estudiante):
        estudiantes.append(estudiante)

    def registrar_materia(self, materia:Materia):
        materias.append(materia)

    def mostrar_info_grupo_para_estudiante(self):
        print(f"\nInformacion del Grupo {self.tipo}, del semestre {self.id_semestre}")

        for materias in self.materias:
            print(materia.mostrar_info_materia)
