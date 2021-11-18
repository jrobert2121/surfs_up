# Surfs Up Analysis

## Project Overview
This project entails conducting a weather analysis for the island of Oahu for an entreprenuer.  In order to obtain backing for a Surf and Shake shop on the island, an investor requests a weather analysis from the entreprenuer to aid in determining the viability of the investment.

## Purpose
The purpose of the project is to provide information on temperature trends for the months of June and December for the island of Oahu.  This will help potential investors determine if the surf and ice cream shop business would be sustainable year round.

## Resources
Software: Python version 3.7.10, SQLAlchemy,

Data Sources: hawaii.sqlite database, 

## Results - bulleted list addressing 3 key differences in weather between June and Dec
Utilizing SQLAlchemy, we are able to extract temperature data for June and December from the Measurements table.  Then after converting the extracted data to a list, we can easily create dataframes for each of the months' data and take a look at the statistics.

***June Temperatures***                                         ***December Temperatures***

![June_temp_stats](Resources/June_temp_stats.png)               ![Dec_temp_stats](Resources/Dec_temp_stats.png)

Some key differences between the two months include:
 - Average Temperature:  The average temperature for June is 75 degrees but December is slightly cooler with an average temperature of 71 degrees.
 - Maximum Temperature:  The maximum temperatures for both months are very similiar.  June's max temperature is 85 degrees and December is 83 degrees.
 - Minimum Temperature:  The greatest difference between the two months is in this category.  June's minimum temperature is 64 degrees but December's is down to 56 degrees, which may not be the most conducive for ice cream or surfing.  December's standard deviation of 3.75 would lead us to anticipate a greater spread in temperatures over June, which had a standard deviation of 3.26.

## Summary - high level summary of the results and provide 2 more additional queries to perform to gather more weather data for June and Dec
Overall, the temperatures are not dramatically different between June and December.  While December is a bit a cooler and may have a few days not conducive to surfing or ice cream sales, the average and maximum temperatures for both months indicates a fairly stable climate for the proposed venture.

However, a more in depth analysis of the Oahu climate can be performed.  In addition to analyzing temperature, it would also be advisable to conduct an analysis on precipitation levels for those two months.  See below for the example code for the month of June.
```
# Write a query that filters the Measurement table to retrieve the precipitation for the month of June. 
session.query(Measurement.date, Measurement.prcp).\
filter(func.strftime("%m", Measurement.date) == "06").\
group_by(Measurement.date).\
order_by(Measurement.date).all()

# Convert the June precipitation to a list.
june_temps = session.query(Measurement.date, Measurement.prcp).\
filter(func.strftime("%m", Measurement.date) == "06").all()

# Create a DataFrame from the list of precipitation for the month of June. 
june_df = pd.DataFrame(june_temps, columns=['date','precipitation'])

# Calculate and print out the summary statistics for the June precipitation DataFrame.
june_df.describe()
```
We would discover that Oahu experiences more precipitation in the month of December than the month of June but amounts are still within reason.

Another query to consider would be narrowing down the precipitation analysis by weather station on the island.  That may help determine where the best potential location may be. If we know the closest weather station to the proposed location of the Surf n' Shake shop, then an example query to determine precipitation measured by that weather station would look something like:
```
# Using the desired station id, calculate the lowest precipitation recorded, 
# highest precipitation recorded, and average precipitation for desired station id
session.query(func.min(Measurement.prcp), func.max(Measurement.prcp), func.avg(Measurement.prcp)).\
filter(Measurement.station == 'insert desired station id').\
filter(func.strftime("%m%", Measurement.date) == "12").all()
```
The above example would yield the min, max and average precipitation for the month of December of a specific station id.

Overall, while December is cooler and experiences more precipitation on the island of Oahu than in the month of June, the weather analysis seems to support an investment in the Surf n' Shake shop.
