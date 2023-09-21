# NBA Games and Teams Trends: 1947 to 2015:

## Table of Contents
- [Project Overview](#projectoverview)
- [Data Source](#datasource)
- [Key Insights](#keyinsights)

## Project Overview
In this project, I conducted a detailed analysis on 63,157 NBA game records from years 1947 to 2015, to showcase key insights through the aid of effective visualizations aimed at evaluating  what factors are correlated with points scored for 53 teams.

## Data Source
The [data](https://data.fivethirtyeight.com) is sourced from 538: Complete History of the NBA as a csv. Original data is sourced from Basketball Reference, an online database for NBA history. The data represents every NBA game statistic (e.g. location, win or loss, points scored, opposing team played) from 1947 to 2015.

| Variables | Details  | 
| :-----: | :---: |
| game_id | unique identifier for game |
| year_id | year game was played |
| seasongame | season game was played |
| is_playoffs | if the game was a playoff |
| fran_id | playing team |
| pts | points scored by the playing team | 
| opp_fran | opposing team |
| opp_pts | points scored by the opposing team |
| game_location | home or away game|
| game result | win or loss|
| forecast | prediction if the playing team will win |

### Questions:
Is forecast of winning linearly associated to points scored? (for all 53 teams) <br>
Does game location affect points scored for a team?<br>
Is playing team and game result associated for the top 5 and bottom 5 teams?<br>
Is there a linear association between points won and opposing points won for the top 5 teams and bottom 5 teams?<br>
Is there an association between top 5 teams and points won?<br>

## Key Insights:
***There is no linear association between forecast and points won.*** <br>
***Game location affects points scored for two teams (Clippers and Nets)*** <br>
***Playing team and game result are not associated for the top 5 and bottom 5 teams.***<br>
***Points scored and opposing team points scored are linearly associated, with Squires having a strong linear association.***<br>
***Condors, stands out from the top 5 teams, scoring between 100-125 points, 40% of the time.***



