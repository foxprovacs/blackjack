from abc import ABC, abstractmethod
import blackjack.cards as cards


class Player(ABC):

    def __init__(self, name=''):
        self.curr_hand = cards.CardHand()
        self.name = name
        self.game = None
        self.is_winner = False

    def is_bust(self):
        return self.curr_hand.score() > 21

    @abstractmethod
    def should_hit(self):
        pass

    def __repr__(self):
        return self.name


class Dealer(Player):

    def __init__(self):
        super(Dealer, self).__init__()
        self.upcard = None

    def should_hit(self):
        return self.curr_hand.score() <= 16


class BasicPlayer(Player):

    def should_hit(self):
        return self.curr_hand.score() <= 10


class SmartPlayer(Player):

    def should_hit(self):
        curr_score = self.curr_hand.score()
        if self.is_bust():
            return False
        if curr_score <= 16 and self.game.dealer_showing() >= 10:
            return True
        else:
            return False


class CraftyCardCounterPlayer(Player):

    def should_hit(self):
        return True


class LivePlayer(Player):

    def should_hit(self):
        if self.curr_hand.score() < 21:
            x = input('(H)it or (S)tay? ')
            return x.upper() == 'H'
        else:
            return False
