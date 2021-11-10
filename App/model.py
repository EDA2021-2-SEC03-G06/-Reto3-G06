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
import folium
assert cf
import time as chronos
import webbrowser

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newAnalyzer():
    analyzer = {'avistamientos': lt.newList(datastructure='SINGLE_LINKED'),
                'ciudad': om.newMap(omaptype='RBT'),
                'fecha' : om.newMap(omaptype='RBT'),
                'lugar' : om.newMap(omaptype="RBT"),
                'segundos' : om.newMap(omaptype="RBT"),
                'hora' : om.newMap(omaptype='RBT')
                }
    return analyzer


# Funciones para agregar informacion al catalogo


def addUFO(analyzer, UFO):
    lt.addLast(analyzer['avistamientos'], UFO)
    updateCity(analyzer['ciudad'], UFO)
    updateDate(analyzer['fecha'],UFO)
    updateSeconds(analyzer['segundos'],UFO)
    updateHour(analyzer['hora'],UFO)
    updateLatitude(analyzer['lugar'],UFO)
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

def updateDate(map, UFO):
    fecha_str = UFO["datetime"][:10]
    occurreddate = datetime.datetime.strptime(fecha_str,"%Y-%m-%d")
    entry = om.get(map,occurreddate)
    if entry is None:
        datentry = newDataEntry(UFO)
        om.put(map, occurreddate, datentry)
    else:
        datentry = me.getValue(entry)
    addCity(datentry, UFO)
    return map

def updateSeconds(map,UFO):
    segundos_str = UFO["duration (seconds)"]
    occurreddate = float(segundos_str)
    entry = om.get(map,occurreddate)
    if entry is None:
        datentry = newDataEntry(UFO)
        om.put(map, occurreddate, datentry)
    else:
        datentry = me.getValue(entry)
    addCity(datentry, UFO)
    return map

def updateHour(map,UFO):
    hora_str = UFO["datetime"][11:]
    occurreddate = datetime.datetime.strptime(hora_str,"%H:%M:%S")
    entry = om.get(map,occurreddate)
    if entry is None:
        datentry = newDataEntry(UFO)
        om.put(map, occurreddate, datentry)
    else:
        datentry = me.getValue(entry)
    addCity(datentry, UFO)
    return map

def updateLatitude(map,UFO):
    latitude = round(float(UFO["latitude"]),2)
    entry = om.get(map,latitude)
    if entry is None:
        datentry = newDataEntry(UFO)
        om.put(map, latitude, datentry)
    else:
        datentry = me.getValue(entry)
    addCity(datentry, UFO)
    return map

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
    start_time = chronos.process_time()
    lista = me.getValue(om.get(analyser["ciudad"],ciudad))
    lista = lista["lstUFOS"]
    lista_sorted = merge_sort(lista,lt.size(lista),cmpdatetime)
    stop_time = chronos.process_time()
    time = (stop_time - start_time)*1000
    print("se demoro: ", time)
    return lista_sorted

def avistamientos_segundos(analyser,s_min,s_max):
    """
    Primera parte del Req-2
    """
    start_time = chronos.process_time()
    high_key = om.maxKey(analyser['segundos'])
    tupla = om.get(analyser["segundos"],high_key)
    mayores = tupla["value"]["lstUFOS"]
    mayor_cantidad = lt.size(mayores)

    """
    Segunda parte del req-2
    """
    avistamientos = lt.newList(datastructure="ARRAY_LIST")
    s_inicio = s_min
    while s_inicio <= s_max:
        ufos = om.get(analyser['segundos'],s_inicio) 
        if ufos != None:
            ufos = me.getValue(ufos)
            ufos = ufos["lstUFOS"]
            for avistamiento in lt.iterator(ufos):
                lt.addLast(avistamientos,avistamiento)
        s_inicio += 0.5
    
    primeras_3 = lt.newList(datastructure="ARRAY_LIST")
    for posicion in range(4):
        lt.addLast(primeras_3,lt.getElement(avistamientos,posicion))
    ultimas_3 = lt.newList(datastructure="ARRAY_LIST")
    for posicion in range(lt.size(avistamientos)-3,lt.size(avistamientos)):
        lt.addLast(ultimas_3,lt.getElement(avistamientos,posicion))
    
    stop_time = chronos.process_time()
    time = (stop_time - start_time)*1000
    print("se demoro: ", time)
    return mayor_cantidad,primeras_3,ultimas_3

def avistamientos_fecha(analyser,fecha_inicias,fecha_final):
    start_time = chronos.process_time()
    fecha = fecha_inicias
    avistamientos = lt.newList(datastructure="ARRAY_LIST")
    while fecha <= fecha_final:
        avistamiento = om.get(analyser["fecha"],fecha)
        if avistamiento != None:
            avistamiento = me.getValue(avistamiento)
            avistamiento = avistamiento["lstUFOS"]
            for evento in lt.iterator(avistamiento):
                lt.addLast(avistamientos,evento)
        fecha += datetime.timedelta(1,0,0)
    avistamientos_sorted = merge_sort(avistamientos,lt.size(avistamientos),cmpdatetime)
    stop_time = chronos.process_time()
    time = (stop_time - start_time)*1000
    print("se demoro: ", time)
    return avistamientos_sorted

def avistamientos_hora(analyser,hora_inicio,hora_fin):
    start_time = chronos.process_time()
    mas_tarde = str(om.maxKey(analyser['hora']))[11:]
    avistamientos = lt.newList(datastructure="ARRAY_LIST")
    hora = hora_inicio
    while hora <= hora_fin:
        avistamiento = om.get(analyser["hora"],hora)
        if avistamiento != None:
            avistamiento = me.getValue(avistamiento)
            avistamiento = avistamiento["lstUFOS"]
            for evento in lt.iterator(avistamiento):
                lt.addLast(avistamientos,evento)
        hora += datetime.timedelta(minutes = 1)
    avistamientos_sorted = merge_sort(avistamientos,lt.size(avistamientos),cmptime)
    stop_time = chronos.process_time()
    time = (stop_time - start_time)*1000
    print("se demoro: ", time)
    return avistamientos_sorted, mas_tarde

def avistamientos_lugar(analyser,latitud_max,latitud_min,longitud_max,longitud_min):
    start_time = chronos.process_time()
    latitud = latitud_min
    avistamientos = lt.newList(datastructure='ARRAY_LIST')
    while latitud <= latitud_max:
        avistamiento = om.get(analyser['lugar'],latitud)
        if avistamiento != None:
            avistamiento = me.getValue(avistamiento)
            avistamiento = avistamiento["lstUFOS"]
            for evento in lt.iterator(avistamiento):
                if float(evento['longitude']) >= longitud_min and float(evento['longitude']) <= longitud_max:
                    lt.addLast(avistamientos,evento)
        latitud += 0.01
        latitud = round(latitud,2)
    avistamientos_sorted = merge_sort(avistamientos,lt.size(avistamientos),cmpPlace)
    
    
    #REQ 6
    latit_def = (latitud_max+latitud_min)/2
    long_def = (longitud_max+longitud_min)/2

    mapa = folium.Map(location=[latit_def,long_def],zoom_start=4)

    for avistamiento in lt.iterator(avistamientos_sorted):
        folium.Marker(location=[float(avistamiento["latitude"]),float(avistamiento['longitude'])]).add_to(mapa)

    mapa.save(cf.data_dir +"/UFOS/mapita.html")
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    webbrowser.open(cf.data_dir +"/UFOS/mapita.html")
    
    stop_time = chronos.process_time()
    time = (stop_time - start_time)*1000
    print("se demoro: ", time)
    return avistamientos_sorted

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpdatetime(UFO1,UFO2):
    orden = None
    if (UFO1["datetime"]!="") and (UFO2["datetime"]!=""):
        orden = (datetime.datetime.strptime(UFO1["datetime"],"%Y-%m-%d %H:%M:%S") > datetime.datetime.strptime(UFO2["datetime"],"%Y-%m-%d %H:%M:%S"))
    return orden

def cmp_req2(UFO1,UFO2):
    orden = None
    if (UFO1["duration (seconds)"]!="") and (UFO2["duration (seconds)"]!=""):
        if UFO1["duration (seconds)"] == UFO2["duration (seconds)"]:
            if (UFO1["country"]!="") and (UFO2["country"]!=""):
                if UFO1["country"] == UFO2["country"]:
                    if (UFO1["city"]!="") and (UFO2["city"]!=""):
                        orden = UFO1["city"] > UFO2["city"]
                else:
                    orden = UFO1["country"] > UFO2["country"]
        else:
            orden = UFO1["duration (seconds)"] > UFO2["duration (seconds)"]
    return orden

def cmptime(UFO1,UFO2):
    orden = None
    if (UFO1["datetime"]!="") and (UFO2["datetime"]!=""):
        if (datetime.datetime.strptime(UFO1["datetime"][11:],"%H:%M:%S") > datetime.datetime.strptime(UFO2["datetime"][11:],"%H:%M:%S")):
            orden = True
        elif (datetime.datetime.strptime(UFO1["datetime"][11:],"%H:%M:%S") == datetime.datetime.strptime(UFO2["datetime"][11:],"%H:%M:%S")) and (datetime.datetime.strptime(UFO1["datetime"][:10],"%Y-%m-%d") > datetime.datetime.strptime(UFO2["datetime"][:10],"%Y-%m-%d")):
            orden = True
        else:
            orden = False
    return orden

def cmpPlace(UFO1,UFO2):
    orden = None
    if (UFO1["latitude"]!="") and (UFO2["latitude"]!=""):
        if round(float(UFO1['latitude']),2) > round(float(UFO2['latitude']),2):
            orden = True
        elif round(float(UFO1['latitude']),2) == round(float(UFO2['latitude']),2) and round(float(UFO1['longitude']),2) > round(float(UFO2['longitude']),2):
            orden = True
        else:
            orden = False
    return orden


# Funciones de ordenamiento
def merge_sort(catalogo,size,cmpfuncion):
    sub_list = lt.subList(catalogo, 1, size)
    sorted_list = ms.sort(sub_list,cmpfuncion)
    return sorted_list