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
        table = self.players + [self.dealer]
        for p in table:

            if isinstance(p, players.Dealer):
                p.curr_hand.cards[0].is_visible = True

            while not p.is_bust() and p.should_hit():
                c = self.shoe.draw()
                p.curr_hand.add(c)

            self.set_winners()
        
    def set_winners(self):
        dealer_score = self.dealer.curr_hand.score()

        for p in self.players:
            curr_player_score = p.curr_hand.score()

            if p.is_bust():
                p.game_flag = GameStatus.Loss
            elif p.curr_hand.is_blackjack() and not self.dealer.curr_hand.is_blackjack():
                p.game_flag = GameStatus.Win
            elif curr_player_score > dealer_score:
                p.game_flag = GameStatus.Win
            elif self.dealer.is_bust():
                p.game_flag = GameStatus.Win