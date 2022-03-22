class Player:
    def __init__(self, name, nationality, assists, goals, penalties, games, team):
        self.name = name
        self.nationality= nationality
        self.assists=assists
        self.goals=goals
        self.penalties=penalties
        self.games=games
        self.team=team
    
    @property
    def get_points(self):
        return self.goals+self.assists
    
    def __str__(self):
        return f"{self.name:20}, {self.team}, {self.goals}+{self.assists} = {self.get_points} "