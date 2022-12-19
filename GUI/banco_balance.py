from tkinter import ttk
import tkinter as tk
from tkinter import Label, Button, Entry, messagebox
from tkinter import Tk
import tkinter

def ventana_balance():
    # Creamos una nueva ventana
    mywindow_balance = tk.Tk()
    mywindow_balance.title('Tu balance')
    mywindow_balance.geometry('1200x300')
    mywindow_balance.resizable(False,False)
    # Se crea una variable global
    global balance
    global balance_txt
    # Indicamos el dinero de base que tenemos en una variable colocando el simbolo $
    balance = 0
    balance_txt = f' Tienes {balance}'
    
    texto_balance = ttk.Label(mywindow_balance, text='Mi balance', font=('Arial', 25))
    texto_balance.place(relx=0.47, rely=0.02)

    # Muestra el balance
    texto_balance_txt = Label(mywindow_balance, text=balance_txt, font=('Arial', 15))
    texto_balance_txt.place(relx=0.49, rely=0.30)

    # Añadir dinero
    anadir_dinero_entry = ttk.Entry(mywindow_balance)
    anadir_dinero_entry.place(relx=0.15, rely=0.40)

    anadir_dinero_label = ttk.Label(mywindow_balance, text="Ingresar: ")
    anadir_dinero_label.place(relx=0.18, rely=0.32)

    # Funcion que hace que se añada dinero
    def anadirdinero():
        global balance
        global balance_txt
        dinero = anadir_dinero_entry.get()
        balance = int(dinero) + int(balance)
        balance_txt = f' Tienes {balance} $'
        texto_balance_txt = Label(mywindow_balance, text=balance_txt, font=('Arial', 15))
        texto_balance_txt.place(relx=0.49, rely=0.30)

    anadir_dinero_button = ttk.Button(mywindow_balance, text="Ingresar", command=anadirdinero)
    anadir_dinero_button.place(relx=0.17, rely=0.50)

    # Retirar dinero
    retirar_dinero_label = ttk.Label(mywindow_balance, text='Retirar: ')
    retirar_dinero_label.place(relx=0.80, rely=0.32)

    retirar_dinero_entry = ttk.Entry(mywindow_balance)
    retirar_dinero_entry.place(relx=0.77, rely=0.40)

    # Funcion para retirar el dinero con una logica
    def retirarDinero():
        # Resta el dinero que ha elegido el usuario al balance
        def retiradinero():
            global balance
            global balance_txt
            dinero = retirar_dinero_entry.get()
            balance = int(balance) - int(dinero)
            # Cambia el numero negativo a positivo al retirar el dinero
            balance * -1
            balance_txt = f' Tienes {balance} $'
            texto_balance_txt = Label(mywindow_balance, text=balance_txt, font=('Arial', 15))
            texto_balance_txt.place(relx=0.49, rely=0.30)
        # En caso que el balance valga menos que 1
        if balance < 1:
            print('Retirada dinero: Numero negativo')
            print(balance_txt)
        else:
            print('Retirada dinero: Numero positivo')
            print(balance_txt)
            # Ejecuta la funcion "retirardinero" que resta el dinero que ha elegido el usuario al balance
            retiradinero()
    # Boton de retirar
    retirar_dinero_button = ttk.Button(mywindow_balance, text='Retirar', command=retirarDinero)
    retirar_dinero_button.place(relx=0.79, rely=0.50)

    # Cerrar sesion
    def CerrarSesion():
        print('Has cerrado sesion')
        iniciosesion()

    cerrar_sesion = ttk.Button(mywindow_balance, text='Cerrar sesion', command=CerrarSesion)
    cerrar_sesion.place(relx=0.02, rely=0.05)

    mywindow_balance.mainloop()

def iniciosesion():
    mywindow = tk.Tk() # Ejecutamos el GUI de tkinter
    mywindow.title('Login') # Nombre de la ventana
    mywindow.geometry('500x300') # Dimensiones de la ventana
    mywindow.resizable(False,False) # De esta forma hacemos que no puedas estirar la ventana

    titlehome = ttk.Label(mywindow, text='Banco', font=('Arial', 25))
    titlehome.place(relx=0.35, rely=0.02)

    tilelogin = ttk.Label(mywindow, text='Login', font=('Arial', 20))
    tilelogin.place(relx=0.39, rely=0.30)

    # Login

    login_label_usuario = ttk.Label(mywindow, text='Usuario:')
    login_label_usuario.place(relx=0.41, rely=0.49)

    login_entry_usuario = ttk.Entry(mywindow)
    login_entry_usuario.place(relx=0.33, rely=0.56)

    login_label_passwd = ttk.Label(mywindow, text='Contraseña:')
    login_label_passwd.place(relx=0.39, rely=0.65)

    login_entry_passwd = ttk.Entry(mywindow, show='*')
    login_entry_passwd.place(relx=0.33, rely=0.73)


    # Diccionario de usuarios con contraseña
    dic_usuarios = {
        'usuario': {'Samuel', 'admin', 'usuario', 'a'},
        'contraseña': 12345
    }

    def IniciarSesion():
        usuario = login_entry_usuario.get()
        contraseña = int(login_entry_passwd.get())
        if usuario in dic_usuarios['usuario'] and contraseña == dic_usuarios['contraseña']:
            tkinter.messagebox.showinfo(title='Inicio de sesion correcto', message='Se ha iniciado sesion correctamente, veras tu zona privada en una nueva ventana')
            # Cerramos la ventana creada para loguearnos
            mywindow.destroy()
            # Ejecuta la funcion ventana_balance para ejecutar otra ventana cuando se cumpla la condicion
            ventana_balance()
        else:
            tkinter.messagebox.showinfo(title='Inicio de sesion incorrecto', message='No se ha podido iniciar sesion, nombre de usuario o contraseña incorrectos')
    login_button = ttk.Button(mywindow, text='Iniciar sesion', command=IniciarSesion)
    login_button.place(relx=0.38, rely=0.83)
    mywindow.mainloop()
iniciosesion()
