class Maestro:
    numero_control:str
    nombre: str
    apellido: str
    ano_nacimiento: int
    rfc:str
    sueldo:float

    def __init__(self, numero_control:str, nombre:str, ano_nacimiento: int, apellido:str, rfc:str, sueldo:float):
        self.numero_control = numero_control
        self.nombre = nombre
        self.ano_nacimiento = ano_nacimiento
        self.apellido = apellido
        self.rfc = rfc
        self.sueldo = sueldo
    