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

        game.play()

        expected = False
        actual = player.is_winner

        print('Player is_winner = {0}'.format(player.is_winner))

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

        game.play()

        expected = True
        actual = player.is_winner

        print('Player is_winner = {0}'.format(player.is_winner))

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
