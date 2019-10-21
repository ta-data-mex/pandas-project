import pandas as pd
import numpy as np
import re

def getPassengerData(columnData):
    result = re.sub('[^0-9 ]','', columnData)
    
    return pd.Series(result.split(' '))

#get file
planecrash_data = pd.read_csv("C:\\Users\\david\Documents\\pandas-project\\your-code\\plane-crash.csv")





#Cleaning aboard and fatalities columns

aboard = planecrash_data['aboard'].apply(getPassengerData)
aboard=aboard.drop(1,axis=1)
fatalities = planecrash_data['fatalities'].apply(getPassengerData)
fatalities=fatalities.drop(1,axis=1)
aboard.rename({0:'Total_aboard',2:'Passengers_aboard',3:'Crew_aboard'},axis=1,inplace=True)
fatalities.rename({0:'Total_fatalities',2:'Passengers_fatalities',3:'Crew_fatalities'},axis=1,inplace=True)

#Getting rid of null columns that have over 1000
null_cols = planecrash_data.isnull().sum()
removed_cols = list(null_cols[null_cols > 1000].index)


planecrash_data = planecrash_data.merge(aboard,left_index=True, right_index=True)
planecrash_data = planecrash_data.merge(fatalities,left_index=True, right_index= True)



#Appending new columns
removed_cols.append('aboard')
removed_cols.append('fatalities')
planecrash_data = planecrash_data.drop(removed_cols,axis = 1)




planecrash_data.to_csv('plane_crash_clean.csv',index=False)