import sys
import ast
import datetime
import pandas as pd
import requests as r


def main():

  today = datetime.date.today()
  tnice = today.strftime('%Y-%m-%d')

  # url to sleeper app (fantasy football analytics)
  url = 'https://sleeper.app/graphql' 

  # sleep payload to graphql db 
  payload = {
    "operationName": "season_stats",
    "variables": {    
    },
    "query": 
      "query season_stats { season_stats(category: \"proj\",sport: \"nfl\",season: \"2018\",season_type: \"regular\",order_by: \"adp_ppr\",positions: [\"QB\",\"RB\",\"WR\",\"TE\",\"K\",\"DEF\"]){category\ncompany\ndate\ngame_id\nopponent\nplayer\nplayer_id\nseason\nseason_type\nsport\nstats\nteam\nweek}}"
  }

  response = r.post(url, data=payload)
  try: 
    data = response.json()
    raw_data = data['data']['season_stats']
  except:
    print( 'response failed',response.text() )
    sys.exit()

  df = pd.DataFrame(raw_data)

  ls = []
  for index, row in df.iterrows():
      str_player_dict = row['player']
      player_dict = ast.literal_eval(str_player_dict)
      player_dict['team'] = row['team']
      ls.append(player_dict)
  table = pd.DataFrame(ls)
  table.to_csv('fantasy_football_rankings_'+tnice+'.csv')
  print('file conversion was sucessful')


if __name__ == '__main__':
  main()
