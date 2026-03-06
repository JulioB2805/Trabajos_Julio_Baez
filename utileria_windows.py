from tkinter import *
import os

def abrirCalculadora():
    os.system("calc")

def abrirVisual():
    os.system("code")

def abrirnotas():
    os.system("notepad")

ventana=Tk()
ventana.title("Utilerias de windows")
ventana.geometry("400x200")

bCalc=Button(text="Calculadora",command=abrirCalculadora)
bCalc.place(x=0, y=0)

bVisual=Button(text="Visual Studio Code", command=abrirVisual)
bVisual.place(x=100,y=0)

bnotas=Button(text="Bloc de notas", command=abrirnotas)
bnotas.place(x=0,y=40)

ventana.mainloop()