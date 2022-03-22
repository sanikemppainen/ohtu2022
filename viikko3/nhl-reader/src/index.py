import requests
from player import Player
from PlayerStats import PlayerStats
from PlayerReader import PlayerReader

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    player_reader= PlayerReader(url)
    player_stats= PlayerStats(player_reader)

    player_stats.sorted_scores()
    


if __name__ == "__main__":
    main()
