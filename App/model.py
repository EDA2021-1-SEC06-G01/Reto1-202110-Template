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
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as sele
from DISClib.Algorithms.Sorting import mergesort as merge
from DISClib.Algorithms.Sorting import quicksort as quick
import time
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog(estructuraDeDatos):
    catalog = {'videos': None,
               'categories': None,
               'country':None,
               'likes':None}
    
    catalog['videos'] = lt.newList(estructuraDeDatos,
                                    cmpfunction= cmpVideosByViews)
    catalog['categories'] = lt.newList(estructuraDeDatos)
    catalog['country'] = lt.newList(estructuraDeDatos)
    catalog['likes'] = lt.newList(estructuraDeDatos)
    return catalog



# Funciones para agregar informacion al catalogo
def addCategory(catalog, elem):
    lt.addLast(catalog['categories'], elem)

def addVideo(catalog, elem):
    lt.addLast(catalog['videos'],elem)

# Funciones para creacion de datos
def newCategory(id):
    catalog = {'id':''}
    catalog['id'] = id
    return catalog

def newVideo(title, id):
    video = {'title':'','video_id':''}
    video['title'] = title
    video['video_id'] = id
    return video


# Funciones de consulta


# Funciones utilizadas para comparar elementos dentro de una lista
def cmpVideosByViews(video1, video2):
    #Retorna True si los 'views' del video1 son menores que los del video2
    if float(video1['views']) > float(video2['views']):
        return True
    else:
        return False

<<<<<<< HEAD



=======
def cmpVideosByTrends(video1, video2):
    contadorV1 = 0
    contadorV2 = 0
    for video in catalog['videos']:
        if video['video_id']==video1['video_id']:
            contadorV1 += 1
        elif video['video_id']==video2['video_id']:
            contadorV2 += 1
    if contadorV1 > contadorV2:
        return True
    else:
        return False
>>>>>>> da30781b732a466bea659cfeeb8b52eee3dc41a3

# Funciones de ordenamiento
def mejoresVideosPorViews(catalog, numeroDeElementos, algoritmo):
    sub_list = lt.subList(catalog['videos'], 1, numeroDeElementos)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    if algoritmo == "shellsort":
        sorted_list = sa.sort(sub_list, cmpVideosByViews)
    elif algoritmo == "insertionsort":
        sorted_list = ins.sort(sub_list, cmpVideosByViews)
    elif algoritmo == "selectionsort":
        sorted_list = sele.sort(sub_list, cmpVideosByViews)
    elif algoritmo == "mergesort":
        sorted_list = merge.sort(sub_list, cmpVideosByViews)
    elif algoritmo == "quicksort":
        sorted_list = quick.sort(sub_list, cmpVideosByViews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time -start_time)*1000
    return elapsed_time_mseg, sorted_list


<<<<<<< HEAD
def videostendenciaporpais(catalog, categorias, pais,numero):

    sub_list = lt.subList(catalog['videos'], 1, (numero+1))
    sub_list = sub_list.copy()
    sorted_list = sa.sort(sub_list,cmpVideosByViews)
    for i in sorted_list['country']:
        paises = lt.getElement(sorted_list['country'], i)
        lt.addFirst(sorted_list,paises)
    return sorted_list 




    






=======


def videosTendenciaPorCategoria(catalog, categoria):
    sublista = lt.newList(datastructure="ARRAY_LIST", cmpfunction=None)
    poscategoria = lt.isPresent(catalog['categories'], categoria)
    categoria = lt.getElement(catalog['categories'], poscategoria)
    for videos in catalog['videos']:
        if video['categories'] == categoria:
            lt.addFirst(sublista, video)
    start_time = time.process_time()
    sorted_list = merge.sort(sublista, cmpVideosByTrends)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time-start_time)*1000
    return elapsed_time_mseg, sorted_list
>>>>>>> da30781b732a466bea659cfeeb8b52eee3dc41a3

