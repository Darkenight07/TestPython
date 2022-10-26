import tkinter as tk
from tkinter import Label, Button

mywindow = tk.Tk() # Ejecutamos el GUI de tkinter
mywindow.title ('Python Juego') # Nombre de la ventana
mywindow.geometry('1280x720') # Dimensiones de la ventana
mywindow.resizable(False,False) # De esta forma hacemos que no puedas estirar la ventana

def mensaje():
    print(f'Mensaje y resultado {4 + 5}')

lbl = Label(mywindow, text='Hola que tal estamos')
lbl.config(fg='red')
lbl.pack()

btn = Button(mywindow, text='Presione este boton para mensaje', command=mensaje)
btn.config(fg='red',bg='blue') # Poner una configuracion al objeto, fg o bg que es background
btn.pack()

btn.place(x=34, y=34) # De esta forma posicionamos el objeto, hay otros como
# width=1000, height=100 ancho y altura

mywindow.mainloop()