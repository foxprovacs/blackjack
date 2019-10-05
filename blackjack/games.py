import blackjack.players as players
import blackjack.cards as cards


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
            s += '\t\t' + str(p) + ':' + str(p.curr_hand) + '\n'
    
        return s

    def clear(self):
        # TODO: Need to clear the dealer's hand too
        for p in self.players:
            p.clear()

    def deal(self):
        table = self.players + [self.dealer]
        self.clear()
        for i in range(0,2):
            for p in table:
                card = self.shoe.draw(is_face_down= ((i==0) & (isinstance(p, players.Dealer))))
                p.curr_hand.add(card)   

    def show_cards(self):
        table = self.players + [self.dealer]
        for p in table:
            print(p, str(p.curr_hand))

    def play(self):
        table = self.players + [self.dealer]
        for p in table:

            if isinstance(p, players.Dealer):
                p.curr_hand.cards[0].is_visible = True

            while not p.is_bust() and p.should_hit():
                #print('{0} is drawing a card...'.format(p.name))
                c = self.shoe.draw()
                p.curr_hand.add(c)
        
        


    # def play(self, show_output=True):
    #     if show_output:
    #         print('Dealer is showing {}'.format(self.dealer.hand))

    #     for p in self.players.items():
    #         curr_player = p[1]
    #         if show_output:
    #             print('Player ' + p[0] + ': ' + str(p[1].hand))
    #         while not curr_player.is_bust() and curr_player.should_hit():
    #             curr_player.hand.add(self.draw())
    #             if show_output:
    #                 print('Player ' + p[0] + ': ' + str(p[1].hand))

    #     # Flip over the dealer's first card
    #     self.dealer.hand.cards[0].is_visible = True

    #     while self.dealer.should_hit():
    #         self.dealer.hand.add(self.draw())

    #     self.set_winners()



    # def set_winners(self):
    #     dealer_score = self.dealer.hand.score()

    #     for p in self.players.items():
    #         curr_player = p[1]
    #         curr_player_score = curr_player.hand.score()

    #         if curr_player.is_bust():
    #             curr_player.is_winner = False
    #         elif curr_player.hand.is_blackjack and not self.dealer.hand.is_blackjack:
    #             curr_player.is_winner = True
    #         elif curr_player_score > dealer_score:
    #             curr_player.is_winner = True
    #         elif self.dealer.is_bust():
    #             curr_player.is_winner = True

    # def deal(self):
    #     for i in range(1, 3):
    #         for p in self.players.items():
    #             p[1].hand.add(self.draw())

    #         c = self.draw()
    #         if i == 1:
    #             c.is_visible = False
    #         self.dealer.hand.add(c)

    #     # See if anyone has Blackjack
    #     for p in self.players.items():
    #         p[1].hand.is_blackjack = p[1].hand.score() == 21
    #     self.dealer.hand.is_blackjack = self.dealer.hand.score() == 21

    # def __repr__(self):
    #     s = 'Dealer: ' + str(self.dealer.hand) + ' = ' + str(self.dealer.hand.score())
    #     for p in self.players.items():
    #         s += '\nPlayer ' + p[0] + ': ' + str(p[1].hand) + ' = ' + str(p[1].hand.score()) \
    #              + (' Win!' if p[1].is_winner else ' Lose')
    #     return s

    # def clear(self):
    #     self.dealer.hand.clear()
    #     self.dealer.is_winner = False
    #     for p in self.players.items():
    #         p[1].hand.clear()
    #         p[1].is_winner = False

    # def dealer_showing(self):
    #     """ Players cannot see the first card drawn to the dealer """
    #     return self.dealer.hand.cards[1].get_value()
