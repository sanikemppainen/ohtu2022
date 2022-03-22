class Player:
    def __init__(self, name, nationality, assists, goals, penalties, games, team):
        self.name = name
        self.nationality= nationality
        self.assists=assists
        self.goals=goals
        self.penalties=penalties
        self.games=games
        self.team=team
    
    def __str__(self):
        return f"{self.name}, {self.team}, {self.goals}, {self.assists}, {self.games}, {self.penalties} "