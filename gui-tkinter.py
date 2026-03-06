from tkinter import *
from tkinter import ttk

def saludar():
    print("hola")
ventana=Tk()
ventana.title("Ventana de inicio")
ventana.geometry("450x250")

frm=ttk.Frame(ventana,padding=10)
frm.grid()
ttk.Label(frm,text="Saludar").grid(column=0,row=0)
ttk.Button(frm,text="Iniciar",command=saludar).grid(column=1,row=0)

ventana.mainloop()