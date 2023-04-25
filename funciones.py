import os

#tupla de tipo estudiante
listaRegistro=[]         #lista ordenada de registros
#onjecto persona para el logeo con admin y pass
class Person():
  def __init__(self, name, password):
    self.name = name
    self.password = password
#objeto estudiante se usa para los registros
class Estudiante:
  def __init__(self, nombre, seccion,operacion):
    self.name = nombre
    self.seccion = seccion
    self.operacion=operacion

#almacenar un nuevo registro de operacion
def GuardarRegistro(alumno,seccion,operacion):
    file = open("Registros.txt", "a")
    file.write(alumno + "," + seccion + "," + operacion+"\n")

#actualizar un registro de operacion
def ActualizarRegistro(alumno,seccion,operacion):
    archivo = open("Registros.txt", "r")
    archivoAux = open("RegistrosAux.txt", "a")

    #se busca el registro y se lee cada linea
    for linea in archivo:
        #cada linea se separa en un vector con el uso de split
        tmp = linea.split(',')
        #si los datos coinciden se actualiza
        if tmp[0] == alumno and tmp[1] == seccion:
            archivoAux.write(alumno + "," + seccion + "," +operacion+"\n")
        else:
            #caso contrario se deja el dato previo sin modificarlo
            archivoAux.write("".join(linea))

    archivo.close()
    archivoAux.close()
    #se renombran los archivos
    os.remove("Registros.txt")
    os.rename("RegistrosAux.txt", "Registros.txt")

#eliminar un estudiante
def EliminarRegistro(alumno,seccion,operacion):
    archivo = open("Registros.txt", "r")
    archivoAux = open("RegistrosAux.txt", "a")

    #se leen todas las lineas del archivo
    for linea in archivo:
        #se hace un vector y si cada linea es diferente a la que se busca se guarda
        # pero al encontrar la deseada se omite ya qye no cumple la condicion
        tmp = linea.split(',')
        if tmp[0] != alumno and tmp[1] != seccion:
            archivoAux.write(tmp[0] + "," + tmp[1] + "," +tmp[2])

    archivo.close()
    archivoAux.close()
    os.remove("Registros.txt")
    os.rename("RegistrosAux.txt", "Registros.txt")

# leer el registro
def LeerRegistros():
    archivo = open("Registros.txt", "r")
    datos = archivo.readlines()
    # Es necesario quitar el ultimo caracter porque es un salto de linea
    datosModificar = [linea[:-1] for linea in datos]
    #se lee cada linea y se agrega a la listaEstudiante para su uso
    for linea in datosModificar:
        tmp = linea.split(',')
        estudiante = Estudiante(tmp[0],tmp[1],tmp[2])
        listaRegistro.append(estudiante)

    archivo.close()
