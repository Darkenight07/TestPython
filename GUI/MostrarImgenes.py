import requests
import tkinter as tk
from tkinter import Label, Button, Entry, Image
from PIL import Image, ImageTk

mywindow = tk.Tk() # Ejecutamos el GUI de tkinter
mywindow.title ('Descargador de imagenes') # Nombre de la ventana
mywindow.geometry('500x400') # Dimensiones de la ventana
mywindow.resizable(False,False) # De esta forma hacemos que no puedas estirar la ventana


pegueaquienlaceimagentxt = Label(mywindow, text='Pegue un enlace aqui:')
pegueaquienlaceimagentxt.place(relx=0.001, rely=0.1, relwidth=0.5, relheight=0.5)


pegueaquienlaceimagen = Entry(mywindow)
pegueaquienlaceimagen.place(x=200, y=130)

def DownloadImageJPG():
    url_image = pegueaquienlaceimagen.get()
    name_local_image = 'download.jpg'
    imagen = requests.get(url_image).content
    with open(name_local_image, 'wb') as handler:
        handler.write(imagen)
        # Muestra la imagen descargada
    im1 = Image.open(name_local_image)
    im1.show()


buttondownloadyoutube = Button(mywindow, text='Descargar video JPG ', command=DownloadImageJPG)
buttondownloadyoutube.config(bg='red')
buttondownloadyoutube.place(relx=0.60, rely=0.70, relwidth=0.3, relheight=0.1)

def DownloadImagePNG():
    url_image = pegueaquienlaceimagen.get()
    name_local_image = 'download.png'
    imagen = requests.get(url_image).content
    with open(name_local_image, 'wb') as handler:
        handler.write(imagen)
    # Muestra la imagen descargada
    im = Image.open(name_local_image)
    im.show()


buttondownloadyoutube = Button(mywindow, text='Descargar video PNG ', command=DownloadImagePNG)
buttondownloadyoutube.config(bg='red')
buttondownloadyoutube.place(relx=0.1, rely=0.70, relwidth=0.3, relheight=0.1)



mywindow.mainloop()