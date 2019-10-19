Proyecto Limpieza de Datos
	Ramiro Maravilla


Escog� la muestra de Goodreads sobre libros.

Esta base contiene los registros de los libros que tienen una rese�a y han sido calificados en el portal de GoodReads. 
La base de datos se puede encontrar en el siguiente link https://www.kaggle.com/jealousleopard/goodreadsbooks. 
La base sucia tiene 10 columnas y 13,719 filas. 

Las variables son:

bookID (int) - Contiene el n�mero de libro 
title (object) - Contiene el t�tulo del libro
authors (object) - Contiene los autores
average_rating (object) - Contiene la calificaci�n promedio del libro por los lectores
isbn (object) - N�mero �nico de identificaci�n de la obra (ayuda a diferenciar diferentes ediciones de libros)
isbn13 (object) - Otro formato de isbn (redudante en mi opini�n)
language_code (object) - C�digo del lenguaje del libro
num_pages (object) - N�mero de p�ginas
ratings_count (int) - n�mero de veces que ha sido calificado en Goodreads
text_reviews_count (int) - N�mero de rese�as

Originalmente, las variables son cargadas de la siguiente manera:


Proceso de limpieza:
1) Se cargaron los paquetes 
2) Se carg� la base de datos
3) Hacemos una descripci�n general 
4) Eliminamos dos columnas que no nos sirven: Unnamed:10 y isbn113
5) Limpiamos la variable num_pages.
	En esta variable se identif� que ten�a strings en vez de n�meros.
	Igualamos a cero todos los strings en esta variable
	Tiramos todas las filas con num_pages = 0
	Despu�s tiramos todas la filas con menos de 10 cuartillas porque eso no es libro
6) Limpiamos la variable average_ratings
	Tiramos todas las filas que tienen un rating de cadena
7) Limpiamos la variable language_code
	Homogenizamos los diferentes tipos de ingl�s (en-CA, en-GB, en-US) en uno solo
		Reemplazamos el "-" por nada
		Eliminamos CA, GB y US
		Reemplazamos "eng" por en. Todos los libros en ingl�s tienen el mismo c�digo
8) Limpiamos la variable "text_reviews_count"
	Eliminamos todos los registros con menos de 5 reviews (decisi�n random)
9) Al promedio de ratings_count le sumo y resto una desviaci�n est�ndar para quedarme
   con los registros de ratings que no han sido sobre calificados.
	Sumo al promedio de ratings una desviaci�n. Elimino los que tengan m�s que eso
	Resto tambi�n desviaci�n al promedio, como el n�mero es negativo, establezco 
	un n�mero m�nimo de ratings de 100
10) Limpio authors.
	Hay muchos libros que tienen varios autores. Sustituyo desde el segundo autor por "et al."
11) isbn
	Limpio isb quitando todas las letras, s�lo los n�meros.
12) Limpio de titutlos y autores los car�cteres en espa�ol (acentos y �) que no los lee
13) Espacios
	Sutituyo espacios dobles por un espacio
14) Reviso si hay duplicados en titulo, autor e isbn. No hay
15) Guardo la base de datos como libros_limpi3.csv