import pandas
import numpy
from datetime import datetime

plane_crashes = pandas.read_csv('planecrashinfo_20181121001952.csv')

#Se separan las columnas de aboard y fatalities, para tener los datos totales, por pasajeros y por tripulación
aboard = plane_crashes['aboard'].apply(lambda x: pandas.Series(x.split(' ')))
fatalities = plane_crashes['fatalities'].apply(lambda x:pandas.Series(x.split(' ')))
aboard.rename({0:'Total_aboard',1:'Passengers_aboard',2:'Crew_aboard'},axis=1,inplace=True)
fatalities.rename({0:'Total_fatalities',2:'Passengers_fatalities',3:'Crew_fatalities'},axis=1,inplace=True)

#Se limpian los datos separados para obtener solo los valores númericos
aboard['Passengers_aboard'] = aboard['Passengers_aboard'].apply(lambda x: pandas.Series(x.replace("(passengers:","")))
fatalities['Passengers_fatalities'] = fatalities['Passengers_fatalities'] .apply(lambda x: pandas.Series(x.replace("(passengers:","")))

aboard['Crew_aboard'] = aboard['Crew_aboard'].apply(lambda x:pandas.Series((x.replace(' crew:','')).replace(')','')))
fatalities['Crew_fatalities'] = fatalities['Crew_fatalities'].apply(lambda x:pandas.Series((x.replace('crew:','')).replace(')','')))

#Se unen estas columnas al dataframe original
plane_crashes = plane_crashes.merge(aboard,left_index=True, right_index=True)
plane_crashes = plane_crashes.merge(fatalities,left_index=True, right_index= True)

#Se sustituyen los valores default de la base por valores nulos para identificarlos mejor
for col in plane_crashes:
    plane_crashes[col].replace({'?':None,'? ':None,' ?':None,'?\xa0':None,'\xa0':None},inplace = True)

#Se eliminan las columnas con mas de 1000 valores nulos y las columnas aboard y fatalities a las cuales ya se les extrajó la info
null_cols = plane_crashes.isnull().sum()
drop_cols = list(null_cols[null_cols > 1000].index)
drop_cols.append('registration')
drop_cols.append('aboard')
drop_cols.append('fatalities')
plane_crashes = plane_crashes.drop(drop_cols,axis = 1)

#Se llenan todos los valores nulos por 0 de las columnas que serán númericas
plane_crashes[['Total_aboard','Passengers_aboard','Crew_aboard','Total_fatalities','Passengers_fatalities','Crew_fatalities']] = plane_crashes[['Total_aboard','Passengers_aboard','Crew_aboard','Total_fatalities','Passengers_fatalities','Crew_fatalities']].fillna(0)

#Todos los datos son tipo Object, asi que los datos que se necesitan númericos se pasan a enteros y las fechas a un formato fecha
plane_crashes[['Total_aboard','Passengers_aboard','Crew_aboard','Total_fatalities','Passengers_fatalities','Crew_fatalities']] = plane_crashes[['Total_aboard','Passengers_aboard','Crew_aboard','Total_fatalities','Passengers_fatalities','Crew_fatalities']].astype('int')
plane_crashes['date'] = plane_crashes['date'].apply(lambda x: pandas.Series(datetime.strptime(x, "%B %d, %Y")))

#Aqui se corrigen los datos totales, ya que en algunos no cuadra la suma
fixing_row_ab = list(plane_crashes[(plane_crashes['Crew_aboard'] + plane_crashes['Passengers_aboard']) > plane_crashes['Total_aboard']].index)
fixing_row_ft = list(plane_crashes[(plane_crashes['Crew_fatalities'] + plane_crashes['Passengers_fatalities']) > plane_crashes['Total_fatalities']].index)

for ind in fixing_row_ab:
    plane_crashes['Total_aboard'][ind] = plane_crashes['Crew_aboard'][ind] + plane_crashes['Passengers_aboard'][ind]

for ind in fixing_row_ft:
    plane_crashes['Total_fatalities'][ind] = plane_crashes['Crew_fatalities'][ind] + plane_crashes['Passengers_fatalities'][ind]


#Estadisticas generales
stats = plane_crashes.describe().transpose()

low_variance = []

for col in plane_crashes._get_numeric_data():
    minimum = min(plane_crashes[col])
    ninety_perc = numpy.percentile(plane_crashes[col], 90)
    if ninety_perc == minimum:
        low_variance.append(col)

print(low_variance)

stats['IQR'] = stats['75%'] - stats['25%']
print(stats)

outliers = pandas.DataFrame(columns=plane_crashes.columns)

for col in stats.index:
    iqr = stats.at[col,'IQR']
    cutoff = iqr * 1.5
    lower = stats.at[col,'25%'] - cutoff
    upper = stats.at[col,'75%'] + cutoff
    results = plane_crashes[(plane_crashes[col] < lower) |
                   (plane_crashes[col] > upper)].copy()
    results['Outlier'] = col
    outliers = outliers.append(results,sort=False)

column_order = ['date','location','operator','ac_type','Total_aboard','Passengers_aboard','Crew_aboard','Total_fatalities','Passengers_fatalities','Crew_fatalities','ground','summary']
plane_crashes = plane_crashes[column_order]
plane_crashes.to_csv('plane_crash_clean.csv',index=False)




