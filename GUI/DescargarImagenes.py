from tkinter import StringVar, ttk
import requests
import tkinter as tk
from tkinter import Label, Button, Entry, Image
from PIL import Image

mywindow = tk.Tk() # Ejecutamos el GUI de tkinter
mywindow.title ('Descargador de imagenes') # Nombre de la ventana
mywindow.geometry('500x400') # Dimensiones de la ventana
mywindow.resizable(False,False) # De esta forma hacemos que no puedas estirar la ventana


pegueaquienlaceimagentxt = Label(mywindow, text='Pegue un enlace aqui:')
pegueaquienlaceimagentxt.place(relx=0.001, rely=0.1, relwidth=0.5, relheight=0.5)


pegueaquienlaceimagen = Entry(mywindow)
pegueaquienlaceimagen.place(x=200, y=130)


# Funcion que descarga imagenes en formato PNG obteniendo la url gracias a un get de un entry 
# de tkinter
"""
def DownloadImagePNG():
    url_image = pegueaquienlaceimagen.get()
    name_local_image = 'download.png'
    imagen = requests.get(url_image).content
    with open(name_local_image, 'wb') as handler:
        handler.write(imagen)
    # Muestra la imagen descargada
    im = Image.open(name_local_image)
    im.show()


"""


# Combobox

def DownloadImage():
    if str(lista.get()) == 'JPG':
        url_image = pegueaquienlaceimagen.get()
        name_local_image_jpg = 'download.jpg'
        imagen = requests.get(url_image).content
        with open(name_local_image_jpg, 'wb') as handler:
            handler.write(imagen)
        # Muestra la imagen descargada
        im = Image.open(name_local_image_jpg)
        im.show()
    elif str(lista.get()) == 'PNG':
        url_image = pegueaquienlaceimagen.get()
        name_local_image_png = 'download.png'
        imagen = requests.get(url_image).content
        with open(name_local_image_png, 'wb') as handler:
            handler.write(imagen)
        # Muestra la imagen descargada
        im = Image.open(name_local_image_png)
        im.show()


lista = ttk.Combobox(mywindow)
lista.place(relx=0.1, rely=0.50, relwidth=0.3, relheight=0.1)
lista['values'] = ('No hay nada seleccionado','JPG', 'PNG')
lista.current(0)

button_download = Button(mywindow, command=DownloadImage, text='Descargar')
button_download.place(relx=0.1, rely=0.70, relwidth=0.3, relheight=0.1)



"""
buttondownloadyoutube = Button(mywindow, text='Descargar imagen PNG ', command=DownloadImagePNG)
buttondownloadyoutube.config(bg='red')
buttondownloadyoutube.place(relx=0.1, rely=0.70, relwidth=0.3, relheight=0.1)

"""


mywindow.mainloop()