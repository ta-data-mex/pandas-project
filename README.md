![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Project: Data Cleaning and Manipulation with Pandas

## Descripción

Se utilizó la información del siguiente link:

* [Plane crashes](https://www.kaggle.com/nguyenhoc/plane-crash)

La base limpia se encuentra en el documento llamado: **plane_crash_clean.csv** dentro de la carpeta **Lab**

---

## Procedimiento:

* 1.- Despues de descargar la información en un archivo csv planecrashinfo_20181121001952.csv, se importa utilizando pandas.read_csv.
* 2.- Las columnas de 'aboard' y 'fatalities' contienen datos del total de pasajeros a bordo y fallecidos separados por tripulación y pasajeros,
*     así que se separan estas columnas en tres cada una y se obtienen los datos númericos obtenido 6 columnas más en total.
* 	  Estas columnas se agregan al dataframe original ultilizando el index correspondiente.
* 3.- Se limpia el dataframe plane_crashes de los símbolos '?' y se les asigna un valor nulos para trabajar con ellos.
* 4.- Se escogen las columnas con más de 1000 datos nulos para eliminarlas. En esta lista tambien se agrega 'registration', 'aboard' y 'fatalities'.
*	  Ya que 'registration' no tiene mucha relevancia y las otras dos columnas ya se separaron en unas nuevas columnas en el paso 2.
* 5.- En las columnas que se tienen datos númericos se cambian los valores nulos por ceros para evitar errores.
* 6.- Se cambian las columnas con datos númericos a tipo int. Todas las demas columnas son tipo Object.
* 7.- Tambien se cambia la columna de date a un formato de fecha dia/mes/año y se convierte a tipo date.
* 8.- Existen unas columnas en las que los totales de personas abordo y personas fallecidas no es correcto, ya que no cuadra con
*  	  con la suma de pasajeros y tripulación. Se corrigen las filas necesarias.
* 9.- Se muestran las estadísticas generales del dataframe.
* 10.- Se modifica el orden de las columnas y finalmente se crea el archivo plane_crash_clean.csv con el dataframe resultante.

