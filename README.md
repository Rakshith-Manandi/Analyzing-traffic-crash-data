# Analyzing-traffic-crash-data
This repository contains code that analyses FARS dataset and visualizes interesting correlations between the data using Python
The Fatality Analysis Reporting System (FARS) Dataset is provided by the National Highway Traffic Safety Administration.
The requirement for a traffic accident to be logged into the FARS is that it must result in a fatality within 30 days of the accident.

Throughout our project, our process is to start most of our analysis by visualizing some broad aspects of data and narrowing in on interesting features of the visualizations produced.


We started our analysis by analyzing traffic fatalities per state. 
![Alt text](Readme_Figures/Figure_1.png?raw=true "Figure 1. Total Accidents By State in 2017. Darker states like CA, TX, FL have a higher count
")

We see a general trend that the most populated states have the highest number of fatalities. This lead us to plot per capita to make less populated states comparable.
![Alt text](Readme_Figures/Figure_2.png?raw=true)

Next we see that the states that lead in fatalities per capita have changed from the previous figure dramatically. We note that Mississippi and other rural states are now the leaders (per capita) compared to urban states which lead in total.

We now visualize fatalities by the road's speed limit of the fatality, and road type (rural or urban).
![Alt text](Readme_Figures/Figure_3.png?raw=true)

We see a large spike for rural roads at higher speed limits.
This indicates that rural roads tend to be much more dangerous at higher speeds compared to urban roads and that urbanness or ruralness of the area could be a contributing factor to traffic safety.

Next we visualized the total number of fatalities per year over the time range 1994-2016.
![Alt text](Readme_Figures/Figure_4.png?raw=true)
We see that there is a significant decrease in the 2005-2010 interval.

We also visualize fatalities in this time range by vehicle type.
![Alt text](Readme_Figures/Figure_5.png?raw=true)
Again we see a significant decrease in the same 2005-2010 inteval for trucks and cars.

We also visualized fatalities in this time range by age group.
![Alt text](Readme_Figures/FIgure_6.png?raw=true)
We see the decerase in the same interval for the major age group 21-44 years old.

We found in other research that the factors that attribute to this trend is that advancements in vehicle safety technology continues to improve. Also this decline is historically common in times of recession (2008 was the year of recession).

Next we start our analysis differently: We hypothesize that date and time is related to crash frequency.
This led us to visualize daily fatalities every day in 2017 using an interactive plotly graph.
![Alt text](Readme_Figures/Figure_7.png?raw=true)

We noticed that the plot seems to be periodic with many peaks.
After zooming in on the peaks and cross-referencing the dates, we found that there is a particular relationship to the weekend as a "fatality hotspot".
![Alt text](Readme_Figures/Figure_8.png?raw=true)

After plotting time of day versus day of week in a heatmap using seaborn, we see exactly when the hotspots are to happen.
![Alt text](Readme_Figures/Figure_9.png?raw=true)
We see that these times are near the last call times for bars, which is when they close for the night.

This led us to investigate alcohol related crashes.
![Alt text](Readme_Figures/Figure_10.png?raw=true)
We see that there is a high ratio of alcohol-related crashes during these hotspot time intervals compared to other time intervals.
This indicated that drinking and driving is a big factor in fatality count.

The insights that we presented here can be used in drinking and driving solutions, emerging laws and regulations, etc.

Note:
Due to dependency issues the plots are not displayed in the jupyter notebook

