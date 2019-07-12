# Project: Data Cleaning and Manipulation with Pandas
## (By Daniel Hernández Mota)
---
### Database used:
 * [National Drug Directory](https://www.fda.gov/drugs/drug-approvals-and-databases/national-drug-code-directory)

#### Process:
- First of all, the document was downloaded from the website, and Jupyter Notebook was implemented as an IDE to run python. Pandas was imported and the function pd.read_csv was used in order to obtain the text, separated by the tabulator. Then, the data frame was partially visualized in order to understand the data. 
- General information of the dataframe was also obtained (lenght of dataframe and name of columns), also an analysis of the NaN values was done to drop the columns that didn't had 90% of the dataframe. 
- After this, the name of the columns was actualized and then the rows with any data that was NaN with the unrecoverable information. Then, the fields that were easy to fill were also modified.
- This two steps helped to remove all the data with NaN values, then other information was actualized in order to have more uniformity on the data. Dates were changed into the corresponding format, a boolean flag was changed into 0 or 1, and extra text that was not needed was also modified. 
- This yield a cleaner dataframe. Because of this, the exportation of the csv was done effectively. The separation used to divide the text is '|'.

#### Results:
- The result obtained was a csv file named product.csv with the clean database.

#### Obstacles:
- It was difficult to remember all the methods used in class, therefore a lot of documentation was needed to progress efficiently. Also there were other methods that I needed to check to achieve things such as converting a float number into a date. However, most of the progress was done with the techniques seen in class.

#### Lessons learned: 
- Data cleaning is a necessary tool for obtaining data in a proficient way in order to work with them. There are also many databases that have poor data information stored in, therefore the understanding and knowledge for obtaining these values is imperative when doing data analysis.

