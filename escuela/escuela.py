from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo 
from usuario.usuario import Usuario
from maestros.maestro import Maestro
from coordinador.coordinador import Coordinador
from materias.materia import Materia 
from carrera.carrera import Carrera
from semestre.semestre import Semestre
from datetime import datetime
from random import randint

class Escuela:
    lista_usuarios: List[Usuario] = []
    lista_estudiantes: List[Estudiante] = []
    lista_maestros: List[Maestro] = []
    lista_grupos: List[Grupo] = []
    lista_materias: List[Materia] = []
    lista_carreras: List[Carrera] = []
    lista_semestres: List[Semestre] = []
    lista_coordinadores: List[Coordinador] = []

    def __init__(self):
        coordinador = Coordinador(numero_control="12345", nombre="Edson", apellido="Medina", rfc="MEDINA123", sueldo=100000, anios_antiguedad=10, contrasenia="123*")
 
        self.lista_usuarios.append(coordinador)
        self.lista_coordinadores.append(coordinador)

    def registrar_estudiante(self, estudiante: Estudiante):
        self.lista_usuarios.append(estudiante)
        self.lista_estudiantes.append(estudiante)

    def registrar_maestro(self, maestro: Maestro):
        self.lista_usuarios.append(maestro)
        self.lista_maestros.append(maestro)

    def registrar_coordinador(self, coordinador: Coordinador):
        self.lista_usuarios.append(coordinador)
        self.lista_coordinadores.append(coordinador)

    def registrar_materia(self, materia: Materia):
        self.lista_materias.append(materia)

    def registrar_carrera(self, carrera:Carrera):
        self.lista_carreras.append(carrera)

    def registrar_grupo (self, grupo: Grupo):
        id_semestre = grupo.id_semestre

        for semestre in self.lista_semestres:
            if semestre.id_semestre == id_semestre:
                semestre.registrar_grupo_en_semestre(grupo=grupo)
                break

        self.lista_grupos.append(grupo)

    def registrar_semestre(self, semestre:Semestre):
        id_carrera = semestre.id_semestre

        for carrera in self.lista_carreras:
            if carrera.matricula == id_carrera:
                carrera.registrar_semestre(semestre=semestre)
                break

        self.lista_semestres.append(semestre)
    
    def listar_estudiantes(self):
        print("\n** ESTUDIANTES **\n")

        for estudiante in self.lista_estudiantes:
            print(estudiante.mostrar_info_estudiante())

    def listar_maestros(self):
        print("\n** MAESTROS **\n")

        for maestro in self.lista_maestros:
            print(maestro.mostrar_info_maestro())

    def listar_materias(self):
        print("\n** MATERIAS **\n")

        for materias in self.lista_materias:
            print(materias.mostrar_info_materia())

    def listar_grupos(self):
        print("\n** GRUPOS **\n")

        for grupo in self.lista_grupos:
            print(grupo.mostrar_info_grupo())

    def listar_carrera(self):
        print("\n** CARRERAS **\n")

        for carrera in self.lista_carreras:
            print(carrera.mostrar_info_carrera())

    def listar_semestre(self):
        print("\n** SEMESTRES **\n")

        for semestre in self.lista_semestres:
            print(semestre.mostrar_info_semestre())

    def eliminar_estudiante(self, numero_control: str):
        for estudiante in self.lista_estudiantes:
            if estudiante.numero_control == numero_control:
                self.lista_estudiantes.remove(estudiante)
                print("Estudiante eliminado")
                return
        print(f"No se encontro el estudiante con numero de control: {numero_control}")

    def eliminar_maestro(self, numero_control: str):
        for maestro in self.lista_maestros:
            if maestro.numero_control == numero_control:
                self.lista_maestros.remove(maestro)
                print("Maestro eliminado")
                return
        print(f"No se encontro el maestro con numero de control: {numero_control}")

    def eliminar_materia(self, id_materia: str):
        for materia in self.lista_materias:
            if materia.id_materia == id_materia:
                self.lista_materias.remove(materia)
                print("Materia eliminada")
                return
        print(f"No se encontro la materia con ID: {id_materia}")

    def generar_numero_control_estudiante(self):
        ano = datetime.now().year
        mes = datetime.now().month
        longitud_mas_uno = len(self.lista_estudiantes) + 1
        aleatorio = randint(0, 10000)
        numero_control = f"L{ano}{mes}{longitud_mas_uno}{aleatorio}"
        return numero_control
    
    def generar_numero_control_maestro(self, maestro: Maestro):
        ano_nacimiento = maestro.ano_nacimiento
        dia = datetime.now().day
        aleatorio = randint(500, 5000)
        dos_letras_nombre = maestro.nombre[:2].upper()
        dos_letras_rfc = maestro.rfc[-2:].upper()
        longitud_maestros = len(self.lista_maestros) + 1
        
        numero_control = f"M{ano_nacimiento}{dia}{aleatorio}{dos_letras_nombre}{dos_letras_rfc}{longitud_maestros}"
        return numero_control

    def validar_inicio_sesion(self,numero_control: str, contrasenia: str):
        for usuario in self.lista_usuarios:
            if usuario.numero_control == numero_control:
                if usuario.contrasenia == contrasenia:
                    return usuario
        
        return None

    def generar_id_materia(self, materia: Materia):
        dos_digitos_nombre = materia.nombre[-2:].upper()
        semestre = materia.semestre
        cantidad_creditos = materia.creditos
        aleatorio = randint(1, 1000)

        id_materia = f"MT{dos_digitos_nombre}{semestre}{cantidad_creditos}{aleatorio}"
        return id_materia


        
   