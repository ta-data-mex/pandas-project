![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Project: Data Cleaning and Manipulation with Pandas

## Overview
I chose the [London air quality](https://www.londonair.org.uk/london/asp/datadownload.asp).
The data is from Lewisham, particurarly from two sites abbreviated as PH1 and LW2. The data is from 1-nov-2018 to 1-jul-2019, including hourly mean values from pollutants such as Nitric Oxide (ug m-3), Nitrogen Dioxide (ug m-3), Ozone (ug m-3), PM10 Particulates, PM2.5 Particulates and Total Suspended Particles (TSP). The graph plot from the two different sites of Lewisham are shown below:

* [Lewisham Honor Oak Park - abbreviated as HP1](https://www.londonair.org.uk/london/asp/datasite.asp?CBXSpecies1=NOm&CBXSpecies2=NO2m&CBXSpecies3=O3m&CBXSpecies5=PM10m&CBXSpecies7=PM25m&CBXSpecies8=TSPm&day1=1&month1=nov&year1=2018&day2=1&month2=jul&year2=2019&period=hourly&ratidate=&site=HP1&res=6&Submit=Replot+graph)
![sketch1](https://dl.dropboxusercontent.com/s/z4sq6rabutl3qyj/Sketch_HP1.png?dl=0)

* [Lewisham Catfor - abbreviated as LW2](https://www.londonair.org.uk/london/asp/datasite.asp?CBXSpecies1=NOm&CBXSpecies2=NO2m&CBXSpecies3=NOXm&CBXSpecies4=O3m&CBXSpecies5=SO2m&day1=1&month1=nov&year1=2018&day2=1&month2=jul&year2=2019&period=hourly&ratidate=&site=LW1&res=6&Submit=Plot+graph)
![sketch2](https://dl.dropboxusercontent.com/s/lozwje2sls3i7kr/Sketch_LW2.png?dl=0)


## Steps of the data wrangling

* **0 - How the data is coming?** before diving into data cleaning, I did make sense of the given data. So, I sketched if I keep or drop the columns, as its follows:

* * **Site** - Site code: It is necessary since I want to merge two areas from Lewisham. *Keep it.* 
* * **Species** - pollutants names with standard chemical notation (e.g., CO = carbon monoxide), meteorological parameters are as follows: WSPD = wind speed, WDIR = wind direction, BP = barometric pressure, TMP = ambient temperature, RAIN = rainfall, SOLR = incoming solar radiation. *Keep it.*
* * **DateTime** - Date and time of the measurement. This data is hourly mean value, i.e. for 01-jan-2018 12:00 encompasses measurements taken between 12:00 and 12:59 on 01 January 2018. *Keep it.*
* * **Value** - Measurement concentration. *Keep it.*
* * **Units** - Shows the units the values are quoted in. *Keep it.*
* * **Provisional or Ratified** - P for provisional and R for Ratified. Provisional measurements are subjected to change. Ratified measurements have been through the full QAQC procedure and will not change in the future. *Keep it.*

* **1- Changing title names** - I changed names in the most intuitive fashionable way.
* **2- Rearranging columns order** - I reorder the columns, keeping in mind possible visualizations.
* **3- Changing names** On this part I found a challenge: unexpected changes of the names. Unexpected variances of the names. I was thinking to replace the 'NO', but it changed me the 'NO2' as well. And will change the 'NOX' from the second source. So I preferred to keep pragmatic (and recognized) names from the pollutants. This is a sample of the precautions to take into consideration when we decide to change values or names.
* **4- Skiping NaN values**, I decided to dropping the rows that had NaN values on its 'Value' column.
* **5- Combining Data Frames** I used 'concat' method to attach rows with the same number of columns.
* **6- Checking extreme values or outliers** Firstly, I focused on negative numbers, as they may be not reliable because of possible uncalibrated instruments [(as here is noted)](https://www.researchgate.net/post/How_can_I_deal_with_negative_and_zero_concentrations_of_PM25_PM10_and_gas_data). So I just indicated on the column 'Provisional or Ratified column that these values were not reliable.

* **7- Creating an empty df called 'outliers'** This part could be further explored to find out if they should be kept in the data or dropped. Additionally,  it could be used for the creation of additional categorical fields. For example, how high or low are pollutants concentrations in the air. This could give us a flag if the air is dangerous for sensitive population. 
* **8- Exporting clean data** :)
