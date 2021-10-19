class Gestures:

    def __init__(self, player1_selection):
        self = None
        player1_selection = None

    def rock(self, player1_selection, player2_selection):
        if player1_selection == ('ROCK') and player2_selection == ('LIZARD'): 
            return True
        elif player1_selection == ('ROCK') and player2_selection == ('SCISSORS'):
            return True
        else:
            return False
    def paper(self, player1_selection, player2_selection):
        if player1_selection == ('PAPER') and player2_selection == ('ROCK'): 
            return True
        elif player1_selection == ('PAPER') and player2_selection == ('SPOCK'):
            return True
        else:
            return False

    def scissors(self, player1_selection, player2_selection):
        if player1_selection == ('SCISSORS') and player2_selection == ('PAPER'):
            return True
        elif player1_selection == ('SCISSORS') and player2_selection== ('LIZARD'):
            return True
        else:
            return False

    def lizard (self, player1_selection, player2_selection):
        if player1_selection == ('LIZARD') and player2_selection == ('SPOCK'):
            return True
        elif player1_selection == ('LIZARD') and player2_selection == ('PAPER'):
            return True
        else: 
            return False

    def spock (self, player1_selection, player2_selection):
        if player1_selection == ('SPOCK') and player2_selection == ('SCISSORS'):
            return True
        elif player1_selection == ('SPOCK') and player2_selection == ('ROCK'):
            return True
        else:
            return False