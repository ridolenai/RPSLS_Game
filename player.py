gesture_options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

class Player:
    def __init__(self, score):
        self.name = input ('Enter your name please: ')
        self.score = 0

    def gesture_choice(self):
        self = input(f'{self.name} please make a selection based off the options given above. ')
        return self
