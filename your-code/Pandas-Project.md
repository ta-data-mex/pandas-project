                                            PANDAS-PROYECT

A contunuación se describirá brevemente los pasos que se siguieron para realizar este proyecto utilizando los métodos de data cleaning y data manipulation vistos en clase.

1. En primer lugar, fue necesario elegir una base de datos sobre la cual trabajar, en este caso la base utilizada fue "Top_1_000_Songs_To_Hear_Before_You_Die.csv".
2. En segundo lugar, fue necesario importar la librería de pandas a través del comando "import pandas as pd" y posteriormente para leerlo y abrirlo se utilizaron los comandos de "pd.read_csv".
3. Posteriormente, la base de datos la transformé en un data frame a través del comando "pd.DataFrame".
4. Me di cuenta que antes que nada hay que ver el tipo de valores que contiene nuestro data frame para poder analizarlos de mejor manera y para ello, utilicé el método de "data.dtype" para visuarlos.
5. Porque me interesaba ver la columnas para poder conceptualizar de mejor manera el data frame, utilicé la función de "data.columns".
6. Me pareció interesante visualizar cuántas canciones se lanzaron cada año, y por ello utilicé el comando de "value_counts".
7. Asimismo, también quise visualizar cuántas canciones tenía cada artista, y por ello utilicé nuevamente el método.
8. Cómo el data frame era de una lista mil canciones me era imposible visualizarlas todas en su conjunto pero a través de "values_counts", me fue posible vizualizar el número de canciones que tenía la columna "THEME" así como el número de sus categorías.
9. "Null" me ayudó para contabilizar y visualizar en qué columnas habia valores nulos.
10. Me pareció que la mejor manera para tratar esos valores vacios era llenarlos con ("-") y no eliminarlos, ya que solo fataban URLS pero las canciones si estaban dentro del data frame.
11. Con "filtered" pude filtrar pr año, artista y tema un valor en específico de mi data frame.
12. Utilice el método de "concat" (concatenación de fila) para juntar dos categorías de datos de la misma columna, en este caso ARTIST.
13. Con el método "min y max" pude sacar los valores de que canción era la más antigua y la más nueva.
14. Con el método "sort.values" puede ordenar de manera ascendente el nombre de los valores de la columna "ARTIST".
15. Utilicé el método "melt" para ir viendo por artista y año el tipo de valor que tenían de la columna THEME.


