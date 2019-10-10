import unittest
from context import games, players


class GameTestCase(unittest.TestCase):

    def setUp(self):
        self.game = games.Game()
        self.game.add_player(players.BasicPlayer('Player 1'))
        self.game.add_player(players.BasicPlayer('Player 2'))
        self.game.add_player(players.BasicPlayer('Player 3'))

    def test_game_1(self):
        actual = len(self.game.players)
        self.assertTrue(actual > 0)

    def test_game_2(self):
        # After draw, dealer has one card face down
        self.game.deal()
        actual = self.game.dealer.curr_hand.cards[0].is_visible
        expected = False
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
