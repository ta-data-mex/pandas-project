# ExcelCalificaciones
Proyecto para concentrado y pequeño análisis de calificaciones provenientes de un varios documentos de excel

Este proyecto utiliza datos reales obtenidos durante el ultimo cuatrimestre del año 2018, que son calificaciones de alumnos, aunque no existe como tal una politica de privacidad, al ser documentos personales, no los voy a incluir en el proyecto, puesto que la primera parte del codigo se utiliza para extraer toda la informacion de los excel y subirlos a una base de datos de mongodb conectada a atlas.

La segunda parte del proyecto, se llevara a cabo la limpieza de los registros, comenzando con la eliminacion de la columna _id, que corresponde a una columna de mongo, despues se limpiarán los datos repetidos que se encuentren en el dataframe, la separacion de los datos por carreras.

-Promedio parcial de los alumnos por materia
-Promedio de materia por grupo
-Promedio del profesor por materia que imparte
-Promedio general del profesor
-Promedio general de la carrera por cada parcial
-Promedio general de la carrera por cuatrimestre
-Promedio de grupos por cuatrimestre

La idea es que se separen del dataframe original todos esos subdataframe siempre después de identificar y remover duplicados

Para la tercera parte del proyecto se realizarán los cálculos descritos en la parte de arriba.

Problemas a los que me enfrenté durante la segunda parte fueron a la separación de los datos por carrera, para hacerlos de forma automática,
Habia problemas con la escritura del nombre de las carreras, por decir algo, la carrera de ingeniería en sistemas computacionales, se encontraba con acento y sin acento en ingeniería
El reemplazo de los valores para ese dato, al hacerlo con loc, sustituia valores desconocidos por la frase de ingeniería, impidiendome el poder hacer algunos cálculos de prueba.


