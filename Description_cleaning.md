![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Project: Plane crashes dataset

## Overview

I decided to use this dataset because I consider this dataset contain more problems with the data, since some columns with a lot of missing data until a bad representation of the data like strings with different fields incorporate.

## Steps.
Markup : 1. I started importing the basic library Pandas, and after when I went trought the follow steps also import.
          2. I added some general information about the dataset, just to have available in the notebook.
          3. I read the original csv of the dataset and stored in a variable like dataframe.
          4. I explore in general aspects the dataset.
          5. I check for missing values and I note the next important aspects.
              1. The missing values has a string value '?'.
              2. I had full information just for the 'date' column in the dataset.
          6. I start the data cleaning column by column, with the next general actions.
              1. Date column: I had a string with the structure "Month, day year", so in order to further analysis I split into three columns "month", "day" and "year", I consider that future filters could be easiest with this columns. I use regular expressions and list comprehension
              2. Time column: It has a character that marks the format on 24hrs format, but I let it like char_unknown, and I also split the column into "hour" and minutes. I consider like in the date case that it could facilitate filters and analysis in the future. I use regular expressions, lambda functions and pd.DataFrame.apply method.
              3. Location column: For this column I used an auxiliar file with the states of the United States because in the location column also we have a single String with the information about Region-Country location, but in the case of the crash was in the United States the String contain SubRegion-State location so if I found a Unite States state I had to consider the country like United States but if not I had to consider like a country the last part of the String.
              4. Operator column: for this column I tried to homogenize in categories. So I identify the most comun operators and a category for those. I got a new column with 9 categories.
              5.Route column: for this column I didn't apply any change because it has more complex variations than operators column.
              6.Aircraft column: For this I applied the same strategy than operators.
              7.I drop Flight number, Registration and Construction numbers columns because it doesn't hae to much info.
              


## Suggested Ways to Get Started

* **Examine the data and try to understand what the fields mean** before diving into data cleaning and manipulation methods.
* **Break the project down into different steps** - use the topics covered in the lessons to form a check list, add anything else you can think of that may be wrong with your data set, and then work through the check list.
* **Use the tools in your tool kit** - your knowledge of Python, data structures, Pandas, and data wrangling.
* **Work through the lessons in class** & ask questions when you need to! Think about adding relevant code to your project each night, instead of, you know... _procrastinating_.
* **Commit early, commit often**, don’t be afraid of doing something incorrectly because you can always roll back to a previous version.
* **Consult documentation and resources provided** to better understand the tools you are using and how to accomplish what you want.
