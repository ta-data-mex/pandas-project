Primero importe el archivo de accidentes aéreos
Cambié las cabeceras (1)
Validé que no existieran registros repetidos (2)
Decidí dividir los datos entre datos númericos que podría realizar operaciones matematicas (int) por lo que seleccione 3 columnas: aboard, fatalities y ground. Me parecieron los datos más relevantes. (3)
Decidí homogenizar dichas columnas (data cleaning) y colocarles valor cero a aquellos registros con los que no se contaban información ('?') (4).
Asimismo, limpie la columna local_time que presentaban errores. (5)
Decidí sumar las columnas Date y local_time. Al ser strings no pude modificarlas para dado que queria cambiarla de formato hacia 'Date_time (pd.to_datetime). (6)
Generé una nueva columna ('Total_death') que suman 'fatalties' y 'ground' para poder identificar el total de fallecidos por los accidentes.
Y comence a explorar la data de fallecidos. (7)

Luego quise identificar una incongruencia con los datos. Pensar que las personas en el avión (aboard = pasajeros + crew) es menor que las fatalities (muertes de pasajeros +crew) conduciria a pensar que se tratan de registros erroneos, pero no olvidar que el valor faltante ("?") fue convertido en cero. (8)
Por último, realice trabajos con la varianza y los rangos interquartiles para identificar aquellos valores fuera del rango.
Finalmente exporte el archivo resultante hacia un formato .csv 