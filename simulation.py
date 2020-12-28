import blackjack.games as games
import blackjack.players as players

game = games.Game()
game.add_player(players.BasicPlayer('Basic Player 1'))
game.add_player(players.BasicPlayer('Basic Player 2'))
game.add_player(players.BasicPlayer('Basic Player 3'))
game.add_player(players.BasicPlayer('Basic Player 4'))
# game.add_player(players.SmartPlayer('Smart Player 1'))

number_of_hands = 1
debug_output = True
for i in range(1, number_of_hands+1):
    game.deal()
    game.play()

    if debug_output:
        print(game)

for p in game.players:
    win_rate = p.wins / (p.wins + p.losses)
    loss_rate = p.losses / (p.wins + p.losses)
    draw_rate = p.draws / (p.wins + p.losses + p.draws)
    print('{0}:{1} wins, {2} losses, {3} draws, {4:.2f} win rate, {5:.2f} loss rate, {6:.2f} draw rate, '
          .format(p.name, p.wins, p.losses, p.draws, win_rate, loss_rate, draw_rate))