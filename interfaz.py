import tkinter as tk
from tkinter import messagebox
from producto import Producto
from inventario import Inventario
from excepciones import MiError, escirbirNombre, escirbirPrecio, escirbirCantidad

inventario = Inventario()

def registrar():
    try:
        nombre = str(nombre_in.get())
        escirbirNombre(nombre)
        precio = float(precio_in.get())
        escirbirPrecio(precio)
        cantidad = int(cantidad_in.get())
        escirbirCantidad(cantidad)
        producto = Producto(nombre=nombre, precio=precio, cantidad=cantidad)
        inventario.agregar_producto(producto)

        messagebox.showinfo("INFORMACION DEL PRODUCTO", producto.mostrar_info())
        
    except MiError as e:
        messagebox.showerror("Error", e.mensaje)

def mostrar_inventario():
    inventario.mostrar_productos()


ventana = tk.Tk()
ventana.title("PRODUCTO")
ventana.geometry("423x200")
 
nombre = tk.Label(ventana, text="Nombre del producto:", bg="lightblue", fg="black", font=("Arial", 11, "bold"), relief="sunken", padx=10, pady=10)
nombre.grid(row=0, column=0)
nombre_in = tk.Entry(ventana)
nombre_in.grid(row=0, column=1)

precio = tk.Label(ventana, text="Precio del producto:", bg="lightblue", fg="black", font=("Arial", 11, "bold"), relief="sunken", padx=10, pady=10)
precio.grid(row=1, column=0)
precio_in = tk.Entry(ventana)
precio_in.grid(row=1, column=1)

cantidad = tk.Label(ventana, text="Cantidad del producto:", bg="lightblue", fg="black", font=("Arial", 11, "bold"), relief="sunken", padx=10, pady=10)
cantidad.grid(row=2, column=0)
cantidad_in = tk.Entry(ventana)
cantidad_in.grid(row=2, column=1)

boton_registrar = tk.Button(ventana, text="Registrar", command=registrar, bg="lightgreen", font=("Arial", 11, "bold"))
boton_registrar.grid(row=3, column=1)

boton_inventario = tk.Button(ventana, text="Inventario", command=mostrar_inventario, bg="lightgreen", font=("Arial", 11, "bold"))
boton_inventario.grid(row=4, column=1)


ventana.mainloop()

