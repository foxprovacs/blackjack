import unittest
from blackjack_players import BasicPlayer
from blackjack import Card


class TestCardValues(unittest.TestCase):

	def test_1(self):
		p = BasicPlayer('Test Player')
		p.add_card(Card('1','D'))
		p.add_card(Card('2', 'D'))

		actual = p.current_hand_value()
		expected = 3

		self.assertEqual(actual, expected)

	def test_2(self):
		p = BasicPlayer('Test Player')
		p.add_card(Card('A','D'))
		p.add_card(Card('A', 'H'))
		p.add_card(Card('A', 'S'))
		p.add_card(Card('K', 'D'))

		actual = p.current_hand_value()
		expected = 13

		self.assertEqual(actual, expected)

if __name__ == '__main__':
	unittest.main()