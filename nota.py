import tkinter as tk

ventana = tk.Tk()
ventana.title("Ventana con Pestañas")

Nota = tk.Notebook(ventana)
P1 = tk.frame(Nota)
P2 = tk.frame(Nota)
Nota.add(P1)
Nota.add(P2)