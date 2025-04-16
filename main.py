import fastf1
from fastf1 import plotting
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

plotting.setup_mpl(misc_mpl_mods=False, color_scheme='fastf1')

# Enable caching to speed up subsequent accesses
fastf1.Cache.enable_cache('cache')

def main(year, race):
    session = fastf1.get_session(year, race +' Grand Prix', 'R')
    session.load()

    all_laps = session.laps

    stints = all_laps[["Driver", "Stint", "Compound", "LapNumber"]]
    stints = stints.groupby(["Driver", "Stint", "Compound"])
    stints = stints.count().reset_index()
    stints = stints.rename(columns={"LapNumber": "NumberOfLaps"})
    print(stints)

    cumulative_width = {driver: 0 for driver in stints["Driver"].unique()}

    for _, driver_stint in stints.iterrows():
        driver = driver_stint["Driver"]
        number_of_laps = driver_stint["NumberOfLaps"]
        compound = driver_stint["Compound"]

        plt.barh(
            driver,
            number_of_laps,
            left=cumulative_width[driver],  # Start the bar at the cumulative width
            edgecolor="black",
            color={
                "MEDIUM": "yellow",
                "HARD": "white",
                "SOFT" or "SUPERSOFT": "red",
                "HYPERSOFT": "pink",
                "INTERMEDIATE": "green",
                "WET": "blue",
            }.get(compound, "gray") # if Compound is unrecognized
        )

        cumulative_width[driver] += number_of_laps

    plt.xlabel("Number of Laps")
    plt.ylabel("Driver")
    plt.title(f"Tire Starategy Comparison in {race} {year}")
    plt.show()

    

    

def get_race_name(year):
    races = fastf1.get_event_schedule(year)["Country"].unique()
    race_name = input("Enter the name of the race: ").capitalize()
    while not (race_name in races):
        for race in races:
            print(race)
        race_name = input("Race not found! Please, enter a valid race name: ")
    
    return race_name

def welcome():
    year = int(input("Year (e.g., 2023): "))
    race = get_race_name(year)

    main(year, race)

if __name__ == "__main__":
    welcome()
