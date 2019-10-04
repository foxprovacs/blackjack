import unittest
#from blackjack import Card, CardHand
from context import cards.Card, cards.CardHand


class TestCardHands(unittest.TestCase):

    def test_1(self):
        hand = CardHand()
        hand.add(Card('1','D'))
        hand.add(Card('2', 'D'))

        actual = hand.score()
        expected = 3
        self.assertEqual(actual, expected)

    def test_2(self):
        hand = CardHand()
        hand.add(Card('A','D'))
        hand.add(Card('J', 'D'))

        actual = hand.score()
        expected = 21
        self.assertEqual(actual, expected)

    def test_3(self):
        hand = CardHand()
        hand.add(Card('J','D'))
        hand.add(Card('A', 'D'))

        actual = hand.score()
        expected = 21
        self.assertEqual(actual, expected)

    def test_4(self):
        hand = CardHand()
        hand.add(Card('A','D'))
        hand.add(Card('A', 'D'))
        hand.add(Card('A', 'D'))

        actual = hand.score()
        expected = 13
        self.assertEqual(actual, expected)

    def test_5(self):
        hand = CardHand()
        hand.add(Card('A','D'))
        hand.add(Card('A', 'D'))
        hand.add(Card('A', 'D'))
        hand.add(Card('A', 'D'))

        actual = hand.score()
        expected = 14
        self.assertEqual(actual, expected)

    def test_6(self):
        hand = CardHand()
        hand.add(Card('A','D'))
        hand.add(Card('A', 'D'))
        hand.add(Card('J', 'D'))

        actual = hand.score()
        expected = 12
        self.assertEqual(actual, expected)

    def test_7(self):
        hand = CardHand()
        hand.add(Card('7','D'))
        hand.add(Card('K', 'D'))

        actual = hand.score()
        expected = 17
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()