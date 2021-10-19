from gestures import Gestures
from player import Player
from ai import AI

class Gameboards:
    def __init__ (self):
        self.welcome = print("Welcome to the wonderful world of trying to reason with Sheldon. \n I don't have any idea why you are going to try, but good luck. \n Scenario: you are sitting in Sheldon's spot so he is obviously unhappy.\n In a rare act of reasonable behavior, he has challenged you to a game of Rock Paper Scissors Lizard Spock.\n What's that you say? You don't know the rules?  Great, now we get to listen to him explain them AGAIN! \n Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, \n Spock smashes scissors, scissors decapitates lizard, lizard eats paper, paper disproves Spock, Spock vaporizes rock, \n and as it always has, rock crushes scissors.")
        self.player1 = None
        self.player2 = None  
        self.playerAI = None
                  
    def comparison(self, player1_selection, player2_selection):
        gesture_options = ['ROCK', 'PAPER', 'SCISSORS', 'LIZARD', 'SPOCK']
        self.y = Gestures(player1_selection)   
        if player1_selection.upper() == player2_selection.upper():
            return  
        if player1_selection.upper() not in gesture_options:
            print('Make another selection. ')
            return
        if self.y.rock(player1_selection.upper(), player2_selection.upper()) == True:
            self.player1.score += 1
            return
        elif self.y.paper(player1_selection.upper(), player2_selection.upper()) == True:
            self.player1.score += 1
            return
        elif self.y.scissors(player1_selection.upper(), player2_selection.upper()) == True:
            self.player1.score += 1
            return
        elif self.y.lizard(player1_selection.upper(), player2_selection.upper()) == True:
            self.player1.score += 1
            return
        elif self.y.spock(player1_selection.upper(), player2_selection.upper()) == True:
            self.player1.score += 1
            return
        else:
            self.player2.score += 1

    def competition(self):       
        quantity = input ('How many players will there be, 1 or 2? ')
        gesture_options = ['ROCK', 'PAPER', 'SCISSORS', 'LIZARD', 'SPOCK']
        
        if quantity == ('1'):
            self.player1= Player(0) 
            self.player2 = AI()
        elif quantity == ('2'):
            self.player1 = Player(0) 
            self.player2 = Player(0)
        if self.player1.name.upper() == 'SHELDON' or self.player2.name.upper() == 'SHELDON':
            print ("Fine, Sheldon, take your spot.  I'm going home")
            exit()
            
        print (f"So we have {self.player1.name} and {self.player2.name} competing for a spot on the couch today.  Well, let's get started.")
        while self.player1.score < (2) and self.player2.score < (2):
            print (f'Here are your options: {gesture_options}')
            player1_selection = (self.player1.gesture_choice())
            player2_selection = (self.player2.gesture_choice())
            if player1_selection.upper() and player2_selection.upper() in gesture_options:
                self.comparison(player1_selection.upper(), player2_selection.upper())
                
        if self.player1.score == 2:
            print (f'{self.player1.name} won.  {self.player1.name} gets the couch.')
        if self.player2.score == 2:
            print (f'{self.player2.name} won.  {self.player2.name} gets the couch.')
                    
                
                    
                
                    

    
