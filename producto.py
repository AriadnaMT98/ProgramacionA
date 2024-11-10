class Producto:
    nombre: str
    precio: float
    cantidad: int
    valor_total: float

    def __init__(self, nombre: str, precio: float, cantidad: int):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def valor_total(self):
        total = self.precio * self.cantidad
        return total

    def mostrar_info(self):
        info=(f"\nNombre del producto:  {self.nombre}\nPrecio del producto: {self.precio}\nCantidad de producto: {self.cantidad}\nValor total: {self.valor_total()}\n")
        return info