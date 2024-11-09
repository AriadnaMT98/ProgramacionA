from producto import Producto
from typing import List
from tkinter import messagebox

class Inventario:
    lista_productos: List[Producto]  = []

    def agregar_producto(self, producto:Producto):
         self.lista_productos.append(producto)

    def mostrar_productos(self):
        if not self.lista_productos:
            messagebox.showinfo("INVENTARIO", "El inventario está vacío.")
        else:
            productos_info = "\n".join([producto.mostrar_info() for producto in self.lista_productos])
            messagebox.showinfo("INVENTARIO", productos_info)
