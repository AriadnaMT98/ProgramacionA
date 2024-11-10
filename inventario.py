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
            productos_info = ""
            total = 0
            for producto in self.lista_productos:
                productos_info += producto.mostrar_info() 
                total += producto.valor_total()  
            mensaje = f"{productos_info}\nValor total del inventario: {total}"
            messagebox.showinfo("INVENTARIO", mensaje)
        