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
from DISClib.Algorithms.Sorting import insertionsort
from DISClib.Algorithms.Sorting import selectionsort
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog(id):
    catalog = {'videos': None,
               'categories': None,
               'country':None,
               'likes':None}
    
    catalog['videos'] = lt.newList('SINGLE_LINKED')
    catalog['categories'] = lt.newList('SINGLE_LLINKED')
    catalog['country'] = lt.newList('SINGLE_LINKED')
    catalog['likes'] = lt.newList('SINGLE_LINKED')

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
def mejoresVideosPorViews(catalog, estructuraDeDatos, numeroDeElementos, algoritmo):
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento