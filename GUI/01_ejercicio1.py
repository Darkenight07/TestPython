import tkinter as tk
from tkinter import Label, Button, Entry

mywindow = tk.Tk() # Ejecutamos el GUI de tkinter
mywindow.title ('MiniCalculadora') # Nombre de la ventana
mywindow.geometry('400x200') # Dimensiones de la ventana
mywindow.resizable(False,False) # De esta forma hacemos que no puedas estirar la ventana

def FnSuma():
    n1 = txt1.get()
    n2 = txt2.get()
    r = float(n1) + float(n2)
    txt3.delete(0,'end')
    txt3.insert(0,r)

lb1 = Label(mywindow,text='Primer numero', bg='yellow')
lb1.place(x=10,y=10,width=100, height=30)
txt1 = Entry(mywindow, bg='pink')
txt1.place(x=120,y=10,width=100, height=30)


lb2 = Label(mywindow,text='Segundo numero', bg='yellow')
lb2.place(x=10,y=50,width=100, height=30)
txt2 = Entry(mywindow, bg='pink')
txt2.place(x=120,y=50,width=100, height=30)

#Boton 

btn=Button(mywindow, text='Sumar', command=FnSuma)
btn.place(x=230, y=50, width=80, height=30)


lb3 = Label(mywindow,text='Resultado', bg='yellow')
lb3.place(x=10,y=120,width=100, height=30)
txt3 = Entry(mywindow, bg='pink')
txt3.place(x=120,y=120,width=100, height=30)

mywindow.mainloop()
