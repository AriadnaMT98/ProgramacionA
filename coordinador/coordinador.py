from usuario.usuario import Usuario
from usuario.utils.roles import Rol

class Coordinador(Usuario):
    sueldo: str
    rfc: str
    anios_antiguedad: int

    def __init__(self, numero_control:str, nombre: str, apellido:str, sueldo:str, rfc: str, anios_antiguedad: int, contrasenia: str):
        super().__init__(numero_control=numero_control, nombre=nombre, apellido=apellido, contrasenia=contrasenia, rol=Rol.COORDINADOR)
        self.sueldo = sueldo
        self.rfc = rfc
        self.anios_antiguedad = anios_antiguedad

    def mostrar_info_coordinador(numero_control):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info = f"Numero de control:  {self.numero_control}\nNombre completo: {nombre_completo}\nSueldo: {self.sueldo}\nRFC: {self.rfc}\nAños de antigüedad: {self.anios_antiguedad}\nRol: {self.rol}\n"
        return info