

if player2_selection.upper() == ('ROCK'):
                print(f'{self.player1.name} wins because Spock vaporized Rock')
                self.player1.score += 1
            elif player2_selection.upper() == ('PAPER'):
                print(f'{self.player2.name} wins because Paper disproves Spock')
                self.player2.score += 1
            elif player2_selection.upper() == ('SCISSORS'):
                print(f'{self.player1.name} wins because Spock smashes Scissors')
                self.player1.score += 1
            else:
                player2_selection.upper() == ('LIZARD')
                print(f'{self.player2.name} wins because Lizard poisons Spock')
                self.player2.score += 1