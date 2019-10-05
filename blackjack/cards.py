import random


class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.is_visible = True

        # Allows for cards to sort before counting values, so that Aces can be considered for 11 or 1.
        self.rank_order = 2 if value is 'A' else 1

    def __repr__(self, force_display=False):
        return self.value if (self.is_visible and not force_display) else '_'

    def __str__(self):
        if self.is_visible:
            s = '({0}:{1})'.format(self.value,self.suit)
        else:
            s = '({0}:{1})'.format('?','?')
        return s

    def get_value(self, ace_is_high=False):
        if self.value.isdigit():
            return int(self.value)
        else:
            if self.value == 'A':
                if ace_is_high:
                    return 11
                else:
                    return 1
            elif self.value in ['J', 'Q', 'K']:
                return 10

class Deck:

    def __init__(self, shuffle=True):
        self.cards = []
        self.reset(shuffle)

    def reset(self, shuffle=True):
        for s in ['D', 'C', 'S', 'H']:
            for v in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                self.cards.append(Card(v, s))
        if shuffle:
            random.shuffle(self.cards)


class Shoe:

    def __init__(self, number_of_decks=8):
        self.cards = []
        self.number_of_decks = number_of_decks

        # Tracks the cards drawn; used for player strategies that involve some
        # level of card counting.
        self.cards_drawn = []

        self.reset()

    def reset(self):
        self.cards = []
        for i in range(1, self.number_of_decks + 1):
            self.cards = self.cards + Deck().cards

    def draw(self, is_face_down=False):
        if len(self.cards) == 0:
            self.reset()
        card = self.cards.pop()
        if is_face_down:
            card.is_visible = False
        self.cards_drawn.append(card)
        return card


class CardHand:

    def __init__(self):
        self.cards = []

        # Will be set to true if player has a natural blackjack, i.e. a 21 on first 2 cards.
        self.is_blackjack = False

    def __repr__(self):
        s = ''
        for card in self.cards:
            s += str(card) + ' '
        return s

    def __str__(self):
        s = ''
        for card in self.cards:
            s += str(card) + ' '
        return s

    def add(self, card):
        self.cards.append(card)

    def clear(self):
        self.cards = []
        self.is_blackjack = False

    def score(self):
        """Calculate the value of the hand

        Aces can count as 1 or 11, but in the case of holding multiple Aces only one can
        count as 11. To account for this, cards are sorted first with Aces last. All Aces
        will count as 1 by default. If the last card is an Ace, and the current hand value
        is 10 or less, then that Ace will count as 11
        """

        # Have Aces go last; easier to account for 11 or 1 values
        sorted_cards = sorted(self.cards, key=lambda x: x.rank_order, reverse=False)

        last_card_in_hand = sorted_cards[-1]

        curr_value = 0
        for card in sorted_cards:
            curr_value += card.get_value(ace_is_high=(card == last_card_in_hand))

        if last_card_in_hand.value == 'A' and curr_value > 21:
            curr_value -= 10

        return curr_value