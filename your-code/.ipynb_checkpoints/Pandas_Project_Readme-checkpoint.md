# Project: Data Cleaning and Manipulation with Pandas

## Plane Crashes Dataset 
 
Data format:  

```
Format date:    Date of accident,  in the format - January 01, 2001 
time:    Local time, in 24 hr. format unless otherwise specified
location: location information
Airline/Op:  Airline or operator of the aircraft
flight_no:   Flight number assigned by the aircraft operator
route:   Complete or partial route flown prior to the accident
ac_type:     Aircraft type
registration:    ICAO registration of the aircraft
cn_ln:   Construction or serial number / Line or fuselage number
aboard:  Total aboard (passengers / crew)
fatalities:  Total fatalities aboard (passengers / crew)
ground:  Total killed on the ground
summary:     Brief description of the accident and cause if known
```

The cleaning of this dataset could be resumed in the next steps:

1. Import useful libraries
2. Load the data into a dataframe with pandas and show the first 10 rows to determinate the structure of the data.
3. From the step above it can be inferred:
    - The data in the columns date and time has no correct format for it's respective information (and both can be merged into one).
    - Several columns have '?' in their registries, indicating no data.
    - The columns aboard and fatalities make distinction between crew and passengers, however this distinction is made in every registry, which make the data difficult to access
4. Determine how many null values this dataframe has.
5. From step 4 it can be seen that instead of `null` values, the dataframe has the `?` char where there is no data. In oreder to have a clear vision of the ocurrence of `?` in the data a Heatmap it's created where can be seen the mentioned before.
6. The first change to be made will be on the `date` and `time` columns; due to the nature of the data in this columns, the information can be hold in one column, wich will be the result of the merging of both columns. The column `date_time` is created by formating and merging the columns `date` and `time`, `date_time` has the format `YYYY-bb-dd HH:MM:SS`.
7. Next will be managing the data in the `aboard` and `fatalities` columns, from a simple look, it's clear that each entry has information stored in a messy format. In order to have a better access to data, the column `aboard` will be splitted into three columns, one for each count aboard (total, passengers and crew).
8. Given that `fatalities` has an equal format as `aboard`, the same as above will be applied to `fatalities`, again, it will be splitted into three columns (total, passengers and crew).
9. After all the formating and creation of new columns it's done, the `?` is replaced in the dataframe by the string `NoData` in order to advice the analyst that there is no data available for in given registry.
10. The former columns from which the new columns were calculated are dumped and the dataframe is rearranged for a coherent lecture of the information.
11. Finally, the dataframe is saved into a csv file called `planecrashinfo_clean.csv`

