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

# Funcion num y operadores

def envia_boton(valor):
    anterior = resultado.get()
    resultado.delete(0,'end')
    resultado.insert(0, str(anterior + str(valor)))
    
#   Botones para que funcione los botones de suma

def suma():
    global num1
    global operacion
    num1 = resultado.get()
    num1 = float(num1)
    resultado.delete(0,'end')
    operacion = '+'

def resta():
    global num1
    global operacion
    num1 = resultado.get()
    num1 = float(num1)
    resultado.delete(0,'end')
    operacion = '-'

def multiplicacion():
    global num1
    global operacion
    num1 = resultado.get()
    num1 = float(num1)
    resultado.delete(0,'end')
    operacion = '*'

def division():
    global num1
    global operacion
    num1 = resultado.get()
    num1 = float(num1)
    resultado.delete(0,'end')
    operacion = '/'

# Funcion para que realice las operaciones
def igual():
    global num2
    num2 = resultado.get()
    resultado.delete(0, 'end')
    if operacion == '+':
        resultado.insert(0, num1 + float(num2))
    if operacion == '-':
        resultado.insert(0, num1 - float(num2))
    if operacion == '*':
        resultado.insert(0, num1 * float(num2))
    if operacion == '/':
        resultado.insert(0, num1 / float(num2))

# Funcion eliminar, CE

def function_del():
    resultado.delete(0,'end')

# Botones num

btn_num7 = Button(mywindow, text=7, command=lambda: envia_boton(7))
btn_num7.place(x=500, y=250)

btn_num4 = Button(mywindow, text=4, command=lambda: envia_boton(4))
btn_num4.place(x=500,y=280)

btn_num1 = Button(mywindow, text=1, command=lambda: envia_boton(1))
btn_num1.place(x=500, y=310)

btn_num8 = Button(mywindow, text=8, command=lambda: envia_boton(8))
btn_num8.place(x=530,y=250)

btn_num5 = Button(mywindow, text=5, command=lambda: envia_boton(5))
btn_num5.place(x=530,y=280)

btn_num2 = Button(mywindow, text=2, command=lambda: envia_boton(2))
btn_num2.place(x=530,y=310)

btn_num9 = Button(mywindow, text=9, command=lambda: envia_boton(9))
btn_num9.place(x=560,y=250)

btn_num6 = Button(mywindow, text=6, command=lambda: envia_boton(6))
btn_num6.place(x=560,y=280)

btn_num3 = Button(mywindow, text=3, command=lambda: envia_boton(3))
btn_num3.place(x=560,y=310)

btn_num0 = Button(mywindow, text=0, command=lambda: envia_boton(0))
btn_num0.place(x=530,y=340)

# Botones operadores

btn_num_division = Button(mywindow, text='/',command=division)
btn_num_division.place(x=590,y=220)

btn_num_multi = Button(mywindow, text='X',command=multiplicacion)
btn_num_multi.place(x=590,y=250)

btn_num_rest = Button(mywindow, text='-', command=resta)
btn_num_rest.place(x=590,y=280)

btn_num_sum = Button(mywindow, text='+', command=suma)
btn_num_sum.place(x=590,y=310)

btn_num_iguala = Button(mywindow, text='=', command=igual)
btn_num_iguala.place(x=590,y=340)

btn_num_ce = Button(mywindow, text='CE', command=function_del)
btn_num_ce.place(x=500,y=220)

# Caja resultado

resultado = Entry(mywindow)
resultado.place(x=485,y=195)

mywindow.mainloop()
