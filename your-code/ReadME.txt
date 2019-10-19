Proyecto Limpieza de Datos
	Ramiro Maravilla


Escogí la muestra de Goodreads sobre libros.

Esta base contiene los registros de los libros que tienen una reseña y han sido calificados en el portal de GoodReads. 
La base de datos se puede encontrar en el siguiente link https://www.kaggle.com/jealousleopard/goodreadsbooks. 
La base sucia tiene 10 columnas y 13,719 filas. 

Las variables son:

bookID (int) - Contiene el número de libro 
title (object) - Contiene el título del libro
authors (object) - Contiene los autores
average_rating (object) - Contiene la calificación promedio del libro por los lectores
isbn (object) - Número único de identificación de la obra (ayuda a diferenciar diferentes ediciones de libros)
isbn13 (object) - Otro formato de isbn (redudante en mi opinión)
language_code (object) - Código del lenguaje del libro
num_pages (object) - Número de páginas
ratings_count (int) - número de veces que ha sido calificado en Goodreads
text_reviews_count (int) - Número de reseñas

Originalmente, las variables son cargadas de la siguiente manera:


Proceso de limpieza:
1) Se cargaron los paquetes 
2) Se cargó la base de datos
3) Hacemos una descripción general 
4) Eliminamos dos columnas que no nos sirven: Unnamed:10 y isbn113
5) Limpiamos la variable num_pages.
	En esta variable se identifó que tenía strings en vez de números.
	Igualamos a cero todos los strings en esta variable
	Tiramos todas las filas con num_pages = 0
	Después tiramos todas la filas con menos de 10 cuartillas porque eso no es libro
6) Limpiamos la variable average_ratings
	Tiramos todas las filas que tienen un rating de cadena
7) Limpiamos la variable language_code
	Homogenizamos los diferentes tipos de inglés (en-CA, en-GB, en-US) en uno solo
		Reemplazamos el "-" por nada
		Eliminamos CA, GB y US
		Reemplazamos "eng" por en. Todos los libros en inglés tienen el mismo código
8) Limpiamos la variable "text_reviews_count"
	Eliminamos todos los registros con menos de 5 reviews (decisión random)
9) Al promedio de ratings_count le sumo y resto una desviación estándar para quedarme
   con los registros de ratings que no han sido sobre calificados.
	Sumo al promedio de ratings una desviación. Elimino los que tengan más que eso
	Resto también desviación al promedio, como el número es negativo, establezco 
	un número mínimo de ratings de 100
10) Limpio authors.
	Hay muchos libros que tienen varios autores. Sustituyo desde el segundo autor por "et al."
11) isbn
	Limpio isb quitando todas las letras, sólo los números.
12) Limpio de titutlos y autores los carácteres en español (acentos y ñ) que no los lee
13) Espacios
	Sutituyo espacios dobles por un espacio
14) Reviso si hay duplicados en titulo, autor e isbn. No hay
15) Guardo la base de datos como libros_limpi3.csv