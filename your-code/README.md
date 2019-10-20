![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Project: Data Cleaning and Manipulation with Pandas

## Plane Crashings

El archivo original planecrash.csv es una base que contiene informaciòn sobre accidentes aèreos

* 13 columnas
* 5784 renglones
* Fecha, Hora,lugar,nùmero de vuelo,nùmero de registro,
* Tipo de transporte,tipo de vuelo,nùmero de pasajeros y descripciòn del accidente


**
--

## Mis pasos fueron los siguientes:


*Importar numpy y pandas

*Importar el csv y revisar los datos.

*Convertì los '?' en nulls, y eliminè las columnas que no contenian suficiente informaciòn

*La columna "time" tenìa bastantes detalles asì que elminè los caracteres extraños. 

* Tranpuse la base para ver los nulls por rows y eliminè las que tenìan mas de la mitad de los datos en null

*Para limpiar las columnas de "aboard" y "fatalities" empecè remplazando los caracteres extraños.
Cada dato incluia total pasajeros, total del crew y total de personas en el aviòn, asì que delimitè por espacios para sacar el 
total de personas y lo incluì en en 2 nuevas columnas ("Total_Passengers",Total_Fatalities").
Despuès delimite por ":" y separè el total del Crew de cada una en nuevas columnas.
Eliminè las rows cuando los datos de estas ultimas dos columnas eran null.
Calcule el total de pasajeros que no eran del crew restando el Total-Crew.


* Para la columna de "route" revisè la frecuencia de los datos, homologuè Test con Test Flight, y los campos que incluìan destinos los reemplacè por commercial.
Antes creè una copia de dicha columna para almacenar ahi los destinos de los vuelos comerciales("Route").

*Reacomodè las columnas y exportè a plane_crash.csv
