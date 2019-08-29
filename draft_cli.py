#!/usr/local/bin/python3
"""
purpose of this is to give you a rich feature set to be of assistance you during the draft 

TODO:
 - abilily to run optimization based on:
    projected stats
    strength of schedule
    bye weeks
    
"""
import sys
import cmd
import readline
import pandas as pd
from tabulate import tabulate

class MyCmd(cmd.Cmd):

    def __init__(self, showintro=True):
        self.prompt = "mmlol>"
        self.intro = """
         /$$      /$$ /$$      /$$ /$$        /$$$$$$  /$$      
        | $$$    /$$$| $$$    /$$$| $$       /$$__  $$| $$      
        | $$$$  /$$$$| $$$$  /$$$$| $$      | $$  \ $$| $$      
        | $$ $$/$$ $$| $$ $$/$$ $$| $$      | $$  | $$| $$      
        | $$  $$$| $$| $$  $$$| $$| $$      | $$  | $$| $$      
        | $$\  $ | $$| $$\  $ | $$| $$      | $$  | $$| $$      
        | $$ \/  | $$| $$ \/  | $$| $$$$$$$$|  $$$$$$/| $$$$$$$$
        |__/     |__/|__/     |__/|________/ \______/ |________/
        """ if showintro else ""             
        self.draft = pd.read_csv("draft_order.csv")
        self.available_players = pd.read_csv("available_players.csv")
        self.player_list = pd.read_csv("available_players.csv").Player.tolist()
        self.player_pos = pd.read_csv("available_players.csv").set_index('Player').Pos.to_dict()
        self.has_been_chosen = dict()
        self.managers = [str(x).lower().strip() for x in self.draft.team.unique()]
        self.round = 0 
        self.roster = {
            'QB': None,
            'RB1': "David Johnson",
            'RB2': None,
            'WR1': None,
            'WR2': "M. Valdes-Scantling",
            'WR3': "A. Humphries",
            'TE': "O.J Howard",
            'FLEX': None,
            'D/ST': None,
            'K':  None,
            'BE': None,
            'BE': None,
            'BE': None,
            'BE': None,
            'BE': None,
            'BE': None,
        }
        cmd.Cmd.__init__(self)

    def do_slots(self, inp):
        slots_to_fill = [
            slot for slot in self.roster.keys() 
            if self.roster[slot] == None
        ]
        for s in slots_to_fill: print(s)
        
    def do_roster(self, inp):
        print(tabulate(pd.DataFrame([self.roster]),
            headers='keys', 
            tablefmt='fancy_grid', 
            showindex=False
            )
        )

    def do_remove(self, s):
        vaild = False
        while not vaild:
            team = input("who picked them? ")
            if str(team).lower() in self.managers:
                vaild = True
            else:
                print(team, 'is not a manager, check spelling')

        if s not in self.player_list:
            if s in self.has_been_chosen:
                print(s, 'has already been picked')
            else:
                print('player not in player list, check spelling')
        else:
            print(s, 'has been picked by', team)
            self.has_been_chosen.update({s:team})
            self.player_list.remove(s)
        self.round += 1        

    def do_add(self, s):
        if s not in self.player_list:
            if s in self.has_been_chosen:
                print(s, 'has already been picked')
            else:
                print('player not in player list check spelling')
        else:
            print(s, 'has been added')
            self.has_been_chosen.update({s:"gucci"})
            self.player_list.remove(s)
            player_pos = self.player_pos.get(s)
            slots_to_fill = [
                slot for slot in self.roster.keys() 
                if self.roster[slot] == None
            ]
            pos_to_fill = sorted([x for x in slots_to_fill if x.startswith(player_pos)])[0]
            if not pos_to_fill:
                pos_to_fill = 'BE'
            self.roster[pos_to_fill] = s 
        self.round += 1

    def complete_add(self, text, line, begidx, endidx):
        mline = line.partition(' ')[2]
        offs = len(mline) - len(text)
        return [s[offs:] for s in self.player_list if s.startswith(mline)]

    def complete_remove(self, text, line, begidx, endidx):
        mline = line.partition(' ')[2]
        offs = len(mline) - len(text)
        return [s[offs:] for s in self.player_list if s.startswith(mline)]

    def help_add(self):
        print("add player to your team")
        
    def help_remove(self):
        print("reomve player from eligble draft pool")
    
    def do_nextBest(self, inp):
        if inp:
            print(tabulate(
                self.available_players[
                    (self.available_players.Pos==inp) & 
                    (~self.available_players.Player.isin(self.has_been_chosen))].head(5),
                headers='keys', 
                tablefmt='fancy_grid', 
                showindex=False
                )
            )
        else:
            for pos in self.available_players.Pos.unique():
                print(tabulate(
                    self.available_players[
                        (self.available_players.Pos==pos) & 
                        (~self.available_players.Player.isin(self.has_been_chosen))].head(5),
                    headers='keys', 
                    tablefmt='fancy_grid', 
                    showindex=False
                    )
                )

    def do_whosePick(self, inp):
        print(
            tabulate(self.draft.loc[self.round]
                .to_frame()
                .transpose()
                .set_index('pick'), 
                headers='keys', tablefmt='fancy_grid'
            )
        )

    def update_data(self):
        """helper fn to update data whenever add or delete is called"""
        

    def do_clear(self, inp):
        import subprocess; subprocess.call('clear', shell=True)

    def do_quit(self, inp):
            sys.exit('exiting')

    def default(self, inp):
        if inp in ['k', 'clear']:
            self.do_clear(inp)
        if inp in ['q', 'quit']:
            self.do_quit(inp)


if __name__ == '__main__':
    my_cmd = MyCmd()
    my_cmd.cmdloop()
