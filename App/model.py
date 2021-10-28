"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as ms
import datetime
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newAnalyzer():
    analyzer = {'avistamientos': lt.newList(datastructure='SINGLE_LINKED'),
                'ciudad': om.newMap(omaptype='RBT')
                }
    return analyzer


# Funciones para agregar informacion al catalogo


def addUFO(analyzer, UFO):
    lt.addLast(analyzer['avistamientos'], UFO)
    updateCity(analyzer['ciudad'], UFO)
    return analyzer


def updateCity(map, UFO):
    occurredcity = UFO['city']
    entry = om.get(map,occurredcity)
    if entry is None:
        datentry = newDataEntry(UFO)
        om.put(map, occurredcity, datentry)
    else:
        datentry = me.getValue(entry)
    addCity(datentry, UFO)
    return map


def addCity(datentry, UFO):
    lst = datentry['lstUFOS']
    lt.addLast(lst, UFO)
    return datentry


def newDataEntry(UFO):
    entry = {'lstUFOS': lt.newList('SINGLE_LINKED')}
    return entry

# Funciones para creacion de datos

# Funciones de consulta

def UFOSize(analyzer):
    return lt.size(analyzer['avistamientos'])

def indexHeight(analyzer):
    return om.height(analyzer['ciudad'])


def indexSize(analyzer):
    return om.size(analyzer['ciudad'])

def avistamiento_ciudad(analyser,ciudad):
    lista = me.getValue(om.get(analyser["ciudad"],ciudad))
    lista = lista["lstUFOS"]
    lista_sorted = merge_sort(lista,lt.size(lista),cmpdatetime)
    return lista_sorted

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpdatetime(UFO1,UFO2):
    orden = None
    if (UFO1["datetime"]!="") and (UFO2["datetime"]!=""):
        orden = (datetime.datetime.strptime(UFO1["datetime"],"%Y-%m-%d") > datetime.datetime.strptime(UFO2["datetime"],"%Y-%m-%d"))
    return orden
# Funciones de ordenamiento
def merge_sort(catalogo,size,cmpfuncion):
    sub_list = lt.subList(catalogo, 1, size)
    sorted_list = ms.sort(sub_list,cmpfuncion)
    return sorted_list