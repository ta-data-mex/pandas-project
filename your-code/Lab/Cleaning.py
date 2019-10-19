import pandas
import numpy

plane_crashes = pandas.read_csv('planecrashinfo_20181121001952.csv')

plane_crashes['aboard'] = plane_crashes['aboard'].apply(lambda x: pandas.Series(x.split(' ')))
plane_crashes['fatalities'] = plane_crashes['fatalities'].apply(lambda x:pandas.Series(x.split(' ')))

for col in plane_crashes:
    plane_crashes[col].replace({'?':None},inplace = True)

plane_crashes['aboard'].replace({'? ':None},inplace=True)

null_cols = plane_crashes.isnull().sum()
drop_cols = list(null_cols[null_cols > 1000].index)
plane_crashes = plane_crashes.drop(drop_cols,axis = 1)

plane_crashes[['aboard','fatalities','ground']] = plane_crashes[['aboard','fatalities','ground']].fillna(0)

plane_crashes['aboard'] = plane_crashes['aboard'].astype('int')
plane_crashes['fatalities'] = plane_crashes['fatalities'].astype('int')
plane_crashes['ground'] = plane_crashes['ground'].astype('int')

test = plane_crashes[(plane_crashes['aboard']==0) & (plane_crashes['fatalities']==0) & (plane_crashes['ground'] == 0)].index
plane_crashes=plane_crashes.drop(test,axis=0)

stats = plane_crashes.describe().transpose()
print(stats)


plane_crashes.to_csv('plane_crash_clean.csv')


