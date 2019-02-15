import unittest
import Model
import move_source
from move import Move


class DummySource(move_source.MoveSource):

    def __init__(self, name):
        self.name = name

    def play(self, hand, current_card) -> [Move]:
        move = hand[0]
        return [Move(Move.Type.SINGLE, [move])]


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

    def test_player_hand(self):
        dummy = DummySource("Dummy")
        player = Model.Player(dummy.name, dummy)
        player.hand = [Model.Card("Hearts", "4"), Model.Card("Diamonds", "5")]
        player.play(None)
        self.assertEqual(2, len(player.hand), "Player should not modify its own hand")

    def test_illegal_moves(self):
        dummy1 = DummySource("Dummy1")
        player1 = Model.Player(dummy1.name, dummy1)
        player1.hand = [Model.Card("Hearts", "4"), Model.Card("Diamonds", "5")]
        dummy2 = DummySource("Dummy2")
        player2 = Model.Player(dummy2.name, dummy2)
        player2.hand = [Model.Card("Hearts", "J"), Model.Card("Hearts", "Q")]
        results = Model.Game.run_game([player1, player2], current_card=Model.Card("Hearts", "10"))
        self.assertEqual(4, results[2][dummy1.name], "Player 1 should have made four illegal moves, two bad cards"
                                                     ", and two move sets with no valid moves")
        self.assertEqual(0, results[2][dummy2.name], "Player 2 should have no illegal moves")


if __name__ == "main":
    unittest.main()
