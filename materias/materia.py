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