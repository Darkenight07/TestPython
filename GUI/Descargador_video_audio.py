import tkinter as tk
from tkinter import Label, Button, Entry
import pytube


mywindow = tk.Tk() # Ejecutamos el GUI de tkinter
mywindow.title ('Descargador de videos | Youtube') # Nombre de la ventana
mywindow.geometry('500x400') # Dimensiones de la ventana
mywindow.resizable(False,False) # De esta forma hacemos que no puedas estirar la ventana 


textlinkyoutube = Label(mywindow, text='Pegue aqui el enlace:')
textlinkyoutube.config(fg='black')
textlinkyoutube.place(relx=0.001, rely=0.1, relwidth=0.5, relheight=0.5)

textlinkyoutube_url = Entry(mywindow)
textlinkyoutube_url.place(x=200, y=130)

textlinkyoutube_path = Entry(mywindow)
textlinkyoutube_path.place(x=200, y=190)

textpathyoutube = Label(mywindow, text='Indique la ruta de descarga:')
textpathyoutube.config(fg='black')
textpathyoutube.place(relx=0.08, rely=0.44, relwidth=0.3, relheight=0.1)

# Funcion que hace que al presionar el boton 'buttondownloadyoutube'
# se descargue el video seleccionado

def DownloadVideoYoutube():
    path = str(r"C:\Users\samue\Downloads")
    url = 'https://www.youtube.com/watch?v=5Ch7KsimJjk'
    yt = pytube.YouTube(url)
    st = yt.streams.get_by_itag('315')
    st.download(path)

"""
lstst = yt.streams.all()
    for st in lstst:
        print(st)
"""


buttondownloadyoutube = Button(mywindow, text='Descargar video mp4', command=DownloadVideoYoutube)
buttondownloadyoutube.config(bg='red')
buttondownloadyoutube.place(relx=0.35, rely=0.70, relwidth=0.3, relheight=0.1)

'https://www.altaruru.com/descargar-videos-y-musica-de-youtube-con-python-pytube/'
mywindow.mainloop()
