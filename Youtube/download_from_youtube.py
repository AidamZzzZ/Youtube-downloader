#Se importan las librerias
from pytube import YouTube
from tkinter import *
from tkinter import messagebox as Messagebox

#se crea una funcion la que agregara el proceso de descarga
def accion():
    enlace=videos.get()
    video = YouTube(enlace)
    descarga = video.streams.get_highest_resolution()
    descarga.download()
    
#se crea otra funcion opcional,que al precionar el boton de informacion muestre mi perfil de github
def popup():
    Messagebox.showinfo("Sobre mi","Enlace a mi perfil de GitHub:https://github.com/AidamZzzZ")

#Se crea el formato
root = Tk()
root.config(bd=15)
root.title("Script para descargar videos!")

#se le agrega una imagen.png(ya descargada) y su ubicacion
imagen = PhotoImage(file="youtube.png")
foto = Label(root, image=imagen, bd=0)
foto.grid(row=0, column=0)

#se agrega una barra menu
menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)

#se agregan botones al menu
menubar.add_cascade(label="Para mas informacion", menu=helpmenu)
helpmenu.add_cascade(label="Informacion del autor",command=popup)
menubar.add_command(label="Salir", command=root.destroy)

#se crean instrucciones para el usuario
instrucciones = Label(root, text= "Programa para descargar videos de Youtube\n")
instrucciones.grid(row=0, column=1)

#enlace para descargar
videos = Entry(root)
videos.grid(row=1, column=1)

#Se crea el boton para descargar los enlaces
boton = Button(root, text="Descargar:", command=accion)
boton.grid(row=2, column=1)


root.mainloop()
