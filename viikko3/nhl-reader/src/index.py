import requests
from player import Player

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)

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

    print("Oliot:")

    players.sort(key=lambda x: x.get_points, reverse=True)

    for player in players:
        if player.nationality=='FIN':
            print(player)
            


if __name__ == "__main__":
    main()
