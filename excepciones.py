class MiError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def escirbirNombre(nombre):
    if(nombre == ""):
        raise MiError("No se puede registar, ingrese el nombre")
    
def escirbirPrecio(precio):
    if(precio <= 0):
        raise MiError("No se puede registar, el precio debe de ser mayor a 0")
    
def escirbirCantidad(cantidad):
    if(cantidad < 0):
        raise MiError("No se puede registar, la cantidad no puede ser negativa")
