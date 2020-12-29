from abc import ABC, abstractmethod
import blackjack.cards as cards
from enum import Enum


class GameStatus(Enum):
    Win = 1
    NotPlayed = 0
    Draw = 2
    Loss = 3


class Player(ABC):
    """ An abstract class representing a generic player or the dealer. """

    def __init__(self, name=''):
        self.curr_hand = cards.CardHand()
        self.name = name
        self.game = None
        self.game_flag = GameStatus.NotPlayed
        self.wins = 0
        self.losses = 0
        self.draws = 0

    def clear(self):
        self.curr_hand = cards.CardHand()
        self.game_flag = GameStatus.NotPlayed

    @abstractmethod
    def should_hit(self):
        """ The primary method definining each player strategy. """
        pass

    def __repr__(self):
        return self.name


class Dealer(Player):

    def __init__(self):
        super(Dealer, self).__init__('Dealer')

    def should_hit(self):
        return self.curr_hand.score() <= 16

    def showing(self):
        return self.curr_hand.cards[1].get_value()


class BasicPlayer(Player):

    def should_hit(self):
        return self.curr_hand.score() <= 16


class SmartPlayer(Player):

    def should_hit(self):
        dealer_score = self.game.dealer.showing()
        my_score = self.curr_hand.score()
        if dealer_score <= 12 and my_score <= 11:
            return True
        elif dealer_score <= 16 and my_score <= 15:
            return True
        else:
            return False


class PyschicPlayer(Player):

    def should_hit(self):
        dealer_score = self.game.dealer.curr_hand.score()
        my_score = self.curr_hand.score()
        next_card = self.game.shoe.peek()
        if (dealer_score > my_score) and (my_score + next_card <= 21):
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
