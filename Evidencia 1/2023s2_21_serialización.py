# -*- coding: utf-8 -*-
"""2023s2 21 Serialización.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J7MwJkS6_9mpDC8Qb9te98nePibieyiu

# **CLASE DE SERIALIZACIÓN**

Elabora una clase llamada **``archivador``**, que tenga como función guardar y leer archivos físicos que contengan un objeto serializado. Los métodos sugeridos serían los siguientes:

1. **``leer_archivo()``**: Lee el contenido de un archivo de extensión ``.pickle``, y retorna el objeto contenido en él.
    1. Especificaciones:
        1. El objeto, internamente, estará serializado usando pickle.
        1. El método retorna una tupla que contiene un valor ``bool`` si la operación no fue posible (``False``), o si fue correcta (``True``).
        1. Como segundo valor de la tupla, retorna el objeto leído (siempre y cuando la operación haya sido posible). Si no, que regrese nada ''.
    1. Argumentos:
        1. **``archivo``** (str): Es el nombre del archivo, sin extensión.

1. **``guardar_archivo()``**: Almacena un objeto serializado a pickle, en un archivo binario de extensión ``.pickle``. Los argumentos del método son los siguientes:
    1. Especificaciones:
        1. Si el archivo existe, lo remplaza.
        1. Retorna True si tuvo éxito, y False si no.
    1. Argumentos:
        1. **``archivo``** (str): Es el nombre del archivo.
        1. **``objeto``** (unknown): Es el objeto a serializar. Puede ser de cualquier tipo.
        1. **``respaldar``** (bool): Indica si se desea hacer respaldo de extensión ``.bak`` del archivo existente, antes de su remplazo (``True``), o no (``False``).
"""

# Definición de datos

eventos={
    1:"Evento 1",
    2:"Evento 2"
}

asistentes={
    1:"Asistente 1",
    2:"Asistente 2",
    3:"Asistente 3"
}

registro={
    1:[1,1],
    2:[2,1],
    3:[3,1],
    4:[1,2],
    5:[2,2]
}

repositorio=[eventos,asistentes,registro]

# Librería para serializar json
import pickle

repositorio_pickle = pickle.dumps(repositorio)

print(repositorio_pickle)

nuevo_objeto=pickle.loads(repositorio_pickle)

print(repositorio==nuevo_objeto)

import pickle
import os

class archivador:
    objeto=''
    archivo='sin_nombre.pickle'
    respaldar=False

    def __init__(self,objeto='',archivo='',respaldar=False):
        self.objeto=objeto
        self.archivo=archivo
        self.respaldar=respaldar

    def guardar_archivo(self,
                        objeto='',
                        archivo='sin_nombre.pickle',
                        respaldar=False):
        try:
            if self.respaldar:
                nombre_bak=self.archivo.split('.')[0]+'.bak'
                if os.path.exists(archivo):
                    if (os.path.exists(nombre_bak)):
                        os.remove(nombre_bak)
                        os.rename(archivo,nombre_bak)
            # Se genera la versión serializada del objeto.
            with open(archivo,"wb+") as f:
                pickle.dump(objeto,f)
        except:
            # Si algo sale mal, retorna False (no fue posible)
            # y un str vacío.
            return False
        # Si pudo hacer la operación, retorna True.
        return True

    def leer_archivo(self,archivo):
        try:
            with open(archivo,"rb") as f:
                datos_recuperados=pickle.load(f)
        except:
            return False,''
        # Si todo salió bien, retorna verdadero, y los datos.
        return True, datos_recuperados

# Generar una instancia de la clase
trabajo=archivador()


# Leo el archivo.
resultado, repositorio=trabajo.leer_archivo('repositorio.pickle')
resultado, sin_modificar=trabajo.leer_archivo('repositorio.pickle')


# Modifico datos.
repositorio[0].update({3:"Evento 3"})

print(repositorio)
print(sin_modificar)



# Ejecutar el método guardar_archivo()
trabajo.guardar_archivo(repositorio,'repositorio.pickle',False)

archivo='archivo.doc'
nombre_bak=archivo.split('.')[0]+'.bak'
print(nombre_bak)