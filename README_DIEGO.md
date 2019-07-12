 ![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Diego's Project: Data Cleaning and Manipulation with Pandas


## Para este proyecto decidí hacer la limpieza de la base de datos National Drugs Code.

### Al descargar el archivo, me encontré con dos bases, ambas con datos faltantes y algunos detalles, por lo que decidí realizar la limpieza de ambas bases y al final hacer un merge.

1. Importar pandas.
2. Importar ambas bases de datos.

#### PARA PACKAGE.

3. Seleccionar una para empezar a limpiar, en este caso la data de package.
4. Revisar los tipos de datos que contiene.
5. Realizar el cambio de nombre a las columnas, según la conveniencia.
6. Revisar las columnas con datos faltantes.
7. Eliminar columnas con muchos datos faltantes, ya que no aportan nada.
8. Cambiar los tipos de datos de las columnas según se crea conveniente.
9. Reemplazar los datos faltantes por 0's.

#### PARA PRODUCT.

10. Seleccionar una para empezar a limpiar, en este caso la data de package.
11. Revisar los tipos de datos que contiene.
12. Realizar el cambio de nombre a las columnas, según la conveniencia.
13. Revisar las columnas con datos faltantes.
14. Reemplazar los datos que estuvieran incorrectos por NaN.
15. Cambiar los tipos de datos de las columnas según se crea conveniente.
16. Reemplazar los datos faltantes por 0's.

#### THE MERGE.

17. Realizar un merge con las dos bases anteriores, eligiendo solo las columnas importantes.

#### EXPORTAR LAS BASES A CSV.

#### RESULTADO.

Al realizar todos los pasos anteriores, mi resultado fueron tres archivos .csv, sin datos faltantes, nombres de columnas más ad hoc según mi criterio, así como formatos correctos de datos.

#### OBSTACULOS.

Uno de los retos que tuve al realizar esté proyecto, fue el de cambiar las columnas a datatime, debido a que a pesar de intentarlo de distintas formas seguía mostrando error, al final me di cuenta que el error venía debido a que un dato tenía fecha del año 3032, algo tonto, pero al final logré solucionarlo.

#### APRENDIZAJE.

Use varias formulas vistas durante las clases, pero la ayuda que obtuve de stackoverflow fue bastante útil al realizar algunos pasos.


