import players
from blackjack import Game

game = Game()
game.add_player(players.BasicPlayer('Basic Player 1'))
# game.add_player(players.BasicPlayer('Basic Player 2'))
# game.add_player(players.BasicPlayer('Basic Player 3'))
# game.add_player(players.BasicPlayer('Basic Player 4'))
# game.add_player(players.SmartPlayer('Smart Player'))

win_tracker = {}

number_of_hands = 10000

for i in range(1, number_of_hands + 1):
    game.deal()
    game.play(show_output=False)

    for p in game.players.items():
        if p[1].is_winner:
            win_tracker[p[0]] = 1 + win_tracker.get(p[0], 0)
    if game.dealer.is_winner:
        win_tracker['dealer'] = 1 + win_tracker.get('dealer', 0)

    game.clear()

for i in win_tracker.items():
    print('{0}: {1}...{2}'.format(i[0], i[1], i[1]/number_of_hands))