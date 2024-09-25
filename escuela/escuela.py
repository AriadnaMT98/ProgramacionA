from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo 
from maestros.maestro import Maestro
from materias.materia import Materia 
from datetime import datetime
from random import randint

class Escuela:
    list_estudiantes: List[Estudiante] = []
    list_maestros: List[Maestro] = []
    list_grupos: List[Grupo] = []
    list_materias: List[Materia] = []

    def registrar_estudiante(self, estudiante: Estudiante):
        self.list_estudiantes.append(estudiante)

    def registrar_maestro(self, maestro: Maestro):
        self.list_maestros.append(maestro)

    def registar_materia(self, materia: Materia):
        self.list_materias.append(materia)
    
    def listar_estudiantes(self):
        print("\n** ESTUDIANTES **\n")

        for estudiante in self.list_estudiantes:
            print(estudiante.mostrar_info_estudiante())

    def listar_maestros(self):
        print("\n** MAESTROS **\n")

        for maestro in self.list_maestros:
            print(maestro.mostrar_info_maestro())

    def listar_materias(self):
        print("\n** MATERIAS **\n")

        for materias in self.list_materias:
            print(materias.mostrar_info_materia())

    def eliminar_estudiante(self, numero_control: str):
        for estudiante in self.list_estudiantes:
            if estudiante.numero_control == numero_control:
                self.list_estudiantes.remove(estudiante)
                print("Estudiante eliminado\n")
                return
        print(f"No se encontro el estudiante con numero de control: {numero_control}\n")

    def eliminar_maestro(self, numero_control: str):
        for maestro in self.list_maestros:
            if maestro.numero_control == numero_control:
                self.list_maestros.remove(maestro)
                print("Maestro eliminado\n")
                return
        print(f"No se encontro el maestro con numero de control: {numero_control}\n")

    def eliminar_materia(self, id_materia: str):
        for materia in self.list_materias:
            if materia.id_materia == id_materia:
                self.list_materias.remove(materia)
                print("Materia eliminada\n")
                return
        print(f"No se encontro la materia con ID: {id_materia}\n")

    def generar_numero_control_estudiante(self):
        ano = datetime.now().year
        mes = datetime.now().month
        longitud_mas_uno = len(self.list_estudiantes) + 1
        aleatorio = randint(0, 10000)
        numero_control = f"L{ano}{mes}{longitud_mas_uno}{aleatorio}"
        return numero_control
    
    def generar_numero_control_maestro(self, maestro: Maestro):
        ano_nacimiento = maestro.ano_nacimiento
        dia = datetime.now().day
        aleatorio = randint(500, 5000)
        dos_letras_nombre = maestro.nombre[:2].upper()
        dos_letras_rfc = maestro.rfc[-2:].upper()
        longitud_maestros = len(self.list_maestros) + 1
        
        numero_control = f"M{ano_nacimiento}{dia}{aleatorio}{dos_letras_nombre}{dos_letras_rfc}{longitud_maestros}"
        return numero_control

    def generar_id_materia(self, materia: Materia):
        dos_digitos_nombre = materia.nombre[-2:].upper()
        semestre = materia.semestre
        cantidad_creditos = materia.creditos
        aleatorio = randint(1, 1000)

        id_materia = f"MT{dos_digitos_nombre}{semestre}{cantidad_creditos}{aleatorio}"
        return id_materia

        
   