from usuario.usuario import Usuario
from usuario.utils.roles import Rol

class Maestro(Usuario):
    ano_nacimiento: int
    rfc:str
    sueldo:float

    def __init__(self, numero_control:str, nombre:str, ano_nacimiento: int, apellido:str, rfc:str, sueldo:float, contrasenia:str):
        super().__init__(numero_control=numero_control, nombre=nombre, apellido=apellido, contrasenia=contrasenia, rol=Rol.MAESTRO)
        self.ano_nacimiento = ano_nacimiento
        self.rfc = rfc
        self.sueldo = sueldo
    
    def mostrar_info_maestro(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info = f"Numero de control:  {self.numero_control}\nNombre completo: {nombre_completo}\nAño de nacimiento: {self.ano_nacimiento}\nRFC: {self.rfc}\nSueldo: {self.sueldo}\nRol: {self.rol}\n"
        return info