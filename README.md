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
