# # NFL Statisitcal Analysis by Position using nflgame module

# ### Import Modules:

import time 
import nflgame
import datetime
import numpy as np
import pandas as pd
import cufflinks as cf
import plotly.plotly as py
from nflgame import statmap
from datetime import timedelta


### Defining Dates:

today = datetime.date.today() 
tmnice = today.strftime('%Y-%m-%d')
year = today.strftime('%Y')
month = today.strftime('%m')

# Define year range 
if int(month) >= 9:
    year = int(year)
else:
    year = int(year) -1
    
years = []
start_year = 2008
while start_year < year:
    start_year = start_year + 1 
    years.append(start_year) 


### Converting Statistical Categories into Pandas Dataframes:

def get_passing_stats(): 
    stats = pd.DataFrame()
    for year in years: 
        game    = nflgame.games(year)
        players = nflgame.combine_game_stats(game)
        df = pd.DataFrame([(p, p.passing_yds, p.passing_att, p.passing_cmp, p.passing_tds, p.rushing_tds) for p in players.passing()])
        df.columns= ['QB','Passing Yards', 'Passing Atp', 'Passing Comp','Passing TDs', 'Rushing TDs'] 
        df['year'] = year
        df['QB'] = df['QB'].astype(str)
        stats = stats.append(df)
    return stats


def get_rushing_stats(): 
    stats = pd.DataFrame()
    for year in years: 
        game    = nflgame.games(year)
        players = nflgame.combine_game_stats(game)
        df = pd.DataFrame([(p, p.rushing_yds, p.rushing_att, p.rushing_tds) for p in players.rushing()])
        df.columns= ['RB','Rushing Yards', 'Rushing Atp','Rushing TDs'] 
        df['year'] = year
        df['RB'] = df['RB'].astype(str)
        stats = stats.append(df)
    return stats

def get_receiving_stats(): 
    stats = pd.DataFrame()
    for year in years: 
        game    = nflgame.games(year)
        players = nflgame.combine_game_stats(game)
        df = pd.DataFrame([(p, p.receiving_yds, p.receiving_rec, p.receiving_tds) for p in players.receiving()])
        df.columns= ['WR','Receiving Yards', 'Receptions','Receiving TDs'] 
        df['year'] = year
        df['WR'] = df['WR'].astype(str)
        stats = stats.append(df)
    return stats


### STILL TO BE DEFINED 
def get_def_stats():

def get_kicking_stats():


### Call Functions:

passing_stats = get_passing_stats()
receiving_stats = get_receiving_stats()
rushing_stats = get_rushing_stats()


### Top Ten Statistical Categories:

passing_stats.sort_values('Passing TDs',ascending=False).head(n=10)
receiving_stats.sort_values('Receiving TDs',ascending=False).head(n=10)
rushing_stats.sort_values('Rushing TDs',ascending=False).head(n=10)

### Query By Player:

passing_stats[passing_stats['QB'] == 'T.Brady']


### Graphical Analyses:

stats_over_10 =passing_stats[passing_stats['Passing TDs'] > 10]

stats_over_10.iplot(kind='scatter', 
                    mode='markers', 
                    x='Passing Yards', 
                    y='Passing TDs', 
                    text = 'QB',
                    filename='simple-scatter',
                    title = 'TD v. Passing Yards 2009-2016')

df =stats_over_10

py.iplot(
    {
        'data': [
            {
                'x': df[df['year']==year]['Passing Yards'],
                'y': df[df['year']==year]['Passing TDs'],
                'name': year, 
                'mode': 'markers',
                'text': df[df['year']==year]['QB']
            } for year in years
        ],
        'layout': {
            'xaxis': {'title': 'Passing Yards', 'type': 'log'},
            'yaxis': {'title': "Touchdowns", 'type': 'log'},
            'title': 'TDs v. Passing Yards 2009-2016'
            
        }
}, filename='scatter-group-by')


rushing_stats.iplot(kind='scatter', 
                    mode='markers', 
                    x='Rushing Yards', 
                    y='Rushing TDs', 
                    filename='simple-scatter', 
                    title = 'TD v. Rushing Yards 2009-2016')


top_rush =rushing_stats[rushing_stats['Rushing TDs'] > 15]
top_rush.iplot(kind='bubble', x='Rushing TDs', y='Rushing Yards', size='Rushing TDs', text='RB',
             xTitle='Rushing TDs', yTitle='Rushing Yards',
             filename='simple-bubble-chart')


#### Note:  *The earliest data avaliable through the nflgame module scrape is the 2009 NFL season.* 

### Please the nflgame module [here](https://github.com/BurntSushi/nflgame)


statmap.categories

data  = pd.DataFrame(statmap.idmap).transpose()

y=data[['cat','desc','fields']]

y[y['cat']=='passing']

roster = {'QB': 1, 
          'RB': 2, 
          'WR': 3, 
          'TE': 1, 
          'WR/RB/TE': 1, 
          'K': 1, 
          'DEF': 1,
          'Bench': 5,
          'IR': 1}

off_scoring =[{'stat':'passing_yards','points': .04},
              {'stat':'rushing_yards','points': .01},
              {'stat':'receiving_years','points': .01},
              {'stat':'passing_td','points': 4},
              {'stat':'rushing_td','points': 6}, 
              {'stat':'receiving_td','points': 6},
              {'stat':'fumble_lost','points': -2},
              {'stat':'interception','points': -2},
              {'stat':'two_pt_con_pass_td','points': 2},
              {'stat':'two_pt_con_rush_td','points': 2},
              {'stat':'two_pt_con_catch_td','points': 2},
              {'stat':'two_pt_con_pass_recp','points': 1}]
 
def_scoring = [{'stat': 'sack', 'points': 1},
               {'stat': 'interception', 'points': 2},
               {'stat': 'fumble_recovery', 'points': 2},
               {'stat': 'touchdown', 'points': 6},
               {'stat': 'saftey', 'points': 3},
               {'stat': 'blocked_kick', 'points': 2},
               {'stat': 'points_allowed_0', 'points':20},
               {'stat': 'points_allowed_1_6', 'points':15},
               {'stat': 'points_allowed_7_13', 'points':10},
               {'stat': 'points_allowed_14_20', 'points':5},
               {'stat': 'points_allowed_21_27', 'points':0},
               {'stat': 'points_allowed_26_34', 'points':-5},
               {'stat': 'points_allowed_35_or_more', 'points':-10}]

k_scoring   = [{'stat': 'fg_0_19', 'points': 3},
               {'stat': 'fg_20_29', 'points': 3},
               {'stat': 'fg_30_39', 'points': 3},
               {'stat': 'fg_40_49', 'points': 4},
               {'stat': 'fg_50', 'points': 5},
               {'stat': 'fg_missed_0_19', 'points': -1},
               {'stat': 'fg_missed_20_29', 'points': -1},
               {'stat': 'fg_missed_30_39', 'points': -1},
               {'stat': 'fg_missed_40_49', 'points': -1},
               {'stat': 'fg_missed_50', 'points': 0},
               {'stat': 'pat_made', 'points': 1},
               {'stat': 'pat_missed', 'points': -1}]

pd.DataFrame(off_scoring)
pd.DataFrame(k_scoring)
pd.DataFrame(def_scoring)