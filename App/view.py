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

def initCatalog():
    return controller.initCatalog()

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
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print('Categorías cargados: '+str(lt.size(catalog['category_id'])))
        print('Videos cargados: '+ str(lt.size(catalog['videos-small'])))
    elif int(inputs[0]) == 2:
        categoria = input("Indique el nombre de la categoría: ")
        pais = input("Indique el país: ")
        n = int(input("Indique el número de videos para listar: "))
        catalog = initCatalog()
        print("Cargando los videos más buenos...")
        videos = controller.getBuenosVideos(catalog, categoria, pais, n)
        printBuenosVideos(videos)

    else:
        sys.exit(0)
sys.exit(0)
