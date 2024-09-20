from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo 
from maestros.maestro import Maestro
from materias.materia import Materia 
from datetime import datetime
from random import randint

class Escuela:
    def __init__(self):
        self.list_estudiantes: List[Estudiante] = []
        self.list_maestros: List[Maestro] = []
        self.list_grupos: List[Grupo] = []
        self.list_materias: List[Materia] = []

    def registrar_estudiante(self, estudiante: Estudiante):
        self.list_estudiantes.append(estudiante)

    def registrar_maestro(self, maestro: Maestro):
        self.list_maestros.append(maestro)
    
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
   