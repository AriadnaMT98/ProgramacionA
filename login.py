import tkinter as tk
from tkinter import messagebox
import mysql.connector
 
def verificar_usuario():
    nombre = entry_nombre.get()
    contraseña = entry_contraseña.get()
 
    try:
        conn = mysql.connector.connect(
            host='localhost',      
            user='root',          
            password='',  
            database='proyecto'    
            )
 
        cursor = conn.cursor()
 
        cursor.execute('''
            SELECT * FROM usuarios WHERE nombre = %s AND contraseña = %s
        ''', (nombre, contraseña))
 
        usuario = cursor.fetchone()
 
        if usuario:
            messagebox.showinfo("Login exitoso", f"Bienvenido {usuario[1]}")
        else:
            messagebox.showerror("Error", "Usuario o contraseña no encontrados.")
   
    except mysql.connector.Error as err:
        messagebox.showerror("Error de conexión", f"Error: {err}")
   
    finally:
        if conn.is_connected():
            conn.close()  

def abrir_admin_ventana():
    root.withdraw()
    
    ventana_admin = tk.Toplevel(root)
    ventana_admin.title("Administrador")
    
    def regresar_a_login():
        ventana_admin.destroy()  
        root.deiconify()  

    boton_regresar = tk.Button(ventana_admin, text="Salir", command=regresar_a_login)
    boton_regresar.pack(pady=20)

def abrir_admin_ventana():
    root.withdraw()
    
    ventana_admin = tk.Toplevel(root)
    ventana_admin.title("Administrador")
    
    def regresar_a_login():
        ventana_admin.destroy()  
        root.deiconify()  

    boton_regresar = tk.Button(ventana_admin, text="Salir", command=regresar_a_login)
    boton_regresar.pack(pady=20)

root= tk.Tk()
root.title("Login")
root.geometry("300x200")

boton_abrir_admin_ventana = tk.Button(root, text="Abrir ventana de administrador", command=abrir_admin_ventana)
boton_abrir_admin_ventana.pack(pady=20)
 

label_nombre = tk.Label(root, text="Nombre:")
label_nombre.pack(pady=5)
entry_nombre = tk.Entry(root, width=30)
entry_nombre.pack(pady=5)
 
label_contraseña = tk.Label(root, text="Contraseña:")
label_contraseña.pack(pady=5)
entry_contraseña = tk.Entry(root, width=30, show="*")
entry_contraseña.pack(pady=5)
 
btn_login = tk.Button(root, text="Login", command=verificar_usuario)
btn_login.pack(pady=20)
 
root.mainloop()