# EV-ETL-Project-2
Our intention with this project is to help future car buyers in making a determination about which currently-available electric vehicles an individual should buy. The two datasets show the relevant information on electric vehicle models for shoppers in Europe.

## Extract
The two datasets were both from Kaggle and were CSV files, because we determined having data sources of the same file type would join easier. We then read both csv files into a Jupyter notebook for both cleaning and merging. 

## Transform
Once we merged the data as an outer join on the model of the vehicle as that was a common value within the two files. From there, we cleaned the data as we did have some duplicated columns. Once the data was cleaned, we exported to a new CSV file to read into a PostgreSQL database.


## Load
The database then was created and the file was imported, bringing our database online. From there we are able to query the database without having to worry about joining two and then executing queries.