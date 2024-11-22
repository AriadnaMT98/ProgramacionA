import tkinter as tk
import mysql.connector
from tkinter import ttk,messagebox
from tkinter import *
 
 
def show():
    print("hola")

def mostrar():
    mysqlC = mysql.connector.connect(host="localhost", user="root", password="", database= "proyecto")
    micursos = mysqlC.cursor()
    micursos.execute("select * from libros")
    lista = micursos.fetchall()

    for i in listbox.get_children():
            listbox.delete(i)

    for i,(id, titulo, autor, editorial, año_publicacion, precio) in enumerate(lista, start=1):
        listbox.insert("", "end", values=(id, titulo, autor, editorial, año_publicacion, precio))
    mysqlC.close()

def actualizar():
    for i in listbox.get_children():
        listbox.delete(i)
    mostrar()

def add():
    tituloAdd = titulo.get()
    autorAdd = autor.get()
    editorialAdd = editorial.get()
    año_publicacionAdd = año_publicacion.get()
    precioAdd = precio.get()
    mysqlC = mysql.connector.connect(host="localhost", user="root", password="", database= "proyecto")
    micursos = mysqlC.cursor()
    try:
        micursos.execute(f"insert into libros(titulo, autor, editorial, año_publicacion, precio) values('{tituloAdd}','{autorAdd}','{editorialAdd}','{año_publicacionAdd}','{precioAdd}')")
        mysqlC.commit()
        titulo.delete(0,END)
        autor.delete(0,END)
        editorial.delete(0,END)
        año_publicacion.delete(0,END)
        precio.delete(0,END)
        messagebox.showinfo("informacion", "libro agregado")
        actualizar()

    except Exception as e:
        print(e)
        mysqlC.rollback()
        mysqlC.close()

def delete():
    seleccion = listbox.selection() 
    if seleccion:
        identificador = listbox.item(seleccion[0], "values")[0]

    mysqlC = mysql.connector.connect(host="localhost", user="root", password="", database= "proyecto")
    micursos = mysqlC.cursor()
    
    try:
        micursos.execute(f"DELETE FROM LIBROS WHERE id={identificador}")
        mysqlC.commit()
        titulo.delete(0,END)
        autor.delete(0,END)
        editorial.delete(0,END)
        año_publicacion.delete(0,END)
        precio.delete(0,END)
        messagebox.showinfo("informacion", "libro eliminado")
        actualizar()
    except Exception as e:
        print(e)
        mysqlC.rollback()
        mysqlC.close()

def edit():
    seleccion = listbox.selection()
    if seleccion:
        identificador = listbox.item(seleccion[0], "values")[0]

    tituloAdd = titulo.get()
    autorAdd = autor.get()
    editorialAdd = editorial.get()
    año_publicacionAdd = año_publicacion.get()
    precioAdd = precio.get()
    mysqlC = mysql.connector.connect(host="localhost", user="root", password="", database= "proyecto")
    micursos = mysqlC.cursor()
    try:
        micursos.execute(f"UPDATE libros set titulo='{tituloAdd}', autor='{autorAdd}', editorial ='{editorialAdd}', año_publicacion='{año_publicacionAdd}', precio='{precioAdd}' where id={identificador}")
        mysqlC.commit()
        titulo.delete(0,END)
        autor.delete(0,END)
        editorial.delete(0,END)
        año_publicacion.delete(0,END)
        precio.delete(0,END)
        messagebox.showinfo("informacion", "libro editado")
        actualizar()

    except Exception as e:
        print(e)
        mysqlC.rollback()
        mysqlC.close()

def filtrar_por_editorial():
    editorial_filtro = editorial_f.get()
    if not editorial_filtro:
        messagebox.showwarning("Advertencia", "Por favor, ingrese una editorial para filtrar.")
        return

    mysqlC = mysql.connector.connect(host="localhost", user="root", password="", database="proyecto")
    micursos = mysqlC.cursor()

    try:
        micursos.execute(f"SELECT * FROM libros WHERE editorial = %s", (editorial_filtro,))
        lista = micursos.fetchall()
        
        for i in listbox.get_children():
            listbox.delete(i)

        for i, (id, titulo, autor, editorial, año_publicacion, precio) in enumerate(lista, start=1):
            listbox.insert("", "end", values=(id, titulo, autor, editorial, año_publicacion, precio))

        if not lista:
            messagebox.showinfo("Información", f"No se encontraron libros de la editorial '{editorial_filtro}'.")
    except Exception as e:
        print(e)
        messagebox.showerror("Error", "Ocurrió un error al filtrar.")
        mysqlC.close()

def obtenerR(event):
    titulo.delete(0,END)
    autor.delete(0,END)
    editorial.delete(0,END)
    año_publicacion.delete(0,END)
    precio.delete(0,END)
    
    renglon = listbox.selection()[0]
    print(renglon)
    seleccion = listbox.set(renglon)
    print(seleccion)
    titulo.insert(0, seleccion["Titulo"])
    autor.insert(0, seleccion["Autor"])
    editorial.insert(0, seleccion["Editorial"])
    año_publicacion.insert(0, seleccion["Año de publicacion"])
    precio.insert(0, seleccion["Precio"])
 
root = tk.Tk()
root.geometry("1200x600")
 
label1 = tk.Label(root,text="REGISTRO DE LIBROS", fg="purple",font=("Broadway",28)).place(x=400,y=0)
 
global titulo
global autor
global editorial
global año_publicacion
global precio

labeltitulo = tk.Label(root, text="Titulo", font=("Georgia", 13))
labeltitulo.place(x=100, y=80)
 
labelautor = tk.Label(root, text="Autor", font=("Georgia", 13))
labelautor.place(x=100, y=110)
 
labeleditorial = tk.Label(root, text="Editorial", font=("Georgia", 13))
labeleditorial.place(x=100, y=140)
 
labelaño_publicacion = tk.Label(root, text="Año de Publicacion", font=("Georgia", 13))
labelaño_publicacion.place(x=650, y=80)

labelprecio = tk.Label(root, text="Precio", font=("Georgia", 13))
labelprecio.place(x=650, y=110)

label_filtro = tk.Label(root, text="Filtrar por Editorial", font=("Georgia", 13))
label_filtro.place(x=650, y=140)
 
titulo = tk.Entry(root)
titulo.place(x=270, y=80)
 
autor = tk.Entry(root)
autor.place(x=270, y=110)
 
editorial = tk.Entry(root)
editorial.place(x=270, y=140)

año_publicacion = tk.Entry(root)
año_publicacion.place(x=820, y=80)

precio = tk.Entry(root)
precio.place(x=820, y=110)

editorial_f = tk.Entry(root)
editorial_f.place(x=820, y=140)

tk.Button(root,text="Crear", command=add, height=5, width=10, font=("Rockwell",14)).place(x=350,y=250)
tk.Button(root,text="Editar",command=edit, height=5, width=10, font=("Rockwell",14)).place(x=500,y=250)
tk.Button(root,text="Eliminar",command=delete, height=5, width=10, font=("Rockwell",14)).place(x=650,y=250)
tk.Button(root, text="Filtrar", command=filtrar_por_editorial, height=1, width=10, font=("Rockwell", 14)).place(x=820, y=170)
tk.Button(root, text="Mostrar todo", command=mostrar, height=1, width=12, font=("Rockwell", 14)).place(x=950, y=170)
 
columnas = ("Id","Titulo","Autor","Editorial", "Año de publicacion", "Precio")
listbox = ttk.Treeview(root,columns=columnas,show="headings")
 
for col in columnas:
    listbox.heading(col, text=col)
    listbox.grid(row=1, column=0, columnspan=1)
    listbox.place(x=0, y=400)
 
mostrar()
listbox.bind("<Double-Button-1>",obtenerR)

 
root.mainloop()