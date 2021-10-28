﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

UFOfile = '/UFOS/UFOS-utf8-small.csv'
cont = None
# ___________________________________________________
#  Menu principal
# ___________________________________________________


def printMenu():
    print("\n")
    print("*******************************************"*3)
    print("Bienvenido")
    print("1- Cargar información de UFOS")
    print("2- Total de avistamientos en una ciudad")
    print("0- Salir")
    print("*******************************************"*3)


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n>')
    if int(inputs[0]) == 1:
        cont = controller.init()
        controller.loadData(cont, UFOfile)
        print('Total de avistamientos: ' + str(controller.UFOSize(cont)))
        print("Primeras 5")
        for posicion in range(5):
            print("*******************************************"*3)
            avistamiento = lt.getElement(cont["avistamientos"],posicion)
            print("Fecha: ",avistamiento["datetime"])
            print("Ciudad: ",avistamiento["city"])
            print("Estado: ",avistamiento["state"])
            print("Pais: ",avistamiento["country"])
            print("Forma: ",avistamiento["shape"])
            print("Duracion en segundos: ",avistamiento["duration (seconds)"])
            print("Duracion en horas/min: ",avistamiento["duration (hours/min)"])
            print("Comentarios: ",avistamiento["comments"])
            print("Fecha de publicacion: ",avistamiento["date posted"])
            print("Latitud: ",avistamiento["latitude"])
            print("Longitud: ",avistamiento["longitude"])
        print("*******************************************"*3)
        print("Últimas 5")
        for posicion in range(lt.size(cont["avistamientos"])-4,lt.size(cont["avistamientos"])+1):
            print("*******************************************"*3)
            avistamiento = lt.getElement(cont["avistamientos"],posicion)
            print("Fecha: ",avistamiento["datetime"])
            print("Ciudad: ",avistamiento["city"])
            print("Estado: ",avistamiento["state"])
            print("Pais: ",avistamiento["country"])
            print("Forma: ",avistamiento["shape"])
            print("Duracion en segundos: ",avistamiento["duration (seconds)"])
            print("Duracion en horas/min: ",avistamiento["duration (hours/min)"])
            print("Comentarios: ",avistamiento["comments"])
            print("Fecha de publicacion: ",avistamiento["date posted"])
            print("Latitud: ",avistamiento["latitude"])
            print("Longitud: ",avistamiento["longitude"])

    elif int(inputs[0]) == 2:
        print('Total de ciudades con avistamientos: ' + str(controller.indexSize(cont)))
        ciudad = input("Que ciudad desea consultar: ")
        avistamientos_ciudad = controller.avistamientos_ciudad(cont,ciudad)
        print("En la ciudad se dieron: ",lt.size(avistamientos_ciudad))
        if lt.size(avistamientos_ciudad) > 4:
            print("Primeras 3")
            for posicion in range(3):
                print("*******************************************"*3)
                avistamiento = lt.getElement(avistamientos_ciudad,posicion)
                print("Fecha: ",avistamiento["datetime"])
                print("Ciudad y País: ",avistamiento["city"],", ",avistamiento["country"])
                print("Forma: ",avistamiento["shape"])
                print("Duracion en segundos: ",avistamiento["duration (seconds)"])
            print("*******************************************"*3)
            print("Últimas 3")
            for posicion in range(lt.size(avistamientos_ciudad)-2,lt.size(avistamientos_ciudad)+1):
                print("*******************************************"*3)
                avistamiento = lt.getElement(avistamientos_ciudad,posicion)
                print("Fecha: ",avistamiento["datetime"])
                print("Ciudad y País: ",avistamiento["city"],", ",avistamiento["country"])
                print("Forma: ",avistamiento["shape"])
                print("Duracion en segundos: ",avistamiento["duration (seconds)"])
        else:
            print("Sus avistamientos son: ")
            for avistamiento in lt.iterator(avistamientos_ciudad):
                print("*******************************************"*3)
                print("Fecha: ",avistamiento["datetime"])
                print("Ciudad y País: ",avistamiento["city"],", ",avistamiento["country"])
                print("Forma: ",avistamiento["shape"])
                print("Duracion en segundos: ",avistamiento["duration (seconds)"])
    else:
        sys.exit(0)
sys.exit(0)