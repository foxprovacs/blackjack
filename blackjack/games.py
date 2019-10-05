import blackjack.players as players
import blackjack.cards as cards
from blackjack.players import GameStatus

class Game:

    def __init__(self, number_of_decks=8):
        self.players = []
        self.number_of_decks = number_of_decks
        self.shoe = cards.Shoe(number_of_decks)
        self.dealer = players.Dealer()

    def add_player(self, player):
        # print('Adding player {0} to game'.format(player.name))
        self.players.append(player)
        player.game = self

    def __repr__(self):
        s = 'Game:\n'
        s += '\tNumber of decks = ' + str(self.number_of_decks)
        s += '\n\tPlayers:\n'
        s += '\t' + str(self.dealer) + str(self.dealer.curr_hand) + '\n'
        for p in self.players:
            s += '\t\t' + str(p) + ':' + str(p.curr_hand) + ' -> '+ str(p.game_flag.name) + '\n'
    
        return s

    def clear(self):
        for p in self.players:
            p.clear()
        self.dealer.clear()

    def deal(self):
        self.clear()

        table = self.players + [self.dealer]
        for i in range(0,2):
            for p in table:
                card = self.shoe.draw(is_face_down= ((i==0) & (isinstance(p, players.Dealer))))
                p.curr_hand.add(card)   

    def play(self):
        #print('----play called----')
        table = self.players + [self.dealer]
        for p in table:

            if isinstance(p, players.Dealer):
                p.curr_hand.cards[0].is_visible = True

            while not p.curr_hand.is_bust() and p.should_hit():
                c = self.shoe.draw()
                p.curr_hand.add(c)

        self.set_winners()
        
    def set_winners(self):
        #print('set_winnners called')
        dealer_score = self.dealer.curr_hand.score()
        #print('set_winners player count: {}'.format(len(self.players)))
        for p in self.players:
            curr_player_score = p.curr_hand.score()

            if p.curr_hand.is_bust():
                p.game_flag = GameStatus.Loss
                p.losses += 1
            elif p.curr_hand.is_blackjack() and not self.dealer.curr_hand.is_blackjack():
                p.game_flag = GameStatus.Win
                p.wins += 1
            elif curr_player_score > dealer_score and not p.curr_hand.is_bust():
                p.game_flag = GameStatus.Win
                p.wins +=1 
            elif curr_player_score == dealer_score and not self.dealer.curr_hand.is_blackjack():
                p.game_flag = GameStatus.Draw
                p.draws += 1
            elif self.dealer.curr_hand.is_bust():
                p.game_flag = GameStatus.Win
                p.wins +=1 
            elif self.dealer.curr_hand.is_blackjack() and curr_player_score < 21:
                p.game_flag = GameStatus.Loss
                p.losses += 1
            elif not self.dealer.curr_hand.is_bust() and (self.dealer.curr_hand.score() > curr_player_score):
                p.game_flag = GameStatus.Loss
                p.losses += 1

            # print('{0} this hand: {1}'.format(p.name, p.game_flag.name))
            #print('{0}:{1} wins, {2} losses, {3} draws'.format(p.name, str(p.wins), str(p.losses), str(p.draws)))
 