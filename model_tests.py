import unittest
import Model
import move_source


class DummySource(move_source.MoveSource):

    def __init__(self, name):
        self.name = name

    def play(self, hand, current_card):
        move = hand[0]
        print(self.name + " requested: " + str(move))
        return [move]


class TestGame(unittest.TestCase):

    def test_simple(self):
        dummy1 = DummySource("Player 1")
        player1 = Model.Player(dummy1.name, dummy1)
        player1.hand = [Model.Card("Hearts", "4"), Model.Card("Diamonds", "5")]
        dummy2 = DummySource("Player 2")
        player2 = Model.Player(dummy2.name, dummy2)
        player2.hand = [Model.Card("Spades", "7")]
        players = [player1, player2]
        results = Model.Game.run_game(players)
        self.assertListEqual([player2, player1], results[0], "Player 2 should win and player 1 should come second")
        self.assertEqual(3, results[1], "The game should have three moves because there are 3 cards")


if __name__ == "main":
    unittest.main()
