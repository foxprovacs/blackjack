import unittest
from context import cards, players


class TestCardHands(unittest.TestCase):

    def test_dealer_1(self):
        d = players.Dealer()
        d.curr_hand.add(cards.Card('A', 'S'))
        d.curr_hand.add(cards.Card('10', 'S'))

        d.curr_hand.cards[0].is_visible = False

        expected = 21
        actual = d.curr_hand.score()
        self.assertEqual(expected, actual)

    def test_dealer_2(self):
        d = players.Dealer()
        d.curr_hand.add(cards.Card('A', 'S'))
        d.curr_hand.add(cards.Card('6', 'S'))

        d.curr_hand.cards[0].is_visible = False

        expected = False
        actual = d.should_hit()
        self.assertEqual(expected, actual)

    def test_dealer_3(self):
        d = players.Dealer()
        d.curr_hand.add(cards.Card('A', 'S'))
        d.curr_hand.add(cards.Card('5', 'S'))

        d.curr_hand.cards[0].is_visible = False

        expected = True
        actual = d.should_hit()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
