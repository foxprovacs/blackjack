import blackjack.games as games
import blackjack.players as players

game = games.Game()
game.add_player(players.BasicPlayer('Basic Player 1'))
# game.add_player(players.BasicPlayer('Basic Player 2'))
# game.add_player(players.BasicPlayer('Basic Player 3'))
# game.add_player(players.BasicPlayer('Basic Player 4'))
game.add_player(players.SmartPlayer('Smart Player 1'))
game.add_player(players.PsychicPlayer('Psychic Player 1'))


# for p in game.players:
#     print('{0}:{1} wins, {2} losses, {3} draws'.format(p.name, str(p.wins), str(p.losses), str(p.draws)))

number_of_hands = 1000
debug_output = False
for i in range(1,number_of_hands+1):
    #print('Playing game {0}'.format(str(i)))
    game.deal()
    game.play()

    if debug_output:
        print(game) 

for p in game.players:
    win_rate = p.wins / (p.wins + p.losses + p.draws)
    success_rate = (p.wins + p.draws) / (p.wins + p.losses + p.draws)
    print('{0}:{1} wins, {2} losses, {3} draws, {4} win rate, {5} success rate'.format(p.name, str(p.wins), str(p.losses), str(p.draws), str(win_rate), str(success_rate)))

print(len(game.players))