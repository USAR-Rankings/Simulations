import pandas as pd
import numpy as np
import math
import random as random
import itertools as itertools
import copy

# Read in name corrections
corrections_df = pd.read_csv('../data/name_corrections.csv')
corrections_dict = dict(zip(corrections_df['OldName'].str.strip().str.upper(), corrections_df['NewName'].str.strip()))


# Function to correct player names
def correct_name(name):
    return corrections_dict.get(name.strip().upper(), name.strip())

def correct_names(df):# Apply corrections to Player1 and Player2 columns
    df['Player1'] = df['Player1'].apply(correct_name)
    df['Player2'] = df['Player2'].apply(correct_name)
    return df

# Functions to get player ratings
def get_rating_player(player,df,tourney): # From MM
    player=player.upper()
    filt_df =df[(df["Name"]==player)&(df["tourney"]==tourney)]
    if len(filt_df)>0:
        return (df[(df["Name"]==player)&(df["tourney"]==tourney)].reset_index(drop=True)["score"][0]* 10 +100).round(2)
    else:
        return 100
    
def get_rating_player(player,df,tourney,default=800):
    player=player.upper()
    filt_df =df[(df["name"]==player)&(df["Tournament"]==tourney)]
    if len(filt_df)>0:
        return (df[(df["name"]==player)&(df["Tournament"]==tourney)].reset_index(drop=True)["elo"][0]).round(2)
    else:
        return default

def get_ratings_all(teams,df,tourney,default=800):
    teams["P1 Rating"]=[get_rating_player(x,df,tourney,default) for x in teams["Player1"]]
    teams["P2 Rating"]=[get_rating_player(x,df,tourney,default) for x in teams["Player2"]]
    teams["Team Rating"]= teams[["P1 Rating", "P2 Rating"]].mean(axis=1).round(2)
    return teams.sort_values(by="Team Rating", ascending=False).reset_index(drop=True)


# Read in players and correct name
open_teams=pd.read_csv("../data/south25_open.csv")
open_teams=correct_names(open_teams)

# Read in most recent rankings
open_rating=pd.read_csv("../data/test_final_players_open_2025-04-25.csv")

# Select what tournamnets rankings to use
open_teams=get_ratings_all(open_teams,open_rating,"PHOENIX-SECTIONAL-25")

# Output results
open_teams.to_csv("../data/south25_open.csv",index=False)
