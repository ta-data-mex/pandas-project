
**``README.md`` file** containing a detailed explanation of the process followed in the importing, cleaning, manipulation, and exporting of your data as well as your results, obstacles encountered, and lessons learned.

*Importación
Para este proyecto descargue la data denominada: Big cities health. La fuente fue: https://data.world/health/big-cities-health
Al tratarse de un archivo csv que se podía descargar no se tuvo que crear una nueva conexión, pues se desargó el csv. 

Inicio:
Importar pandas y numpy. 

*Inicia el proceso de limpieza y export 

1. Se lee un nuevo Data Frame
2. Se identifican las columnas con mayor número de datos nulos. 
3. Se identifican las colunnas a descartar con más de mil datos nulos.
4. Se descartan las columnas para quedarnos con un Data set homogéneo. Cabe mencionar que la columna Values no se modifica porque sólo se detectan 13 nulls en el universo. 
5. Se cambia el nombre de una columna para poder dar un mejor contexto de lo que se trata, en lugar de "Indicator Category" se renombra como "Health Probles".
6. Se saca una radiografía de los tipos de problemas más recurrentes sumando la columna Value que indica la prevalencia a la proporción de individuos de dicho índice.
7. Los valores del Data Frame se reordenan por: 'Year', 'Health Problems','Gender'.
8. Se exporta la base de datos limpia y ordenada. 


*Inicia la parte del análisis y manipulación de datos. 
9. Se busca el valor máximo del set. 
10. Se busca el valor mínimo del set. 
11. Se hace una descripción del set. 
12. Se crea una clasificación de bins en tres niveles. En este paso se clasifican los niveles. 
13. Se aplican los niveles con .cut. 
14. Para continuar analizando y manipulando se utiliza el método.loc  para ubicr en el set los datos del set que empiezan con la palabra "Infant", de esta forma se conoce que en este set que empieza desde el año del 2003, fue hasta 2010 cuando se incluyen estudios de Mortalidad Infantil en Bostón. 
15. Luego se crea un DataFrame temporal que incluye los datos de todos los estudios de Cancer. 
16. Se secribe el nuevo Data Frame. 
17. Se utiliza .groupby para obtener la sumatoria de la prevalencia de Cancer por grupo etareo, se suma y se incluye en orden ascendente.

*Obstáculos: 
Lo que más se me dificultó de este proyecto fue saber cuántos métodos podrían entrar o dónde van los métodos para sumar, ordenar, agrupar. 

*Lecciones aprendidas: 
Aparentemente era algo sencillo porque la base de datos estaba pequeña, y con mucha información de strings muy diferente. Inicié con un challengue de clasificar la columna de indicadores para "separar" datos. Pero aún no lo conluyo...