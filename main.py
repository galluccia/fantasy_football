import time 
import nflgame
import datetime
import numpy as np
import pandas as pd
import fantasy_fns as fns
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