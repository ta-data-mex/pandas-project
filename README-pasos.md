## Pasos a seguir:
1. Importé las librerías necesarias: Pandas, Numpy, PyMySQl, SQLalchemy
2.Importo la base de datos de formato .xls
3. Observo cuántos valores nulos tiene la base de datos.
4. A los valores nulos les agrego n/a en vez de 0, pues representan datos no existentes y el número cero confundiría el verdadero significado de la falta de datos
5. Reviso si aún hay valores nulos. Debido a que la cantidad era poca, no borro ninguna columna
6. Imprimo la base de datos para revisar errores en las columnas
7. Cambió los nombres de tres columnas para que sea más claro el significado de dos de ellos y para empatar el estilo de una con las demás.
8. En la columna Subject hay algunos errores de sintaxis que debo editar para que no se malentienda su significado
9. Reviso que todos los temas en Subject estén correctamente editados. Debido a que son demasiados, resulta mejor categorizarlos según su tipo de información, para así su lectura sea más sencilla
10. Decido categorizar por: datos de emisiones, trabajo por el cuidado del medio ambiente, servicios, salubridad, población, condiciones geoclimáticas, economía y proyectos por el ciudado del medio ambiente
11. La última categoría sólo muestra si los países tienen planes a futuro por el cuidado del medio ambiente. La última columna es la que sirve, así que eliminó las demás que contienen valores nulos.
12. Después de que están categorizadas, las vuelvo a unir en una sola base de datos. Utilizo el outer para que los valores se acomoden en las mismas columnas, sin sobreescribir unas nuevas
13. Exporto la base de datos a un archivo .csv, separado por |, para una lectura más sencilla

