# Data Grab Functions 

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