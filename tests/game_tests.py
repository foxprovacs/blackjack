import unittest
import players
from blackjack import Game, Card


class TestGame(unittest.TestCase):

    def test_1(self):
        """ Dealer has blackjack """
        game = Game()

        player = players.BasicPlayer()
        game.add_player(player)

        game.dealer.hand.add(Card('A', 'S'))
        game.dealer.hand.add(Card('10', 'H'))

        player.hand.add(Card('10', 'S'))
        player.hand.add(Card('10', 'C'))
        player.hand.add(Card('A', 'C'))

        game.play(show_output=False)

        expected = False
        actual = player.is_winner

        # print('Player is_winner = {0}'.format(player.is_winner))

        self.assertEqual(expected, actual)

    def test_2(self):
        """ Player has blackjack """
        game = Game()

        player = players.BasicPlayer()
        game.add_player(player)

        game.dealer.hand.add(Card('10', 'S'))
        game.dealer.hand.add(Card('10', 'H'))

        player.hand.add(Card('10', 'S'))
        player.hand.add(Card('A', 'C'))

        game.play(show_output=False)

        expected = True
        actual = player.is_winner

        # print('Player is_winner = {0}'.format(player.is_winner))

        self.assertEqual(expected, actual)

    def test_cards_drawn(self):
        """ Verify the game.cards_drawn variable is being set properly """
        game = Game()
        player = players.BasicPlayer()
        game.add_player(player)

        cards = []
        for i in range(1, 101):
            card = game.draw()
            cards.append(card)

        sum_x = sum([c.get_value() for c in cards])
        sum_y = sum([c.get_value() for c in game.cards_drawn])

        self.assertEqual(sum_x, sum_y)


if __name__ == '__main__':
    unittest.main()
