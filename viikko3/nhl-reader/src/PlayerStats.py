from typing import List
from PlayerReader import PlayerReader
from player import Player

class PlayerStats:
    def __init__(self, player_reader:PlayerReader):
        self.player_reader=player_reader

    def sorted_scores(self) -> List[Player]:
        print("Pelaajat:")
        return filter(
            lambda player: player.nationality == 'FIN', self.player_reader.get_players)
#        players=self.player_reader.get_players

#        players.sort(key=lambda x: x.get_points, reverse=True)
#        for player in players:
#            if player.nationality=='FIN':
#                print(player)
               