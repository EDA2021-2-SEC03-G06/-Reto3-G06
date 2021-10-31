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
 """

import config as cf
import model
import csv
import datetime

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def init():
    analyzer = model.newAnalyzer()
    return analyzer


#  Funciones para la carga de datos
def loadData(analyzer, UFOfile):
    UFOfile = cf.data_dir + UFOfile
    input_file = csv.DictReader(open(UFOfile, encoding="utf-8"),
                                delimiter=",")
    for avistamiento in input_file:
        model.addUFO(analyzer, avistamiento)
    return analyzer


# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def UFOSize(analyzer):
    return model.UFOSize(analyzer)

def indexHeight(analyzer):
    """
    Altura del indice (arbol)
    """
    return model.indexHeight(analyzer)


def indexSize(analyzer):
    """
    Numero de nodos en el arbol
    """
    return model.indexSize(analyzer)

def avistamientos_ciudad(analyser,ciudad):
    return model.avistamiento_ciudad(analyser,ciudad)

def avistamientos_fecha(analyser, fecha_inicio, fecha_fin):
    fecha_inicias = fecha_inicio[:10]
    fecha_inicias = datetime.datetime.strptime(fecha_inicias,"%Y-%m-%d")
    fecha_final = fecha_fin[:10]
    fecha_final = datetime.datetime.strptime(fecha_final,"%Y-%m-%d")
    return model.avistamientos_fecha(analyser,fecha_inicias,fecha_final)

def avistamientos_hora(analyser, hora_inicio, hora_fin):
    hora_i = datetime.datetime.strptime(hora_inicio,"%H:%M")
    hora_f = datetime.datetime.strptime(hora_fin,"%H:%M")
    return  model.avistamientos_hora(analyser,hora_i,hora_f)

def avistamientos_lugar(analyser,latitud_max,latitud_min,longitud_max,longitud_min):
    return model.avistamientos_lugar(analyser,latitud_max,latitud_min,longitud_max,longitud_min)