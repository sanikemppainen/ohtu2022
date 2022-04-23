from numpy import diff


class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.individual_score=""
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.scores={0: "Love-all", 1:"Fifteen-all", 2:"Thirty-all", 3:"Forty-all"}

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):

        if self.player1_score == self.player2_score:
            self.even_score()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            self.which_won()
        else:
            self.set_score()
        return self.score
    
    def even_score(self): 
        if self.player1_score <= 3:
            self.score = self.scores[self.player1_score]
        else:
            self.score="Deuce"
    
    def which_won(self):
        difference = self.player1_score-self.player2_score
        if difference == 1:
            self.score = "Advantage player1"
        elif difference == -1:
            self.score = "Advantage player2"
        elif difference >= 2:
            self.score = "Win for player1"
        else:
            self.score = "Win for player2"

    def set_score(self):
        self.score = self.scores[self.player1_score] +" + "+ self.scores[self.player2_score]         


            