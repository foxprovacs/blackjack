import blackjack_players
from blackjack import Game

game = Game()
game.add_player(blackjack_players.RealPlayer('Real Player'))
game.add_player(blackjack_players.SmartPlayer('Smart Player'))

game.play()
print('-----------------')
print(game)

