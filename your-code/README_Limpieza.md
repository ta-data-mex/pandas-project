![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Project: Data Cleaning and Manipulation with Pandas

## Overview

La base de datos se obtuvo de: 

* [Goodreads books](https://www.kaggle.com/jealousleopard/goodreadsbooks)

La base de datos contiene la siguiente información organizada por columnas:
- bookID: un código (índice) de los libros contenidos en la base de datos. No son consecutivos, es decir pasan del 12,13,14 al 18.
- title: nombre del libro
- authors: autor o autores, organizado originalmente como [Nombre Apellido-Nombre2 Apellido2]. El Nombre2 y Apellido 2 corresponden al autor 2.
- average_rating: calificación promedio de los libros, por distintos usuarios
- ISBN: código ISBN a 10 dígitos del libro en cuestión
- ISBN13: código ISBN a 13 dígitos (para libros posteriores al 1 de enero de 2007)
- language_code: código a 3 o 5 digitos del idioma del libro
- #num_pages: número de páginas
- ratings_count: número de reseñas 
- text_reviews_count: número de reseñas textuales


## Proceso de Limpieza

1- Checar valores vacíos en columnas y eliminar aquellas con un alto ínidice de valores vacíos.
2.- Estandarízar nomenclatura del 'language_code':
	- en-CA, en-GB, en-US en eng
3.- Eliminar errores en los nombres de Autor(es):
	- eliminar el doble espacio,
	- cambiar forma de enlistar autores (de José Alfredo-Chente Fernandez a José Alfredo, Chente Fernandez
4.- Eliminar libros con:
	- 0 páginas
	- menos de 50 páginas
5.- Eliminar libros con un average_rating mayor a 0, sin embargo, con un rating_count mayor a 0.





## Otras acciones

- Agrupar en distintos DataFrames considerando el Average Rating.
- Ordenar de mayor a menor en función de la evaluación promedio, a la vez que se ordenó alfabeticamente en función del autor. 


## Recursos consultados:
- Learning
- Ejemplos anteriores
- Labs
- Documentación en internet
