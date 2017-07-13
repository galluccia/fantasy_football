# Scoring Dictonary  

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