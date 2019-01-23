from abc import ABC, abstractmethod


class Player(ABC):

	def __init__(self, name=''):
		self.hand = []
		self.name = name
		self.game = None
		self.is_winner = False
		
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
		
	def is_bust(self):
		return self.current_hand_value() > 21
	
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
			

class RealPlayer(Player):

	def should_hit(self):
		if self.current_hand_value() < 21:
			x = input('(H)it or (S)tay? ')
			return x.upper() == 'H'
		else:
			return False