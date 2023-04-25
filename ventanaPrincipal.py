from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import threading

import funciones

#funciones
def DatosBntCargar():               #funcion
    nombre = txtNombre.get()
    seccion=txtSeccion.get()
    data = str(combo.get())           # recuperar datos de esta funcion

    #se validan los datos no esten vacios
    if data!='' and nombre!='' and seccion!='':               #aqui decimos que si data,nombre, seccion son diferentes de vacio
        SeleccionarOpcion(nombre, seccion, data, 1)              # entonces se llema a la funcion seleccionarOpcion.#
                                                                        # opcion 1 guardar.
                                                                         # opciom 2 es actulizar
    else:
        messagebox.showerror("Error", "Complete la informacion")      #sino  muestra este mensaje de error

def DatosBntActualizar():                 # funcion de actualizaf datos
                                           #se recuperan los datos de los componentes graficos para actualizar cada uno
    nombre = str(comboA.get())
    seccion = str(comboB.get())
    data = str(comboC.get())
    #se envian a la funcion necesaria
    SeleccionarOpcion(nombre, seccion, data, 2)

def EliminarDatos():           #funcion para eliminar  datos
    #se recuperan los datos necesarios para eliminar el registrp
    nombre = str(comboA.get())
    seccion = str(comboB.get())
    #data = str(comboC.get())
    funciones.EliminarRegistro(nombre, seccion, "")
    messagebox.showinfo("Aviso", "Se ha eliminado con exito")

    listaRegistro.clear()      #esto nos sirve para limpiar lods datos
    comboA.config(values=[''])
    comboB.config(values=[''])
    comboA.current(0)
    comboB.current(0)
    ListaCombo()          #"se leen los registros

#opcion recibe el nombre seccion seleccion en caso de actualzar y la opcion es su es guardar un registro
# o actualizar
def SeleccionarOpcion(nombre, seccion,seleccion,opcion):
    import ventanaCalculos
    if opcion == 1:
        funciones.GuardarRegistro(nombre, seccion, seleccion)
    if opcion == 2:
        funciones.ActualizarRegistro(nombre, seccion, seleccion)

    listaRegistro.clear()   #limpiar
    comboA.config(values=[''])
    comboB.config(values=[''])
    comboA.current(0)
    comboB.current(0)
    ListaCombo()
    ventanaCalculos.OpcionSeleccionada(seleccion) #ventana de calculos que nos manda a otro scrip ve ventana de calculos
    exec(open("ventanaCalculos.py").read())    #segun la opcion que seleccione el usuario, (cuadrado, o tiengulo etc)

#funcion para leer los datos del archivo
listaRegistro=[]
def LeerRegistros():
    try:
        archivo = open("Registros.txt", "r")                  #aqui se lee el registro
        datos = archivo.readlines()
        # Es necesario quitar el ultimo caracter porque es un salto de linea
        datosModificar = [linea[:-1] for linea in datos]

        for linea in datosModificar:                      #lee registro linea por linea.
            tmp = linea.split(',')      #separar por comas
            estudiante = funciones.Estudiante(tmp[0], tmp[1], tmp[2]) #
            listaRegistro.append(estudiante)
        archivo.close()
    except:
        print("Archivo")

def ListaCombo():
    #se limpia el combobox, despues se genera una matriz
    clearComboBox()
    LeerRegistros()
    #para obtener la longitud
    matriz = [["","",""]]*len(listaRegistro)             # matriz con 3 posisiciones que representan la posicion de la fincion estudiante
    vectorNombre=[]                         # se inician estos vectores de nombre y seccion
    vectorSeccion=[]
    #se inicia un contador en cero
    contador = 0 #para poder moverse en la matriz
    for n in listaRegistro:                                             #iterando sobre la lista,

        #se recorre la lista y se almacenan en una matriz
        Estudiante=n                                                             #donde estudiante =n
        matriz[contador] = [Estudiante.name,Estudiante.seccion,Estudiante.operacion]       #aqaui usamos el objeto estudiante para llenar esta matriz
        vectorNombre.append(Estudiante.name)                                      #aqui le agregamos al vector nombre(estudisnte,name
        vectorSeccion.append(Estudiante.seccion)                                       # aqui tambien
        contador=contador+1                                                        #incrementamos con un contador
    #la matriz alimenta los valores de cada combobox con los vectores
    comboA['values'] = vectorNombre                                          # los combo A y B los llenamos con los vetores
    comboB['values'] =vectorSeccion

def clearComboBox():
    comboA.configure(values=())


 #configuracion de la parte visual
root = Tk()

# Configuración de la ventana secundaria registrar Estudiante
root.title("Registro Estudiantil")
root.eval('tk::PlaceWindow . center')
root.geometry("800x300")
root.resizable(0,0)

#apartado de nuevo registro
lblHeader = Label(root, text="REALIZAR NUEVO CALCULO")
lblAlumno = Label(root,text="Nombre del estudiante")
lblSeccion = Label(root,text="Seccion del estudiante")
lblOperacion = Label(root,text="Operacion a realizar")

lblHeader.place(x=80,y=30)
lblAlumno.place(x=80,y=80)
lblSeccion.place(x=80,y=130)
lblOperacion.place(x=80, y=180)

#apartado de actualizar
lblHeaderActualizar = Label(root, text="ACTUALIZAR CALCULO")
lblAlumnoActualizar = Label(root,text="Nombre del estudiante")
lblSeccionActualizar = Label(root,text="Seccion del estudiante")
lblOperacionActualizar = Label(root,text="Operacion a realizar")

lblHeaderActualizar.place(x=500,y=30)
lblAlumnoActualizar.place(x=500,y=80)
lblSeccionActualizar.place(x=500,y=130)
lblOperacionActualizar.place(x=500, y=180)

#Entries
txtNombre=Entry(root)
txtSeccion=Entry(root)

txtNombre.place(x=250,y=80)
txtSeccion.place(x=250,y=130)

#Combobox con seleccion de la operacion se guiara a cada pantalla
combo = ttk.Combobox(root,state="readonly")
combo['values'] = ('Circulo','Cuadrado','Triangulo','Rectangulo')
combo.place(x=250, y=180)

#actualizar
comboA = ttk.Combobox(root,state="readonly")
comboA.place(x=500, y=80)
comboB = ttk.Combobox(root,state="readonly")
comboB.place(x=500, y=130)
comboC = ttk.Combobox(root,state="readonly")
comboC['values'] = ('Circulo','Cuadrado','Triangulo','Rectangulo')
comboC.place(x=500, y=180)

#btn seleecionar
btnCargar=Button(root,text="Calculo Nuevo",command=DatosBntCargar)
btnCargar.place(x=250,y=230)

btnActualizar=Button(root,text="Actualizar Calculo",command=DatosBntActualizar)
btnActualizar.place(x=500,y=230)

btnEliminar=Button(root,text="Eliminar Calculo",command=EliminarDatos)
btnEliminar.place(x=500,y=260)
#para cargar la lista
ListaCombo()

root.mainloop()
