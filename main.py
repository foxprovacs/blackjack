import players
from blackjack import Game

game = Game()
game.add_player(players.RealPlayer('Real Player'))
game.add_player(players.BasicPlayer('Basic Player'))

game.play()
print('-----------------')
print(game)

