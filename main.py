import players
from blackjack import Game

game = Game()
game.add_player(players.LivePlayer('Real Player'))
game.add_player(players.BasicPlayer('Basic Player'))

game.deal()
game.play()
print('-----------------')
print(game)

