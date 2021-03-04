from tkinter import *
import random

#ventana
ventana = Tk()
ventana.title("Dados")
ventana.geometry("400x435+700+350")
ventana.configure(background="black")

#label resultado
Label(ventana,font = "Tahoma 15", text = "Elige tu dado", bg="black", fg="lawn green").grid(row = 0, column =1, columnspan = 4, padx = 50, pady = 5)

e_texto = Entry(ventana, font = ("Calibri 20"),bg="black", fg="lawn green")
e_texto.grid (row = 1, column = 1, columnspan = 4, padx = 50, pady = 5)

Label(ventana,font = "Tahoma 15", text = "¡¡Que la pifia te acompañe!!", bg="black", fg="lawn green").grid(row = 12, column =1, columnspan = 4, padx = 50, pady = 5)

#funciones
def dcuatro():
    xa=random.randint(1,4)
    e_texto.delete(0, END)
    e_texto.insert(0,xa)
    return xa    
def dseis():
    xb=random.randint(1,6)
    e_texto.delete(0, END)
    e_texto.insert(0,xb)
    return xb
def docho():
    xc=random.randint(1,8)
    e_texto.delete(0, END)
    e_texto.insert(0,xc)
    return xc
def ddiez():
    xd=random.randint(1,10)
    e_texto.delete(0, END)
    e_texto.insert(0,xd)
    return xd
def ddoce():
    xe=random.randint(1,12)
    e_texto.delete(0, END)
    e_texto.insert(0,xe)
    return xe
def dveinte():
    xf=random.randint(1,20)
    e_texto.delete(0, END)
    e_texto.insert(0,xf)
    return xf
    

#botones
boton1 = Button(ventana, text = "1D4",bg="black", fg="lawn green", width = 5, height = 2, command = lambda: dcuatro())
boton2 = Button(ventana, text = "1D6",bg="black", fg="lawn green", width = 5, height = 2, command = lambda: dseis())
boton3 = Button(ventana, text = "1D8",bg="black", fg="lawn green", width = 5, height = 2, command = lambda: docho())
boton4 = Button(ventana, text = "1D10",bg="black", fg="lawn green", width = 5, height = 2, command = lambda: ddiez())
boton5 = Button(ventana, text = "1D12",bg="black", fg="lawn green", width = 5, height = 2, command = lambda: ddoce())
boton6 = Button(ventana, text = "1D20",bg="black", fg="lawn green", width = 5, height = 2, command = lambda: dveinte())

boton1.grid(row = 2, column = 2, columnspan = 2, padx = 10, pady = 5)
boton2.grid(row = 3, column = 2, columnspan = 2, padx = 10, pady = 5)
boton3.grid(row = 4, column = 2, columnspan = 2, padx = 10, pady = 5)
boton4.grid(row = 5, column = 2, columnspan = 2, padx = 10, pady = 5)
boton5.grid(row = 6, column = 2, columnspan = 2, padx = 10, pady = 5)
boton6.grid(row = 7, column = 2, columnspan = 2, padx = 10, pady = 5)



#fin
ventana.mainloop()
