#Portafolio 2 Hackney Aguilar Chaves
"""
Nombre:invertirLista

Entradas:
        Recibe una lista
Salidas:
        La inversa de la lista
Restricciones:
            Si la lista esta vacio retorna 0
        
"""

def invertirLista(lista):
    if lista== []:
        return 0
    else:
        return invertirLista_aux(lista)


def invertirLista_aux(lista):
    if lista==[]:
        invertir= lista
    else:
        
        invertir= [lista[-1]] + invertirLista_aux(lista[:-1])

    return invertir
#------------------------------------------------------------------------------------------
"""
Nombre:extremosLista

Entradas:
        Recibe una lista

soluciones:
        Regresa los extremos de la lista
        
Restricciones:
            Si la lista esta vacia devuelve error
            lista=[1,2,3,4,]
"""

def extremoLista(lista):
    if lista== []:
        return print("Error")
    else:
        return extremosLista_aux(lista)


def extremosLista_aux(lista):
    if lista== []:
        extremos = lista
    else:
        extremos = lista[:1]+lista[-1:]

    return extremos
#------------------------------------------------------------------------------------------
"""
Nombre: eliminarDigito

Entreda:
        Recibe una lista
salidas:
        elimina el numero segun el numero elegido
"""

def eliminarDigito(num,eliminar):
    if num== 0:
        return print("Error")
    else:
        return elimarDigitos(num,eliminar)

#------------------------------------------------------------------------------------------
"""
Nombre: nivelesLista

Entrada:
        Recibe listas
Salidas:
        Devolver de una lista de listas la cantidad de sublista
        que tenga

Restricciones:
            Debe crear una lista
"""

def nivelesLista(lista,sublistas):
    if lista== []:
        return print("Error")
    else:
        return nivelesLista_aux(lista,sublistas)

def nivelesLista_aux(lista,sublistas,indiceActual):
    if lista==[]:
        return []

#------------------------------------------------------------------------
"""
nombre: validarVector

Entradas:
        Recive una lista
        
salida:
        Validar que la lista este compuesta de enteros
        
Restricciones:
        Solo se permiten valores enteros
        Debe de crear una lista
"""

def validarVector(lista):
    if (isinstance (lista,list)):
        return validarVector_aux(lista, True)
    else:
        print("Error: el parametro de entrada debe ser lista")

        
def validarVector_aux(lista,valor):
    if(lista ==[]):
        return valor
    else:
        if(isinstance(lista[0],int)):
            return validarVector_aux(lista[1:], True)
#--------------------------------------------------------------------
"""
Nombre: tamañoVector

Entrada:
        vector es una lista
Salidas:
        Verifica que el tamaño del vector sea el mismo que otro vector

Restriciones:
        Crear una lista con el misto tamaño que otra lista
"""
def tamañoVector(vector):
    if(vector == []):
        return 0
    else:
        return tamañoVector_aux(vector,0)
   
def tamañoVector_aux(vector,resultado):
    if(vector == []):
        return resultado
    else:
        return tamañoVector_aux(vector[1:], resultado + 1)
#---------------------------------------------------------------------------------------    

"""
Nombre:obtenerIndicesListaVectores

Entradas:
        Recibe vectores
Salidas:
        devolcer los indeces de una lista de vectores cuyo valor sean cero
        o un numero negativo

Restricciones:
            Se debe crear vectores
"""
def obtenerIndicesListaVectores(v1,v2,v3):
    if(validarDatosVector(v1) and validarDatosVector(v2) and validarDatosVector(v3)):
        if(tamañoVector(v1)== tamañoVector(v2) and tamañoVector(v2)):
           return obtenerIndicesListaVectores_aux(v1,v2,v3,[])
        else:
            print("Error: los venctores no tiene el mismo tamaño")
    else:
        print("Error: uno de los vectores no tienen valores enteros")

def obtenerIndicesListaVectores_aux(v1,v2,v3,resultado):
    if(v1==[]):
        return resultado
    else:
        return obtenerIndicesListaVectores_aux(v1[1:], v2[1:],v3[1:], resultado + [v[0] + v2[0]+v2[0]])
    
    
    
    





    
    
