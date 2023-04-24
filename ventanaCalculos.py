from tkinter import *
from tkinter import messagebox

import ventanaPrincipal
import math

root = Tk()
#variable que almacena la opcion seleccionada
opcionSeleccionada=StringVar()
def RegresarAnterior():
    #para regresar a la ventana anterior
    ventanaPrincipal.root.deiconify()

#funcion que recibe la opcion seleccionada para ejecutar el calculo requerido
def OpcionSeleccionada(opcion):
    #se almacena la opcion
    opcionSeleccionada = opcion
    #funcion para los calculos dentro de la funcion previa para que se puedan leer los componentes
    def GenerarCalculo():
        #se calcula cada una de las diferentes areas y perimetros de cada figura
        try:
            area = 0
            perimetro = 0.
            if opcionSeleccionada == "Circulo":
                #se obtienen los datos de cada componente
                radio = float(txtLadoA.get())
                area = math.pi * radio * radio
                perimetro = math.pi * 2 * radio
            if opcionSeleccionada == "Cuadrado":
                lado = float(txtLadoA.get())
                area = lado * lado
                perimetro = lado * 4
            if opcionSeleccionada == "Rectangulo":
                base = float(txtLadoA.get())
                altura = float(txtLadoB.get())
                area = base * altura
                perimetro = (base * 2) + (altura * 2)
            if opcionSeleccionada == "Triangulo":
                base = float(txtLadoA.get())
                altura = float(txtLadoB.get())
                lado3 = float(txtLadoC.get())
                area = (base * altura) / 2
                perimetro = base + altura + lado3

            #mensaje general con la informacion de la operacion
            messagebox.showinfo("Resultado", f"El area es {area}\nEl perimetro es {perimetro}")
        except:
            messagebox.showerror("Error", "Complete la informacion")
    #almacenamiento de la opcion seleccionada
    opcionSeleccionada=opcion
    #se llama a la ventana previa se muestra ya qye solo esta oculta
    ventanaPrincipal.root.withdraw()

    # Configuración de la ventana secundaria registrar Estudiante
    root.title("CALCULO DEL AREA Y PERIMETRO")
    root.eval('tk::PlaceWindow . center')
    root.geometry("600x300")
    root.resizable(0, 0)

    lblHeader = Label(root, text=f"Calculo del area del {opcion}")
    lblHeader.place(x=200, y=30)

    lblLadoA = Label(root)
    lblLadoB = Label(root)
    lblLadoC = Label(root)

    lblLadoA.place(x=80, y=80)
    lblLadoB.place(x=80, y=130)
    lblLadoC.place(x=80, y=180)

    txtLadoA = Entry(root)
    txtLadoB = Entry(root)
    txtLadoC = Entry(root)

    txtLadoA.place(x=250, y=80)
    txtLadoB.place(x=250, y=130)
    txtLadoC.place(x=250, y=180)

    #segun cada operacion se cambia el texto de cada componente para ayudar a comprender los datos que debe tener
    if opcion == "Circulo":
        lblLadoA['text'] = 'Ingrese el radio del Circulo    '
        lblLadoB['text'] = '---------------------------------'
        lblLadoC['text'] = '---------------------------------'
    if opcion == "Cuadrado":
        lblLadoA['text'] = 'Ingrese el lado del cuadrado    '
        lblLadoB['text'] = '---------------------------------'
        lblLadoC['text'] = '---------------------------------'
    if opcion == "Rectangulo":
        lblLadoA['text'] = 'Ingrese el alto del rectangulo  '
        lblLadoB['text'] = 'Ingrese el ancho del rectangulo '
        lblLadoC['text'] = '---------------------------------'
    if opcion == "Triangulo":
        lblLadoA['text'] = 'Ingrese el lado A del triangulo '
        lblLadoB['text'] = 'Ingrese el lado B del triangulo '
        lblLadoC['text'] = 'Ingrese el lado C del triangulo '

    # btn seleecionar
    btnCargar = Button(root, text="Calcular",command=GenerarCalculo)
    btnCargar.place(x=250, y=230)

    btnRegresar = Button(root, text="Regresar", command=RegresarAnterior)
    btnRegresar.place(x=250, y=260)

    root.mainloop()