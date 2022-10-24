import tkinter as tk
from tkinter import Label, Button, Entry

mywindow = tk.Tk() # Ejecutamos el GUI de tkinter
mywindow.title ('Calculadora') # Nombre de la ventana
mywindow.geometry('1280x720') # Dimensiones de la ventana
mywindow.resizable(False,False) # De esta forma hacemos que no puedas estirar la ventana

# Titulo principal

title_pr = Label(mywindow, text='Calculadora')
title_pr.config(fg='red')
title_pr.place(x=500, y=10,width=100, height=100)

# Funcionaes num
def num7():
    r_7 = float(7)
    resultado.insert(0,r_7)

def num4():
    r_4 = float(4)
    resultado.insert(0,r_4)

def num1():
    r_1 = float(1)
    resultado.insert(0,r_1)

def num8():
    r_8 = float(8)
    resultado.insert(0,r_8)

def num5():
    r_5 = float(5)
    resultado.insert(0,r_5)

def num2():
    r_2 = float(2)
    resultado.insert(0,r_2)

def num9():
    r_9 = float(9)
    resultado.insert(0,r_9)

def num6():
    r_6 = float(6)
    resultado.insert(0,r_6)

def num3():
    r_3 = float(3)
    resultado.insert(0,r_3)

def num0():
    r_0 = float(0)
    resultado.insert(0,r_0)

# Funcion eliminar, CE

def function_del():
    resultado.delete(0,'end')

# Funciones operadores

def opdivision():
    opdiv = ' / '
    resultado.insert(0,opdiv)

def opmulti():
    opmul = ' X '
    resultado.insert(0,opmul)

def oprest():
    opresta = ' - '
    resultado.insert(0,opresta)

def opsuma():
    opsum = ' + '
    resultado.insert(0,opsum)

# Funciones para sumar, restar, multiplicar y dividir

def sumar():
    resultadosuma = resultado.get()


    print(resultadosuma)








# Botones num

btn_num7 = Button(mywindow, text='7', command=num7)
btn_num7.place(x=500, y=250)

btn_num4 = Button(mywindow, text='4', command=num4)
btn_num4.place(x=500,y=280)

btn_num1 = Button(mywindow, text='1', command=num1)
btn_num1.place(x=500, y=310)

btn_num8 = Button(mywindow, text=8, command=num8)
btn_num8.place(x=530,y=250)

btn_num5 = Button(mywindow, text=5, command=num5)
btn_num5.place(x=530,y=280)

btn_num2 = Button(mywindow, text=2, command=num2)
btn_num2.place(x=530,y=310)

btn_num9 = Button(mywindow, text=9, command=num9)
btn_num9.place(x=560,y=250)

btn_num6 = Button(mywindow, text=6, command=num6)
btn_num6.place(x=560,y=280)

btn_num3 = Button(mywindow, text=3, command=num3)
btn_num3.place(x=560,y=310)

btn_num0 = Button(mywindow, text=0, command=num0)
btn_num0.place(x=530,y=340)

# Botones operadores

btn_num_division = Button(mywindow, text='/', command=opdivision)
btn_num_division.place(x=590,y=220)

btn_num_multi = Button(mywindow, text='X', command=opmulti)
btn_num_multi.place(x=590,y=250)

btn_num_rest = Button(mywindow, text='-', command=oprest)
btn_num_rest.place(x=590,y=280)

btn_num_sum = Button(mywindow, text='+', command=opsuma)
btn_num_sum.place(x=590,y=310)

btn_num_iguala = Button(mywindow, text='=', command=sumar)
btn_num_iguala.place(x=590,y=340)

btn_num_ce = Button(mywindow, text='CE', command=function_del)
btn_num_ce.place(x=500,y=220)

# Caja resultado

resultado = Entry(mywindow)
resultado.place(x=485,y=195)



mywindow.mainloop()
