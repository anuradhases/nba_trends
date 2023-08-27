
#Project: NBA Trends

#Questions tasked with: 
#Explore associations between variables

#Understand Data prior to investigating
#-included in ReadME.md

#Determine structure of data investigating:
#structure is csv

#Part 1: Data Acquisition
#Step 1: Import relevant Modules
#to read data frame and manipulate
import pandas as pd
#to plot visualizations
import matplotlib.pyplot as plt
#for colors
from matplotlib.pyplot import cm
#to manipulate data
import numpy as np
#to plot visualizations
import seaborn as sns
#to perform statistics
from scipy.stats import pearsonr
from scipy.stats import chi2_contingency
import scipy.stats as stats

#Step 2: Read data into script
nba = pd.read_csv('enter source here')


#Step 3:Inspect data
#Population or sample data?
#Sample data (does not include all data points)
#Print first 5 rows of data
print(nba.head())
#Print stats on dataset - # of entries, name of columns, non-null count and data types
print(nba.info())
#Print # of rows and # of columns
print(nba.shape)




#Part 2: Data Cleaning:

#Step 1: Reshape Data?
#data is tidy (tabular format)

#Step 2: Remove duplicates
nba.drop_duplicates()
nba = nba[nba._iscopy == 0]
#Check duplicate data is removed
print(nba._iscopy.value_counts)

#Step 3: Explore the following columns after taking a look at .info()
print(nba.lg_id.value_counts)
#all values are NBA, column can be removed
print(nba.team_id.value_counts)
#hard to understand meaning of team_id, and fran_id included already
#remove team_id
print(nba.win_equiv.value_counts)
#not sure what this variable means, remove
print(nba.opp_id.value_counts)
#similar concept as team_id, hard to undersand meaning of opp_id, and opp_fran included already
print(nba.notes.value_counts)
#majority null, can remove column, not relevant to data analysis
#all elo columns removed since this is a statistic made by 538 not from the original basketball data

#Step 4: Remove columns
nba.drop(['lg_id','date_game','team_id','elo_i', 'elo_n', '_iscopy'], axis =1, inplace = True)
nba.drop(['win_equiv','opp_id','opp_elo_i','opp_elo_n','notes'], axis =1, inplace = True)
#check columns are removed
print(nba.head())

#Step 5: Missing/ Incomplete Data? 
print(nba.info())
#Does non-null count of column match total # of rows?
#Yes, meaning no missing values

#Step 6: Change Data Types of Columns?
#is_playoffs is categorized as numerical when it is a categorical variable, determined by percentile values
#confirm with histogram
# plt.hist(nba.is_playoffs)
# plt.show()
# plt.close()
#change datatype from numerical to categorical for is_playoffs
nba['is_playoffs'] = nba['is_playoffs'].astype('string')
#year_id is stored as integer, when it is an ordinal categorical variable
#since ordinal, kept as integer type for data visualization purposes
#Confirm change in data types
print(nba.info())

#Step 7: Numerical Variables ONLY: Skewed Data? - through comparing mean and median
print(nba.describe())
#comparing 50%(median) and mean for all numerical variables
#no majorly skewed columns

#Step 8: Numerical Variables ONLY: Outlier/Anomalous Data?
#Confirm with BoxPlots
def boxplot(column, name):
    sns.boxplot(data = nba, x = nba[f'{column}'])
    plt.xlabel(str.upper(column))
    plt.title(str.upper(column)+": Distribution")
    plt.savefig(name)
    plt.show()
boxplot('pts', 'pts_boxplot.jpg')
# #Significant amount of outliers
boxplot('opp_pts', 'opp_pts_boxplot.jpg')
# #Significant amount of outliers
boxplot('forecast','forecast_boxplot.jpg')
#outliers towards left

#Since knowledge is not known about specifics of data collection process, and sample size is large,
# outliers are kept but noted



#Part3: Data Visualization/ Exploratory Data Analysis:
#12 variables
#5 categorical variables (game_id,fran_id, opp_fran, game_location, game_result)
#7 numerical variables (game_id, gameorder, year_id, seasongame, pts, opp_pts, forecast)
#irrelevant: game_id (unique identifier for data but not worth analyzing)
#left with 11 variables to analyze

#Step 1: Investigate Variables: not sure what they represent
#find out more about fran_id
#print(nba.fran_id.value_counts(normalize=True))
#fran_id are the sport team names
#rename column
nba = nba.rename({'fran_id':'playing_team'}, axis = 1)
#find out more about opp_fran
#print(nba_trends.opp_fran.value_counts(normalize = True))
#opp_fran are sport team names as well
#rename column
nba = nba.rename({'opp_fran':'opp_team'}, axis = 1)
#find out more about game location
print(nba.game_location.value_counts(normalize = True))
#have values of H and N; H is home and N is not home


#Visualizations and Analysis

#Question 1: Is forecast of winning linearly associated to points won? (for all 53 teams):DONE
#Two Quantitative Variables
corr_forecast_pointdiff, p = pearsonr(nba.forecast, nba.pts)
print(corr_forecast_pointdiff)
pts_vs_forecast = plt.scatter(nba.forecast, nba.pts, color = 'orange')
plt.xlabel('Forecast')
plt.ylabel('Points Scored')
plt.annotate(str(np.round(corr_forecast_pointdiff,2)), xy=(0.05, 0.95), xycoords='axes fraction')
plt.title('Points Scored vs Forecast')
plt.savefig('points_scored_vs_forecast.jpg')
plt.show()
plt.close()

# 0.2 indicates no linear association, below 0.3 

#Question 2: Does game location affect points for a team?:DONE
#First determine how many teams there are
print(nba.playing_team.nunique())
# 53 teams
#check there are minimum of 3 data points for each team for each game location
teams_with_two_locations = nba.groupby(['playing_team','game_location'])['game_location'].count()
teams_with_two_locations = teams_with_two_locations.to_frame(name = 'game_location_count').reset_index()
#print(teams_with_two_locations.head())
teams_with_two_locations = teams_with_two_locations.pivot(index = 'playing_team', columns = 'game_location', values = 'game_location_count')
#print(teams_with_two_locations.head())
teams_for_analysis = teams_with_two_locations[(teams_with_two_locations['H'] >=3) & (teams_with_two_locations['N'] >=3)]
print(teams_for_analysis.head())
print(teams_for_analysis.shape)
#Analysis reveals there are only two teams (Clippers and Nets) that have data for game locations higher than three
# for home (H) and not at home (N).
#One Categorical Variable, One Quantitative Variable
#graph for each team, with location on x axis and points on y axis
def points_vs_game_location(bballteams,name):
    i=1
    fig = plt.figure(figsize=(10,5))
    color = iter(cm.rainbow(np.linspace(0,1,5)))
    for value in bballteams.index:
        #print(value)
        team = nba[nba.playing_team == str(value)]
        plt.subplot(1,2,i)
        c= next(color)
        sns.boxplot(x = team.game_location, y = team.pts,color=c)
        plt.xlabel('Game Location')
        plt.ylabel('Points Scored')  
        plt.title(str.upper(value) + ': Points vs Game Location')
        plt.legend(['h =home', 'n=not home'])
        i+=1
    fig.tight_layout()
    fig.savefig(name)
    plt.show()
    plt.close()
points_vs_game_location(teams_for_analysis,'points_scored_vs_location.jpg')
#Some association: all teams show that location affects the points scored in the game

#Question 3: Is playing team and game result associated?: DONE
#Two Categorical Variables
#contingency table
# since there are 53 teams, choose top 5 highest scoring teams and lowest 5 scoring teams
# calculate mean scored for each team
scores = nba.groupby('playing_team').pts.mean().reset_index()
scores = scores.sort_values(by='pts', ascending = False)
#print(scores.head())
top_teams = scores.head()
#print(scores.tail())
bottom_teams = scores.tail()
ten_teams = top_teams.append(bottom_teams)
nba_ten_teams = nba[nba['playing_team'].isin(ten_teams.playing_team.value_counts().index)]
print(nba_ten_teams.head())
#Assumptions & Checks:
#Both variables are categorical
#All observations independent (value in one observation does not affect another observation)
#Cells in table are mutually exclusive (can only belong to one cell at a time)
#check that expected value of both categorical variables is greater than 5
#expected value: (row sum * column sum)/ table sum
gamelocationvsresult_expected = pd.crosstab(nba_ten_teams.playing_team,nba_ten_teams.game_result)
print(gamelocationvsresult_expected)
#all greater than 5, good to proceed
gamelocationvsresult_freq = gamelocationvsresult_expected/ len(nba_ten_teams)
print(gamelocationvsresult_freq)
chi2, locationvsresultpval, dof, locationvsresultexpected = chi2_contingency(gamelocationvsresult_freq)
print(np.round(locationvsresultexpected,2))
print(locationvsresultpval)
#significance value of 0.05
#null: playing_team and game_result are not associated
#alternate: playing_team and game_result are associated
#if pvalue less than or equal 0.05: reject null (null: playing_team and game result are not associated)
#if pvalue greater than 0.05: fail to reject null
#pval at 0.99
#playing_team and game_result are not associated

#Question 4: Is there an association between points won and opposing points won for the top 5 teams and bottom 5 teams?: DONE
def scatterplot_teams(teams,name):
    color = iter(cm.rainbow(np.linspace(0, 1, 5)))
    fig = plt.figure(figsize=(12,12))
    i=1
    for value in teams.playing_team:
        #print(value)
        team = nba[nba.playing_team == str(value)]
        plt.subplot(3,3,i)
        c= next(color)
        plt.xlabel('Points Scored')
        plt.ylabel('Opposing Team Points Scored')  
        plt.scatter(x=team.pts, y= team.opp_pts, c=c)
        corr_point_vs_opp_pts, p = pearsonr(team.pts, team.opp_pts)
        plt.annotate(str(np.round(corr_point_vs_opp_pts,2)), xy=(0.05, 0.95), xycoords='axes fraction')
        plt.title(str.upper(value) + ': Points vs Opposing Points')
        i+=1
    fig.tight_layout()
    plt.show()
    fig.savefig(name)
    plt.close()
scatterplot_teams(top_teams, 'top_teams_ptswon_vs_opposing_ptswon.jpg')
scatterplot_teams(bottom_teams, 'bottom_teams_ptswon_vs_opposing_ptswon.jpg')
# #no strong correlation but some linear correlation, all above 0.3 but less than 0.6

#Question 5: Is there an association between top 5 teams and points won?:DONE
#one categorical variable, one quantitative variable
#histogram to see distribution of points
#histogram only takes one variable, need to create series for each team
condors = nba.pts[nba.playing_team =='Condors']
stars = nba.pts[nba.playing_team =='Stars']
floridians = nba.pts[nba.playing_team =='Floridians']
squires = nba.pts[nba.playing_team =='Squires']
colonels = nba.pts[nba.playing_team =='Colonels']
plt.hist(condors, color = 'green' , label = 'Condors', density = True, alpha = 0.5)
plt.hist(stars, color = 'blue' , label = 'Stars', density = True, alpha = 0.5)
plt.hist(floridians, color = 'red' , label = 'Floridians', density = True, alpha = 0.5)
plt.hist(squires, color = 'yellow' , label = 'Squires', density = True, alpha = 0.5)
plt.hist(colonels, color = 'orange' , label = 'Colonels', density = True, alpha = 0.5)
plt.xlabel('Playing Team')
plt.ylabel('Points Scored')
plt.title('Top 5 Teams: Points Scored Distribution')
plt.legend()
plt.savefig('top5teams_pts_scored_hist.jpg')
plt.show()
plt.close()
#some overlap




#Statistic Checks:
#normally distributed variables?  & independent samples?  (affects statistical test performed)
#no statistical test performed that is dependent on normal distribution
# Central Limit Theorem: if sample size larger than 30, sample means are normally distributed

#Inaccurate/ Incorrect Data? - can only verify through visual representation - none

#Inconsistent/ Conflicting Data? - can verify through visual representation - none
