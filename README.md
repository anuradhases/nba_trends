# NBA Games and Teams Trends: 1947 to 2015:
## 53 teams, 68 years

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
- Is forecast of winning correlated to points scored? (for all 53 teams) <br>
- Does game location affect points scored for a team?<br>
- Is playing team and game result correlated for the top 5 and bottom 5 teams?<br>
- How does points won change with opposing points won for the top 5 teams and bottom 5 teams?<br>
- Do all top 5 teams score the same?<br>
Note: Top 5 and Botom 5 teams based on points scored.

## Key Insights:
- ***There is no significant correlation between forecast of winning and points won. (R<sup>2</sup> = 0.2).***<br>
- ***Top 5 Teams: Condors, Stars, Floridians, Squires, Colonels.***<br>
- ***Bottom 5 Teams: Huskies, Rebels, Bombers, Falcons, Ironmen.*** <br>
- ***Clippers and Nets performance changes with game location.*** <br>
- ***Among the top 5 and bottom 5 teams, points scored and opposing team points scored are moderately correlated (R<sup>2</sup>~0.5). Squires stands out, having a strong correlation (R<sup>2</sup> = 0.6).***<br>
- ***Among the top 5 teams, Condors stands out, scoring between 100-125 points, 40% of the time.***



