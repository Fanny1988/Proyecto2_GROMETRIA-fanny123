import subprocess
from tkinter import *             #estos son los import
from tkinter import messagebox

#singleton y decorador
def singleton(cls):                        #clse singlenton,
    #diccionario para las instancias
    instances = dict()
    def wrap(*args,**kwargs):              # el wrap tiene relacion con las clases
        if cls not in instances:          # si la clase no esta en las instamcias, enla instancia va a agregar instancia de clases,
            instances[cls]=cls(*args, **kwargs)
            ingresar()                              #llama a la funcion inglesar, la cual entra por medio de una instancia
        return instances[cls]                          # SE RETORNA a ls classe
    return wrap

@singleton
class Admin():
  pass

root = Tk()   # sirvepara tener ventana

#seccion de funciones
def ingresar():
    try:
        user = txtNombreUsuario.get()
        passw = txtClaveUsuario.get()

        user1 = Admin()                          #esto quiere decir que la instancia va a ser única

        #se valida que los datos necesarios esten completos
        if user == "admin" and passw == "admin" and user1:
            import ventanaPrincipal
            root.deiconify()                        # esconder la ventana
            #se llama al scrip ventana principal
            exec(open("ventanaPrincipal.py").read())  #abrir nuevo archivo
        else:
            # si los datos estan incompletos se informa el error
            messagebox.showwarning("Error", "Verifique la informacion")           #mensaje error
    except:
        print("")

#seccion de las variables del logueo
txtUsuario = StringVar()
txtClave = StringVar()

# Configuración de la ventana principal
root.title("Ingreso Administrativo")             #nombre de la ventana
root.geometry("450x250")                          #dimenciones de la ventana
root.resizable(0,0)
root.eval('tk::PlaceWindow . center')            #posicion de la ventana

#label que muestran las etiquetas por cada entrada
lblHeader = Label(root, text="INGRESO DE USUARIO")   #los label son los cuadritos con los textos (ingreso de ususario).
lblUser = Label(root,text="Usuario")                 #(usuario)
lblClave = Label(root,text="Clave")                  #(clave)
#posicion de las entradas
lblHeader.place(x=150,y=30)                            #posicion de los 3 labels
lblUser.place(x=80,y=80)
lblClave.place(x=80,y=130)
#entradas de texto o numericas para el usuario
txtNombreUsuario=Entry(root)
txtClaveUsuario=Entry(root,show="*")
#posiciones de los elementos
txtNombreUsuario.place(x=150,y=80)
txtClaveUsuario.place(x=150,y=130)

#boton acceder
btnCargar = Button(root,text="Ingresar",command=singleton(Admin)) # aqui se define el boton cargar de tipo entry ingresa
btnCargar.place(x=150,y=180)                                    #el command llama a singlenton, que tiene admin
#ciclo que mantiene la ventana de forma constante
root.mainloop()                                        # significa que se va a ejecutar infinitamente
