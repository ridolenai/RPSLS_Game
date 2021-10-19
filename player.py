gesture_options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

#defines a player and takes gesture input
class Player:
    def __init__(self, score):
        self.name = input ('Enter your name please: ')
        self.score = 0

    def gesture_choice(self):
        self = input('Which gesture do you choose?: ')
