import random
from abc import ABC, abstractmethod


class Card:

	def __init__(self, value, suit):
		self.value = value
		self.suit = suit
		
		# Allows for cards to sort before counting values, so that Aces can be considered for 11 or 1.
		self.rank_order = 2 if value is 'A' else 1
		
	def __repr__(self):
		return self.value + ':' + self.suit
		
	def get_value(self, ace_is_low = False):
		if self.value.isdigit():
			return int(self.value)
		else:
			if self.value == 'A':
				if ace_is_low:
					return 1
				else:
					return 11
			elif self.value in ['J','Q','K']:
				return 10
				
		

class Deck:

	def __init__(self):
		self.cards = []
		for s in ['D','C','S','H']:
			for v in ['A','2','3','4','5','6','7','8','9','J','Q','K','A']:
				self.cards.append(Card(v,s))
		random.shuffle(self.cards)
				

class Game:
	
	def __init__(self, number_of_decks=8):
		self.cards = []
		self.players = {}
		self.dealer = Dealer()
				
		for i in range(1,number_of_decks+1):
			self.cards = self.cards + Deck().cards
			
	def draw(self):
		return self.cards.pop()
		
	def simulate(self):
		self._deal()
		
		for p in self.players.items():
			curr_player = p[1]
			while curr_player.should_hit():
				curr_player.add_card(self.draw())
				
		while self.dealer.should_hit():
			self.dealer.add_card(self.draw())
		
	def add_player(self, player):
		self.players[player.name] = player
		player.game = self
		
	def _deal(self):
		for i in range(1,3):
			for p in self.players.items():
				p[1].add_card(self.draw())
				
			self.dealer.add_card(self.draw())
						
	def __repr__(self):
		s = 'Dealer: ' + str(self.dealer.current_hand_value()) + ' ' + str(self.dealer.hand)
		for p in self.players.items():
			s += '\nPlayer ' + p[0] + ': ' + str(p[1].current_hand_value()) + ' ' + str(p[1].hand)
		return s
		
	def clear_hand(self):
		self.dealer.hand = []
		for p in self.players.items():
			p[1].hand = []
	
	def dealer_showing(self):
		""" Players cannot see the first card drawn to the dealer """
		return self.dealer.hand[1].get_value()

		
class Player(ABC):

	def __init__(self, name=''):
		self.hand = []
		self.name = name
		self.game = None
		
	def add_card(self, card):
		self.hand.append(card)
		
	def current_hand_value(self):
		# Have Aces go last; easier to account for 11 or 1 values
		sorted_cards = sorted(self.hand, key=lambda x: x.rank_order, reverse=False)
	
		value = 0
		for card in sorted_cards:
			new_value = value + card.get_value()
			if new_value > 21 and card.value == 'A':
				new_value = value + card.get_value(ace_is_low=True)
			value = new_value
		return value
	
	@abstractmethod
	def should_hit(self):
		pass
		
	def __repr__(self):
		return self.name


class Dealer(Player):

	def should_hit(self):
		return self.current_hand_value() <= 16
		

class BasicPlayer(Player):

	def should_hit(self):
		return self.current_hand_value() <= 10
		

class SmartPlayer(Player):
	def should_hit(self):
		if self.current_hand_value() >= 12 and self.game.dealer_showing() < 10:
			return False
		else:
			return True
				

if __name__ == '__main__':
	game = Game()
	game.add_player(BasicPlayer('A'))
	
	for i in range(1,11):
		print('Round ' + str(i))
		game.simulate()
		print(game)
		game.clear_hand()
		print('------------------------')
		print(len(game.cards))
	
	# game.players['A'].add_card(Card('A','D'))
	# game.players['A'].add_card(Card('Q','C'))
	# game.players['A'].add_card(Card('9','C'))



	
