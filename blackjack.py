import random
import blackjack_players


class Card:

	def __init__(self, value, suit):
		self.value = value
		self.suit = suit
		self.is_visible = True
		
		# Allows for cards to sort before counting values, so that Aces can be considered for 11 or 1.
		self.rank_order = 2 if value is 'A' else 1
		
	def __repr__(self, force_display=False):
		return (self.value + ':' + self.suit) if (self.is_visible and not force_display) else ''
		
	def get_value(self, ace_is_high = False):
		if self.value.isdigit():
			return int(self.value)
		else:
			if self.value == 'A':
				if ace_is_high:
					return 11
				else:
					return 1
			elif self.value in ['J','Q','K']:
				return 10
				
		
class Deck:

	def __init__(self):
		self.cards = []
		for s in ['D','C','S','H']:
			for v in ['A','2','3','4','5','6','7','8','9','J','Q','K','A']:
				self.cards.append(Card(v,s))
		random.shuffle(self.cards)
				

class CardHand:

	def __init__(self):
		self.cards = []

	def __repr__(self):
		s = ''
		for card in self.cards:
			s += str(card) + ' '
		return s

	def add(self, card):
		self.cards.append(card)

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



class Game:
	
	def __init__(self, number_of_decks=8):
		self.cards = []
		self.players = {}
		self.dealer = blackjack_players.Dealer()
				
		for i in range(1,number_of_decks+1):
			self.cards = self.cards + Deck().cards
			
	def draw(self):
		return self.cards.pop()
		
	def play(self):
		self._deal()
		
		print('Dealer is showing {}'.format(self.dealer.hand))
		
		for p in self.players.items():
			curr_player = p[1]
			print('Player ' + p[0] + ': ' + str(p[1].hand.score()) + ' ' + str(p[1].hand))
			while not curr_player.is_bust() and curr_player.should_hit():
				curr_player.hand.add(self.draw())
				print('Player ' + p[0] + ': ' + str(p[1].hand.score()) + ' ' + str(p[1].hand))
				
		while self.dealer.should_hit():
			self.dealer.hand.add(self.draw())
			
		for p in self.players.items():
			curr_player = p[1]
			if curr_player.is_bust():
				curr_player.is_winner = False
			elif curr_player.hand.score() > self.dealer.hand.score() and not self.dealer.is_bust():
				curr_player.is_winner = True
			elif self.dealer.is_bust() and not curr_player.is_bust():
				curr_player.is_winner = True
		
	def add_player(self, player):
		self.players[player.name] = player
		player.game = self
		
	def _deal(self):
		for i in range(1,3):
			for p in self.players.items():
				p[1].hand.add(self.draw())

			c = self.draw()
			if i == 1:
				c.is_visible = False
			self.dealer.hand.add(c)
						
	def __repr__(self):
		s = 'Dealer: ' + str(self.dealer.hand.score()) + ' ' + str(self.dealer.hand)
		for p in self.players.items():
			s += '\nPlayer ' + p[0] + ': ' + str(p[1].hand.score()) + ' ' + str(p[1].hand) + ' ' + 'Win=' + str(p[1].is_winner)
		return s
		
	def clear_hand(self):
		self.dealer.hand = []
		for p in self.players.items():
			p[1].hand = []
			p[1].is_winner = False
	
	def dealer_showing(self):
		""" Players cannot see the first card drawn to the dealer """
		return self.dealer.hand.cards[1].get_value()



	




	
