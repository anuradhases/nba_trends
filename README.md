# NBA Games and Teams Trends: 1947 to 2015:

I explored the associations for game statistics from the NBA dataset from years 1947 to 2015. 

# Part 1: Understanding the Data: 

### Where did the data come from? How was the data collected?
The data is sourced from 538: Complete History of the NBA as a csv. Original data is sourced from Basketball Reference, an online database for NBA history.

### How was the data accessed?
The data was downloaded, and is publicly available at https://data.fivethirtyeight.com
I explored the nba-elo dataset.

### What does the data represent?
The data represents every NBA team game statistic (e.g. location, win or loss, points scored, opposing team played) from 1947 to 2015.

23 Variables are included in this dataset. I chose to use game data, and removed columns that included the statistic measures from 538. (e.g. Elo- a statistic that measures strength based on game-by-game results), ending with 12 variables for analysis.

# Part 2: Inspecting Data:

### Population or Sample Data?
In order to determine what statistic formulas to use, it is important to determine whether we are dealing with population or sample data. Since we do not have data for all years, we are dealing with sample data.

### Data Cleaning:
All duplicates were removed. Irrelevant columns to analysis for this project were removed. 
There was no missing or incomplete data.

### Outliers?
Boxplots for relevant numerical variables (Points scored, Opposing points scored, and Forecast) are below: 

![Figure 1. Points Scored Distribution](/Users/anuroxstar/pts_boxplot.jpg)
 
![Figure 2. Opposing Points Distribution](/Users/anuroxstar/opp_pts_boxplot.jpg)
 
![Figure 3. Forecast Distribution](/Users/anuroxstar/forecast_boxplot.jpg)

Outliers are present for all three variables, indicated by points beyond the whiskers. Since knowledge is not known about the specifics of the data collection process, and the sample size is large (63,157 observations), outliers are kept and noted.

# Part 3: Exploratory Data Analysis & Data Visualizations
To determine which associations I wanted to explore, I determined whether each variable was quantitative or categorical from the 12 variables, leading to 5 categorical variables and 7 quantitative variables. In addition, I determined there are 53 teams in the dataset.

## Question 1: Is forecast of winning linearly associated to points scored? (for all 53 teams)
This question involves two quantitative variables. Figure 4 shows a scatterplot between points scored and forecast. The linear correlation coefficient is in the upper left corner of the graph, at 0.2.

### Conclusion:
There is no linear association between forecast and points won, since it is lower than 0.3. 

![Figure 4. Points Scored vs Forecast](/Users/anuroxstar/)

## Question 2: Does game location affect points scored for a team?
This question involves one categorical variable, and one quantitative variable.
Further exploration indicated only two NBA Teams had data available for the two game locations (Home, Not Home). Figure 5 shows boxplots for the points scored versus game location for the teams: Clippers and Nets. There is a difference in median for points scored for each game location for each team, indicating that there is game location affects points scored. 

### Conclusion:
Game location affects points scored for each team.
 
![Figure 5: Points Scored vs Game Location](/Users/anuroxstar/)

## Question 3: Is playing team and game result associated for the top 5 and bottom 5 teams?
This question involves two categorical variables. A chi square contingency test was used to determine if there was an association. The pvalue was 0.99, which is higher than the significance level of 0.05. This indicates to fail to reject the null, meaning playing team and game result are not associated for the top 5 and bottom 5 teams.

### Conclusion:
Playing team and game result are not associated for the top 5 and bottom 5 teams.

## Question 4: Is there a linear association between points won and opposing points won for the top 5 teams and bottom 5 teams?

This question involves two quantitative variables. Figure 6 illustrates the relationship between the points scored and the opposing team points scored for each game, for the highest 5 scoring teams. The linear correlation coefficient is located in the upper left corner of the graph. All linear correlation coefficients for the highest 5 scoring teams are above 0.3, indicating a linear correlation, but below 0.6, except for Squires, indicating it is not a strong linear association. Squires has a strong linear association between points scored and opposing team points scored.
Figure 7 illustrates the relationship between the points scored and the opposing team points scored for each game, for the lowest 5 scoring teams. The linear correlation coefficient is located in the upper left corner of the graph. All linear correlation coefficients for the highest 5 scoring teams are above 0.3, indicating a linear correlation, but below 0.6, indicating it is not a strong linear association. 

### Conclusion:
There is a linear association for points scored and opposing team points scored for the top 5 teams and bottom 5 teams. Squires has a strong linear association for points scored and opposing team points scored.

![Figure 6. Top 5 Teams: Opposing Team Points Scored vs Points Scored](/Users/anuroxstar/)
 
![Figure 7. Bottom 5 Teams: Opposing Team Points Scored vs Points Scored](/Users/anuroxstar/)

## Question 5: Is there an association between top 5 teams and points won?
This question involves one categorical variable and one quantitative variable.
Figure 8 illustrates the distribution for points scored for the top 5 teams, with overlapping histograms. Condors has a higher frequency, ~0.039, for points scored between 100 and 125, indicating Condors is different from all other top 4 teams. 

### Conclusion:
Condors is different from all other top 4 teams, with a higher frequency for points scored between 100 and 125 at ~0.039. 

![Figure 8. Points Scored vs Top 5 Teams](/Users/anuroxstar/)


