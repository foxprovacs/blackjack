import players
from blackjack import Game

game = Game()
game.add_player(players.BasicPlayer('Basic Player'))
game.add_player(players.SmartPlayer('Smart Player'))

for i in range(1,101):
    game.play()
    print('-----------------')
    print(game)


