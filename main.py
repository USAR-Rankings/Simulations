import pandas as pd
from usar_sim import *



def main():
    # For ease of input I created a csv with the teams and thier ratings as an average of the two player
    open_teams=pd.read_csv("data/Teams_open_national2023.csv")

    #Create a team dictionary out of the teams playing
    team_dict=dict(zip(open_teams["Team"],open_teams["Team Rating"]))
    
    # Set up pools
    open_pools=[['Rouge',"Le Pirate","J Chillin","Mike and Sully"],
                ['Finocchi/Picone',"Dinomite", "Blackmail","Fresh Cuts"],
                ["Gross/Shaytar","Degenerates","Dethrone","TBD"],
                ["Bot House","Outrageous","Risky Business","Party Crashers"],
                ["TRP Blank Check","TRP Fleet Footwork","Beeks/Porter","Poiuytres"],
                ["Lowkey","Lazy","Pickle Juice", "El Nino"],
                ["Slither","BorderLine","Stupid Time Sensitive Discounts","Bangla Tigers"],
                ["Not TBD","BackPaqued","Ryder/Roundnet","Seatbelts"]]  
    
    # Set up simulation
    nationals=Multi_Simulator(open_pools,team_dict)

    # Run Simulation
    nationals.sim_n(32,1000,bracket_keys)

    # Export Results
    nationals.export_results(tag="Florida_Nationals")