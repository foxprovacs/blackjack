import players
from blackjack import Game

game = Game()
game.add_player(players.RealPlayer('Real Player'))
game.add_player(players.SmartPlayer('Smart Player'))

game.play()
print('-----------------')
print(game)

