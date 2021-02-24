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

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Encontrar buenos videos por categoría y país")
    print("3- Encontrar video tendencia por país")
    print("4- Encontrar video tendencia por categoría")
    print("5- Buscar los videos con más likes")

def initCatalog(estructuraDeDatos):
    return controller.initCatalog(estructuraDeDatos)

def loadData(catalog):
    controller.loadData(catalog)

def printBuenosVideos(videos):
    size = lt.size(videos)
    if size:
        print(' Estos son los mejores videos: ')
        for video in lt.iterator(videos):
            print('Título: '+ video['title']+ ' Trending Date: '+video['trending_date']+' Nombre del canal: '+ video['cannel_title']+ ' Fecha de publicación: '+video['publish_time']+' Reproducciones: '+video['views']+ ' Likes: '+video['likes']+ " Dislikes: "+video['dislikes'])
    else:
        print('No se encontraron videos')

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        num = int(input("¿Cuál estructura de datos desea utilizar? (1 para ARRAY_LIST/ 2 para SINGLE_LINKED_LIST)\n"))
        if num == 1:
            estructuraDeDatos = 'ARRAY_LIST'
        elif num == 2:
            estructuraDeDatos = 'SINGLE_LINKED_LIST'
        print("Cargando información de los archivos ....")
        catalog = initCatalog(estructuraDeDatos)
        loadData(catalog)
        print('Categorías cargados: '+str(lt.size(catalog['categories'])))
        print('Videos cargados: '+ str(lt.size(catalog['videos'])))
    elif int(inputs[0]) == 2:
        numeroDeElementos = int(input("¿Cuál es el número de datos que desea utilizar?"))
        num2 = int(input("¿Cuál algoritmo desea utilizar? (1 para shellsort/ 2 para insertionsort/3 para selectionsort)"))
        if num2 == 1:
            algoritmo = 'shellsort'
        elif num2 == 2:
            algoritmo = 'insertionsort'
        elif num2 == 3:
            algoritmo = 'selectionsort'
        resultado = controller.mejoresVideosPorViews(catalog, numeroDeElementos, algoritmo)
        print('Tiempo transcurrido y lista ordenada: '+ str(resultado))

    else:
        sys.exit(0)
sys.exit(0)
