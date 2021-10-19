from player import Player
from random import choice

gesture_options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

class AI(Player):
    gesture_options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    def __init__(self):
        self.name = 'Hal'
        self.score = 0

    def gesture_choice(self):
        self = choice(gesture_options)
        print(f'Hal chose {self}') 
        return self

