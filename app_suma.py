# se importala libreria tkinter 
from tkinter import *
# -----------------------------
# funciones de la app 
# -----------------------------


# -----------------------------
# ve ntana principal de la app
# -----------------------------

# se declara una variable  llamada ventana_principal, que anquiere las caracteristicas de un juego

ventana_principal= Tk()

# Titulo de ventana 
ventana_principal.title("Daniel Diaz ")

# Tamaño de la ventana 
ventana_principal.geometry("800x500")

# deshabilita boton de minimizar la ventana 
ventana_principal.resizable(0,0)

# color de fondo de la ventana 
ventana_principal.config(bg= "black")

# variables globales 
a = StringVar()
b = StringVar()
c = IntVar()
# -----------------------------
# frame 1 - entrada de datos 
# -----------------------------

frame_1  = Frame(ventana_principal)
frame_1.config(bg = "ivory2", width=780,height=240)
frame_1.place(x=10, y=10)

#imagen 
logo= PhotoImage(file="img/btn-suma.png")
Label_logo= Label(frame_1, image= logo)
Label_logo.place(x=10,y=10)

# Etiqueta para el titulo de la app
titulo= Label(frame_1, text="colegio San Jose De Guanenta ")
titulo.config(bg="yellow", fg="blue", font=("arial",16))
titulo.place(x=390,y=10)

# etiqueta para subtitulo 1 de la app 
subtitulo1= Label(frame_1, text= "Especialidad sistemas ")
subtitulo1.config(bg= "yellow", fg="blue", font=("arial",12))
subtitulo1.place(x=390,y=40)

# etiqueta para subtitulo 2 de la app 
subtitulo2= Label(frame_1, text= "Suma de dos enteros ")
subtitulo2.config(bg= "ivory2", fg="blue", font=("arial",15), anchor=CENTER)
subtitulo2.place(x=390,y=70)

# etiqueta para el primer valor - a
Label_a= Label(frame_1, text= "a = ")
Label_a.config(bg= "ivory2", fg="blue", font=("arial",15), anchor=CENTER)
Label_a.place(x=390,y=120)

# Entry para el primer valor - a
Entry_a= Entry(frame_1, width=4, textvariable=a)
Entry_a.config(font=("arial", 20), justify=CENTER)
Entry_a.focus_set()
Entry_a.place(x=487, y=120)

# Entry para el segundo valor valor - a
Entry_b= Entry(frame_1, width=4, textvariable=b)
Entry_b.config(font=("arial", 20), justify=CENTER)
Entry_b.focus_set()
Entry_b.place(x=682, y=120)


# -----------------------------
# frame 2 - operaciones 
# -----------------------------

frame_2  = Frame(ventana_principal)
frame_2.config(bg = "ivory2", width=780,height=120)
frame_2.place(x=10, y=260)

# boton para sumar 
bt_sumar= Button(frame_2, text="Sumar", width=10)




# -----------------------------
# frame 3 - resultados
# -----------------------------

frame_3  = Frame(ventana_principal)
frame_3.config(bg = "ivory2", width=780,height=100)
frame_3.place(x=10, y=390)


# metodo principal que despliega la ventana en pantalla 
ventana_principal.mainloop()