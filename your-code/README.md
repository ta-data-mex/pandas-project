El proyecto utiliza el archivo CSV con los datos de los incidentes de violencia por armas de fuego en los Estados Unidos de 2013 a 2018 recuperados desde https://github.com/jamesqo/gun-violence-data

El mayor problema en contrado durante la limpieza de este dataset fue como se encontraban los datos en columnas como las siguientes:

participant_age_group = 0::Teen 12-17||1::Adult 18+
participant_status = 0::Killed||1::Injured
participant_type = 0::Victim||1::Victim

Los valores en encontrados en columnas de este tipo son strings a manera de una especie de diccionario que elabora el autor del dataset. Dicho string representa un conjunto de valores que pudieran presentarse en columnas independientes, por lo que fue necesario extraer los valores deseados usando regex. Una vez parseados estos strings, se dividieron los datos en diferentes columnas propias para su manejo y analisis.

El segundo problema es en con la subida del dataset original a GitHub ya que este no acepta archivos mayores de 100 MBs. A final de cuentas fue necesario hacer git reset --hard origin/master (pues tras varios intentos de zippearlo y subirlo se acumularon los commits y git seguia subiendo los archivos no zippeados) para volver a cero y subir la version zip.