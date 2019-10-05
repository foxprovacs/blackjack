import unittest
from context import cards


class TestCardValues(unittest.TestCase):

	def test_hand_value_1(self):
		hand = cards.CardHand()
		hand.add(cards.Card('1','D'))
		hand.add(cards.Card('2', 'D'))

		actual = hand.score()
		expected = 3

		self.assertEqual(actual, expected)
		
	def test_hand_value_2(self):
		hand = cards.CardHand()
		hand.add(cards.Card('K','D'))
		hand.add(cards.Card('A', 'D'))

		actual = hand.score()
		expected = 21
		self.assertEqual(actual, expected)

	def test_hand_value_3(self):
		hand = cards.CardHand()
		hand.add(cards.Card('A','D'))
		hand.add(cards.Card('A', 'H'))
		hand.add(cards.Card('A', 'S'))
		hand.add(cards.Card('K', 'D'))

		actual = hand.score()
		expected = 13
		self.assertEqual(actual, expected)

	def test_hand_value_4(self):
		hand = cards.CardHand()
		hand.add(cards.Card('9','D'))
		hand.add(cards.Card('A', 'H'))
		hand.add(cards.Card('A', 'S'))
		hand.add(cards.Card('K', 'D'))

		actual = hand.score()
		expected = 21
		self.assertEqual(actual, expected)

	def test_deck_1(self):
		deck = cards.Deck()
		actual = len(deck.cards)
		expected = 52
		self.assertEqual(actual, expected)

	def test_deck_2(self):
		deck = cards.Deck(shuffle=False)
		cards_drawn = {}

		for c in deck.cards:
			key = str(c)
			if key not in cards_drawn:
				cards_drawn[key] = 1
			else:
				cards_drawn[key] = cards_drawn[key] + 1

		max_key_count = max(cards_drawn.values())
		self.assertEqual(max_key_count, 1)

	def test_shoe_1(self):
		number_of_decks = 5
		shoe = cards.Shoe(number_of_decks)
		actual = len(shoe.cards)
		expected = number_of_decks * 52
		self.assertEqual(actual, expected)

	def test_shoe_2(self):
		shoe = cards.Shoe()
		hand = cards.CardHand()

		hand.add(shoe.draw())
		hand.add(shoe.draw())

		actual = hand.score()
		self.assertGreater(actual, 0)

	def test_shoe_3(self):
		number_of_decks = 8
		shoe = cards.Shoe(number_of_decks)
		cards_drawn = {}

		while (len(shoe.cards) > 0):
			c = shoe.draw()
			key = str(c)
			if key not in cards_drawn:
				cards_drawn[key] = 1
			else:
				cards_drawn[key] = cards_drawn[key] + 1

		max_key_count = max(cards_drawn.values())
		self.assertEqual(max_key_count, 1 * number_of_decks)

	def test_shoe_4(self):
		shoe = cards.Shoe()
		is_face_up = True
		card = shoe.draw()
		
		actual = card.is_visible
		self.assertEqual(actual, is_face_up)

	def test_shoe_5(self):
		shoe = cards.Shoe()
		is_face_up = False
		card = shoe.draw(is_face_down=True)
		
		actual = card.is_visible
		self.assertEqual(actual, is_face_up)


if __name__ == '__main__':
	unittest.main()