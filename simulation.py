import blackjack.games as games
import blackjack.players as players

game = games.Game()
game.add_player(players.BasicPlayer('Basic Player 1'))
game.add_player(players.BasicPlayer('Basic Player 2'))
game.add_player(players.BasicPlayer('Basic Player 3'))
game.add_player(players.BasicPlayer('Basic Player 4'))
# game.add_player(players.SmartPlayer('Smart Player 1'))

number_of_hands = 2
for i in range(1,number_of_hands+1):
    game.deal()
    game.play()
    print(game)

