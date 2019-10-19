# Project: Data Cleaning and Manipulation with Pandas

## Base de datos de concentración de monoxido de carbono en 4 estaciones monitoras de Londres en el periodo 01/01/2000 a 30/09/2019

El proceso seguido fue el siguiente

1. Importar las bibliotecas pandas y numpy (por si acaso)
2. Importar el archivo .csv a un data frame
3. Contar el número de registros por estación monitora
4. Revisión de columnas con valores nulos
5. Renombrado de columnas para dar mayor contexto y nombres más cortos
6. Revisión de valores extremos y de type de los datos
7. Separación del data frame en 4 data frames separados, 1 por estación
8. Eliminar columnas innecesarias por tener el mismo dato y por el contexto
9. Quitar los registros que tienen datos nulos en la medición de la concentración de CO, pues no se pueden sustituir por 0
10. Quitar los registros que tienen datos medidos pero no ratificados
11. Quitar la columna que indica la ratificación de los datos por innecesaria
12. Obtener las estadísticas descrptivas de cada data frame
13. Crear un nuevo data frame con las descripciones de cada uno de los otros
14. Exportar este data frame a un archivo .csv: estadisticas.csv
15. Transformación del dato de "fecha" a una fecha real de python de 1 data frame
16. Agrupación de datos de concentración de CO de 1 data frame por año y mes, se obtuvieron suma y promedio
17. Exportar data frame de promedios de concentración de CO por año y mes de 1 estación monitora, city_prom_mes.csv
