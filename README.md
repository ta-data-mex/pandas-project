![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Project: Data Cleaning and Manipulation with Pandas

## Overview
I chose the [London air quality](https://www.londonair.org.uk/london/asp/datadownload.asp).
The data is from Lewisham, particurarly from two sites abbreviated as PH1 and LW2. The data is from 1-nov-2018 to 1-jul-2019, including hourly mean values from pollutants such as Nitric Oxide (ug m-3), Nitrogen Dioxide (ug m-3), Ozone (ug m-3), PM10 Particulates, PM2.5 Particulates and Total Suspended Particles (TSP). The graph plot from the two different sites of Lewisham are shown below:

* [Lewisham Honor Oak Park - abbreviated as HP1](https://www.londonair.org.uk/london/asp/datasite.asp?CBXSpecies1=NOm&CBXSpecies2=NO2m&CBXSpecies3=O3m&CBXSpecies5=PM10m&CBXSpecies7=PM25m&CBXSpecies8=TSPm&day1=1&month1=nov&year1=2018&day2=1&month2=jul&year2=2019&period=hourly&ratidate=&site=HP1&res=6&Submit=Replot+graph)
![sketch1](https://dl.dropboxusercontent.com/s/z4sq6rabutl3qyj/Sketch_HP1.png?dl=0)

* [Lewisham Catfor - abbreviated as LW2](https://www.londonair.org.uk/london/asp/datasite.asp?CBXSpecies1=NOm&CBXSpecies2=NO2m&CBXSpecies3=NOXm&CBXSpecies4=O3m&CBXSpecies5=SO2m&day1=1&month1=nov&year1=2018&day2=1&month2=jul&year2=2019&period=hourly&ratidate=&site=LW1&res=6&Submit=Plot+graph)
![sketch2](https://dl.dropboxusercontent.com/s/4xmor50xgag98it/Sketch_LW2.png?dl=0)


To use:
https://www.londonair.org.uk/london/asp/datasite.asp?CBXSpecies1=NOm&CBXSpecies2=NO2m&CBXSpecies3=O3m&CBXSpecies5=PM10m&CBXSpecies7=PM25m&CBXSpecies8=TSPm&day1=1&month1=nov&year1=2018&day2=1&month2=jul&year2=2019&period=hourly&ratidate=&site=HP1&res=6&Submit=Replot+graph

https://www.researchgate.net/post/How_can_I_deal_with_negative_and_zero_concentrations_of_PM25_PM10_and_gas_data


You will need to import a data set, use your data wrangling skills to clean it up, prepare it to be analyzed, and then export it as a clean CSV data file.

**You will be working individually for this project**, but we'll be guiding you along the process and helping you as you go. Show us what you've got!

---

## Technical Requirements

The technical requirements for this project are as follows:

* The dataset that we provide you is a significantly messy data set. Apply the different cleaning and manipulation techniques you have learned.
* Import the data using Pandas.
* Examine the data for potential issues.
* Use at least 8 of the cleaning and manipulation methods you have learned on the data.
* Produce a Jupyter Notebook that shows the steps you took and the code you used to clean and transform your data set.
* Export a clean CSV version of your data using Pandas.

## Necessary Deliverables

The following deliverables should be pushed to your Github repo for this chapter.

* **Examine data

* **A Jupyter Notebook (data-wrangling.ipynb)** containing all Python code and commands used in the importing, cleaning, manipulation, and exporting of your data set.
* **A ``README.md`` file** containing a detailed explanation of the process followed in the importing, cleaning, manipulation, and exporting of your data as well as your results, obstacles encountered, and lessons learned.

## Suggested Ways to Get Started

* **Examine the data and try to understand what the fields mean** before diving into data cleaning and manipulation methods.
* **Break the project down into different steps** - use the topics covered in the lessons to form a check list, add anything else you can think of that may be wrong with your data set, and then work through the check list.
* **Use the tools in your tool kit** - your knowledge of Python, data structures, Pandas, and data wrangling.
* **Work through the lessons in class** & ask questions when you need to! Think about adding relevant code to your project each night, instead of, you know... _procrastinating_.
* **Commit early, commit often**, don’t be afraid of doing something incorrectly because you can always roll back to a previous version.
* **Consult documentation and resources provided** to better understand the tools you are using and how to accomplish what you want.

## Useful Resources

* [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
* [Pandas Tutorials](https://pandas.pydata.org/pandas-docs/stable/tutorials.html)
* [StackOverflow Pandas Questions](https://stackoverflow.com/questions/tagged/pandas)
* [Awesome Public Data Sets](https://github.com/awesomedata/awesome-public-datasets)
* [Kaggle Data Sets](https://www.kaggle.com/datasets)
