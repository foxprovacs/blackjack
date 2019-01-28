import unittest
import players
from blackjack import Card


class TestCardHands(unittest.TestCase):

    def test_1(self):
        d = players.Dealer()
        d.hand.add(Card('A', 'S'))
        d.hand.add(Card('10', 'S'))

        d.hand.cards[0].is_visible = False

        expected = 21
        actual = d.hand.score()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
