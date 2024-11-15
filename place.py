import tkinter as tk

root = tk.Tk()
root.title("Ejemplo de .place()")

label1 = tk.Label(root, text="Etiqueta 1", bg="Lightblue")
label1.place(x=50, y=50)

label2 = tk.Label(root, text="Etiqueta 2", bg="Lightgreen")
label2.place(x=200, y=100)

label3 = tk.Label(root, text="Etiqueta 3", bg="Lightcoral")
label3.place(x=400, y=150)

root.mainloop()