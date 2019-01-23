import blackjack_players
from blackjack import Game

game = Game()
game.add_player(blackjack_players.RealPlayer('A'))

game.simulate()
print('-----------------')
print(game)
