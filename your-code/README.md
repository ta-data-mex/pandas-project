{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Escogí una base de datos de la información de bateo del baseball porque muchas de las bases de datos que encontraba estaban bastante arregladas y esta en especial me daba la oportunidad de modificar, eliminar y agregar cosas.\n",
    "\n",
    "Lo primero que hice fue descargar el archivo csv y leerlo en Jupiter con Pandas. Me di cuenta de que no traía los nombres de los jugadores, sólo si ID, y ademas de que las fechas eran de antes de que iniciara la MLB. \n",
    "\n",
    "Entonces como yo quería sacar la información solo de la MLB me concentré en la columna de lgID (leage id) y los Null values los pase a 0 para más adelante eliminar las filas que dieran información de antes de la formación de la MLB en 1876.\n",
    "\n",
    "Después busque un dataframe que tuviera por lo menos el nombre de los jugadores y su id para poder juntar las tablas. Encontré la información pero venía con muchos otros datos que para este caso no necesitaba. Por lo que hice otra tabla con sólo los datos que me podrían servir (playerid, nombre, apellido, de que lado bateaba batea, la fecha de su debut y la de su ultimo juego)\n",
    "\n",
    "Hice un merge de las dos tablas tomando como referencia player id llamando batting a la tabla principal.\n",
    "\n",
    "Cheque que columnas tenían null values y si esas columnas eran de valores numéricos los rellenaba con 0. \n",
    "En el case de debut y final game también los Cambie for 0 para poder eliminarlos más fácil después.\n",
    "\n",
    "Ahora solo las columnas de nombre y bateo con izq o der tenían nulls entonces primero pensé en rellenar la columna de bats con una estimación basada en la proporción de todos los demás bateadores, es decir, si del 100% de los bateadores 50% eran derechos, 30% zurdos y 20% ambos. Rellenar los 1926 faltantes con esa proporción por lo que saque dichos porcentajes, pero después pensé que esto sería alterar la información y como no necesitaba el porcentaje de bateadores, y si lo necesitara más adelante seria el mismo que sin esos valores. Entonces decidí hacer lo mismo que con los nombres y remplace el NaN por “-“ para entender que o no se le conocía por su primer nombre o que no se sabe si era zurdo o derecho.\n",
    "\n",
    "Después saque los indices de los valores 0 en las columnas debut (no lo hice en final game porque eran los mismos que debut) y elimine dichas columnas.\n",
    "\n",
    "Luego revise los tipos de datos de cada columna para ver si eran la mejor opción para esos datos y como las fechas las tenían como strings las cambia a dates.\n",
    "\n",
    "La tabla original no tenia el porcentaje de bateo y como es una estadística importante la saque. \n",
    "Esta se saca dividiendo los hits entre las bases que vas a la caja de bateo. Pero había filas con valores 0 en la columna y esos me darían un problema porque no se puede dividir entre cero y como en ese año no batearon ni una vez saque los indices de esas filas y las elimine.\n",
    "Ahora sí saque el promedio de bateo y lo añadía a allbatting.\n",
    "\n",
    "Al final cambie los nombres de las columnas para que se entendiera mejor de que estadística se hablaba y exporte el archivo como batting-data.\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
