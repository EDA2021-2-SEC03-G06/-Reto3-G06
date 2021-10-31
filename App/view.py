"""
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
from tabulate import tabulate
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
    print("3- Contar Avistamientos por duracion")
    print("4- Contar Avistamientos por Hora/Minuto")
    print("5- Contar los Avistamientos en un rango de fechas")
    print("6- Contar los avistamientos de una zona geografica")
    print("7- Visualizar los avistamientos de una zona geografica")
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
        print("Ultimas 5")
        for posicion in range(5):
            print("*******************************************"*3)
            avistamiento = lt.getElement(cont["avistamientos"],posicion)
            rta = [["Fecha: ",avistamiento["datetime"]],
            ["Ciudad: ",avistamiento["city"]],
            ["Estado: ",avistamiento["state"]],
            ["Pais: ",avistamiento["country"]],
            ["Forma: ",avistamiento["shape"]],
            ["Duracion en segundos: ",avistamiento["duration (seconds)"]],
            ["Duracion en horas/min: ",avistamiento["duration (hours/min)"]],
            ["Comentarios: ",avistamiento["comments"]],
            ["Fecha de publicacion: ",avistamiento["date posted"]],
            ["Latitud: ",avistamiento["latitude"]],
            ["Longitud: ",avistamiento["longitude"]]]
            print(tabulate(rta,tablefmt='grid'))
        print("*******************************************"*3)
        print("Primeras 5")
        for posicion in range(lt.size(cont["avistamientos"])-4,lt.size(cont["avistamientos"])+1):
            print("*******************************************"*3)
            avistamiento = lt.getElement(cont["avistamientos"],posicion)
            rta = [["Fecha: ",avistamiento["datetime"]],
            ["Ciudad: ",avistamiento["city"]],
            ["Estado: ",avistamiento["state"]],
            ["Pais: ",avistamiento["country"]],
            ["Forma: ",avistamiento["shape"]],
            ["Duracion en segundos: ",avistamiento["duration (seconds)"]],
            ["Duracion en horas/min: ",avistamiento["duration (hours/min)"]],
            ["Comentarios: ",avistamiento["comments"]],
            ["Fecha de publicacion: ",avistamiento["date posted"]],
            ["Latitud: ",avistamiento["latitude"]],
            ["Longitud: ",avistamiento["longitude"]]]
            print(tabulate(rta,tablefmt='grid'))

    elif int(inputs[0]) == 2:
        print('Total de ciudades con avistamientos: ' + str(controller.indexSize(cont)))
        ciudad = input("Que ciudad desea consultar: ")
        avistamientos_ciudad = controller.avistamientos_ciudad(cont,ciudad)
        print("En la ciudad se dieron: ",lt.size(avistamientos_ciudad))
        if lt.size(avistamientos_ciudad) > 4:
            print("Primeras 3")
            for posicion in range(1,4):
                print("*******************************************"*3)
                avistamiento = lt.getElement(avistamientos_ciudad,posicion)
                rta = [["Fecha: ",avistamiento["datetime"]],
                ["Ciudad y País: ",(avistamiento["city"],", ",avistamiento["country"])],
                ["Forma: ",avistamiento["shape"]],
                ["Duracion en segundos: ",avistamiento["duration (seconds)"]]]
                print(tabulate(rta,tablefmt='grid'))
            print("*******************************************"*3)
            print("Últimas 3")
            for posicion in range(lt.size(avistamientos_ciudad)-2,lt.size(avistamientos_ciudad)+1):
                print("*******************************************"*3)
                avistamiento = lt.getElement(avistamientos_ciudad,posicion)
                rta = [["Fecha: ",avistamiento["datetime"]],
                ["Ciudad y País: ",(avistamiento["city"],", ",avistamiento["country"])],
                ["Forma: ",avistamiento["shape"]],
                ["Duracion en segundos: ",avistamiento["duration (seconds)"]]]
                print(tabulate(rta,tablefmt='grid'))
        else:
            print("Sus avistamientos son: ")
            for avistamiento in lt.iterator(avistamientos_ciudad):
                print("*******************************************"*3)
                rta = [["Fecha: ",avistamiento["datetime"]],
                ["Ciudad y País: ",(avistamiento["city"],", ",avistamiento["country"])],
                ["Forma: ",avistamiento["shape"]],
                ["Duracion en segundos: ",avistamiento["duration (seconds)"]]]
                print(tabulate(rta,tablefmt='grid'))
    elif int(inputs[0]) == 3:
        s_min = float(input("Ingrese el límite inferior en segundos: "))
        s_max = float(input("Ingrese el límite superior en segundos: "))
        mayor_cantidad,primeras_3,ultimas_3 = controller.avistamientos_segundos(cont,s_min,s_max)
        print("Los avistamientos con la mayor duración fueron una cantidad de: "+str(mayor_cantidad))
        print("Primeras 3")
        for posicion in range(1,4):
            print("*******************************************"*3)
            avistamiento = lt.getElement(primeras_3,posicion)
            rta = [["Fecha: ",avistamiento["datetime"]],
            ["Ciudad y País: ",(avistamiento["city"],", ",avistamiento["country"])],
            ["Forma: ",avistamiento["shape"]],
            ["Duracion en segundos: ",avistamiento["duration (seconds)"]]]
            print(tabulate(rta,tablefmt='grid'))
        print("*******************************************"*3)
        print("Últimas 3")
        for posicion in range(1,4):
            print("*******************************************"*3)
            avistamiento = lt.getElement(ultimas_3,posicion)
            rta = [["Fecha: ",avistamiento["datetime"]],
            ["Ciudad y País: ",(avistamiento["city"],", ",avistamiento["country"])],
            ["Forma: ",avistamiento["shape"]],
            ["Duracion en segundos: ",avistamiento["duration (seconds)"]]]
            print(tabulate(rta,tablefmt='grid'))

    elif int(inputs[0]) == 4:
        hora_inicio = input("ingrese la hora inicial: ")
        hora_fin = input("ingrese la hora final: ")
        avistamientos, mas_tarde = controller.avistamientos_hora(cont,hora_inicio,hora_fin)
        print("El avistamiento mas tarde es a las: ",mas_tarde)
        print("En ese rango de horas hubo: ",lt.size(avistamientos))
        if lt.size(avistamientos) > 4:
            print("Primeras 3")
            for posicion in range(1,4):
                print("*******************************************"*3)
                avistamiento = lt.getElement(avistamientos,posicion)
                rta = [["Fecha: ",avistamiento["datetime"]],
                ["Ciudad y País: ",(avistamiento["city"],", ",avistamiento["country"])],
                ["Forma: ",avistamiento["shape"]],
                ["Duracion en segundos: ",avistamiento["duration (seconds)"]]]
                print(tabulate(rta,tablefmt='grid'))
            print("*******************************************"*3)
            print("Últimas 3")
            for posicion in range(lt.size(avistamientos)-2,lt.size(avistamientos)+1):
                print("*******************************************"*3)
                avistamiento = lt.getElement(avistamientos,posicion)
                rta = [["Fecha: ",avistamiento["datetime"]],
                ["Ciudad y País: ",(avistamiento["city"],", ",avistamiento["country"])],
                ["Forma: ",avistamiento["shape"]],
                ["Duracion en segundos: ",avistamiento["duration (seconds)"]]]
                print(tabulate(rta,tablefmt='grid'))
        else:
            print("Sus avistamientos son: ")
            for avistamiento in lt.iterator(avistamientos):
                print("*******************************************"*3)
                rta = [["Fecha: ",avistamiento["datetime"]],
                ["Ciudad y País: ",(avistamiento["city"],", ",avistamiento["country"])],
                ["Forma: ",avistamiento["shape"]],
                ["Duracion en segundos: ",avistamiento["duration (seconds)"]]]
                print(tabulate(rta,tablefmt='grid'))
    
    elif int(inputs[0]) == 5:
        fecha_inicio = input("Ingrese la fecha inicial: ")
        fecha_fin = input("Ingrese la fecha final: ")
        avistamientos_fecha = controller.avistamientos_fecha(cont,fecha_inicio,fecha_fin)
        print("En esas fecha ubo: ",lt.size(avistamientos_fecha)," avistamientos")
        if lt.size(avistamientos_fecha) > 4:
            print("Primeras 3")
            for posicion in range(1,4):
                print("*******************************************"*3)
                avistamiento = lt.getElement(avistamientos_fecha,posicion)
                rta = [["Fecha: ",avistamiento["datetime"]],
                ["Ciudad y País: ",(avistamiento["city"],", ",avistamiento["country"])],
                ["Forma: ",avistamiento["shape"]],
                ["Duracion en segundos: ",avistamiento["duration (seconds)"]]]
                print(tabulate(rta,tablefmt='grid'))
            print("*******************************************"*3)
            print("Últimas 3")
            for posicion in range(lt.size(avistamientos_fecha)-2,lt.size(avistamientos_fecha)+1):
                print("*******************************************"*3)
                avistamiento = lt.getElement(avistamientos_fecha,posicion)
                rta = [["Fecha: ",avistamiento["datetime"]],
                ["Ciudad y País: ",(avistamiento["city"],", ",avistamiento["country"])],
                ["Forma: ",avistamiento["shape"]],
                ["Duracion en segundos: ",avistamiento["duration (seconds)"]]]
                print(tabulate(rta,tablefmt='grid'))
        else:
            print("Sus avistamientos son: ")
            for avistamiento in lt.iterator(avistamientos_fecha):
                print("*******************************************"*3)
                rta = [["Fecha: ",avistamiento["datetime"]],
                ["Ciudad y País: ",(avistamiento["city"],", ",avistamiento["country"])],
                ["Forma: ",avistamiento["shape"]],
                ["Duracion en segundos: ",avistamiento["duration (seconds)"]]]
                print(tabulate(rta,tablefmt='grid'))
    
    elif int(inputs[0]) == 6:
        longitud_max = round(float(input("Ingrese la longitud superior: ")),2)
        longitud_min = round(float(input("Ingrese la longitud inferior: ")),2)
        latitud_max = round(float(input("Ingrese la latitud superior: ")),2)
        latitud_min = round(float(input("Ingrese la latitud inferior: ")),2)
        avistamientos = controller.avistamientos_lugar(cont,latitud_max,latitud_min,longitud_max,longitud_min)
        print("En ese rango de área hubo: ",lt.size(avistamientos))
        if lt.size(avistamientos) > 6:
            print("Primeras 3")
            for posicion in range(1,6):
                print("*******************************************"*3)
                avistamiento = lt.getElement(avistamientos,posicion)
                rta = [["Fecha: ",avistamiento["datetime"]],
                ["Ciudad y País: ",(avistamiento["city"],", ",avistamiento["country"])],
                ["Forma: ",avistamiento["shape"]],
                ["Duracion en segundos: ",avistamiento["duration (seconds)"]],
                ["latitude", avistamiento["latitude"]],
                ["longitud", avistamiento["longitude"]]]
                print(tabulate(rta,tablefmt='grid'))
            print("*******************************************"*3)
            print("Últimas 3")
            for posicion in range(lt.size(avistamientos)-4,lt.size(avistamientos)+1):
                print("*******************************************"*3)
                avistamiento = lt.getElement(avistamientos,posicion)
                rta = [["Fecha: ",avistamiento["datetime"]],
                ["Ciudad y País: ",(avistamiento["city"],", ",avistamiento["country"])],
                ["Forma: ",avistamiento["shape"]],
                ["Duracion en segundos: ",avistamiento["duration (seconds)"]],
                ["latitude", avistamiento["latitude"]],
                ["longitud", avistamiento["longitude"]]]
                print(tabulate(rta,tablefmt='grid'))
        else:
            print("Sus avistamientos son: ")
            for avistamiento in lt.iterator(avistamientos):
                print("*******************************************"*3)
                rta = [["Fecha: ",avistamiento["datetime"]],
                ["Ciudad y País: ",(avistamiento["city"],", ",avistamiento["country"])],
                ["Forma: ",avistamiento["shape"]],
                ["Duracion en segundos: ",avistamiento["duration (seconds)"]],
                ["latitude", avistamiento["latitude"]],
                ["longitud", avistamiento["longitude"]]]
                print(tabulate(rta,tablefmt='grid'))
    
    elif int(inputs[0]) == 7:
        print("En desarrollo")
    else:
        sys.exit(0)
sys.exit(0)