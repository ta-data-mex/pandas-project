![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)


# Project: Data Cleaning and Manipulation with Pandas 

## Objective 

The general goal with this project was to use the necessary instruments to clean and manipulate a data base so it could be use with no problemas. 

## Steps 

1. First I download the data base from: https://data.world/worldbank/climate-change-data
2. The data was saved in an excel type format so I use the pandas method for opening a excel type document.
3. The data base was about an indicator of climate change. The data base contain 13512 rows and 28 columns: the rows we're the countries names and the columns from the sixth to the last one we're the years the indicator was calculated. This information was access by calling the data frame. 
4. I wanted to see what kind of information was in the data set so after looking at the rows and columns it looked like the indicator was written in scientific notation. I didn't know if this was part of the way Pandas showed the Data Frame or the data base was constructed like that. So I tried to  do some basic arithmetic with this numbers in scientific notation, but to call a specific index result troublesome. 
5. I notice that the columns names, that refer to the years where the indicator was calculated, were of integer type so I couldn't called them if I wanted a specific element of the column. I transformed this column names that were integers into strings so they will be callable. 
6. After this I could call any element of any column. I tried to make basic arithmetic with these elements that were written in scientific notation successfully. 
7. However a lot of information was missing. In every cell that was no information it had two points written (..). At this point I wanted to know al the cells where there were empty values but these two points prevent me from doing so as also the type of the columns. I replace these two points with zeros so I could transform the type of the columns. This was tricky because the last column proved to contain a los of strange values. 
8. Because the column of the year 2011 was becoming a headache I try visualizing the elements of the set. This set contained a los of miswrote information and had information that was in no way similar to the other columns. After exploring the number of miswrote information I decided to drop this columns in order to have a data base where I could have complete information. 
9. To do this I created a subset of the data base where I only have the countries that had a value different from zero in each column (from 1990 to 2010). 
10. With this new subset I calculated some descriptive statistics and the corresponding outliers from each year. 
11. Finally I've saved these new subset and the outliers in a csv document. 