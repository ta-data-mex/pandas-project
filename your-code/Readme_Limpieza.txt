Pasos tomados para la limpieza:
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

6.- Agrupar en distintos DF considerando el Average Rating.