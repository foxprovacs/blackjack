from abc import ABC, abstractmethod
import blackjack.cards as cards
from enum import Enum


class GameStatus(Enum):
    Win = 1
    NotPlayed = 0
    Draw = 2
    Loss = 3


class Player(ABC):

    def __init__(self, name=''):
        self.curr_hand = cards.CardHand()
        self.name = name
        self.game = None
        self.game_flag = GameStatus.NotPlayed
        self.wins = 0
        self.losses = 0
        self.draws = 0

    # def is_bust(self):
    #     return self.curr_hand.score() > 21

    def clear(self):
        self.curr_hand = cards.CardHand()
        self.game_flag = GameStatus.NotPlayed

    @abstractmethod
    def should_hit(self):
        pass

    def __repr__(self):
        return self.name


class Dealer(Player):

    def __init__(self):
        super(Dealer, self).__init__('Dealer')
        self.upcard = None

    def should_hit(self):
        return self.curr_hand.score() <= 16

    def showing(self):
        return self.curr_hand.cards[1].get_value()


class BasicPlayer(Player):

    def should_hit(self):
        return self.curr_hand.score() <= 16


class SmartPlayer(Player):

    def should_hit(self):
        curr_score = self.curr_hand.score()
        if self.curr_hand.is_bust():
            return False
        if self.game.dealer.showing() <= 6:
            return True
        else:
            return False


class CraftyCardCounterPlayer(Player):

    def should_hit(self):
        return True


class PsychicPlayer(Player):

    def should_hit(self):
        # They can see what the dealer has
        dealer_score = self.game.dealer.curr_hand.cards[0].get_value()
        + self.game.dealer.curr_hand.cards[1].get_value()

        if self.curr_hand.score() > dealer_score and dealer_score > 16:
            return False
        elif self.curr_hand.score() < dealer_score and dealer_score < 16:
            return True
        else:
            return False


class LivePlayer(Player):

    def should_hit(self):
        print('You are showing: ' + str(self.curr_hand))
        if self.curr_hand.score() < 21:
            x = input('(H)it or (S)tay? ')
            return x.upper() == 'H'
        else:
            return False
