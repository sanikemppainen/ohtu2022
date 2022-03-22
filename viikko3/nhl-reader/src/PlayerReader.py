from typing import Iterator
import requests
from player import Player
from typing import List

class PlayerReader:
    def __init__(self, url):
        self.url=url
    
    def get_players(self)-> List[Player]:
        response = requests.get(self.url).json()
        players = []
        for player_dict in response:
            player = Player(
                player_dict['name'],
                player_dict['nationality'],
                int(player_dict['assists']),
                int(player_dict['goals']),
                int(player_dict['penalties']),
                int(player_dict['games']),
                player_dict['team']
                )
            players.append(player)
        return players

 

