class Materia:
    id_materia: str
    nombre:str
    descripcion: str
    semestre: int
    creditos: int

    def __init__(self, id_materia:str, nombre:str, descripcion:str, semestre:str, creditos:int):
        self.id_materia = id_materia
        self.nombre = nombre
        self.descripcion = descripcion
        self.semestre = semestre
        self.creditos = creditos

    def mostrar_info_materia(self):
        info = f"ID materia:  {self.id_materia}\nNombre: {self.nombre}\nDescripcion: {self.descripcion}\nSemestre: {self.semestre}\nCreditos: {self.creditos}\n"
        return info