from abc import ABCMeta, abstractmethod
from move import Move


class MoveSource:
    __metaclass__ = ABCMeta

    def __init__(self, name):
        """
        Base initializer for a MoveSource
        :param name: The name of the move source
        """
        self.name = name

    @abstractmethod
    def play(self, hand, current_card) -> [Move]:
        """
        Returns a priority list of moves to make
        :param hand: The hand that the game has to play with
        :param current_card: The current card at the top of the deck
        :return: An ordered list of the moves that this source would like to play
        """
        pass


class ConsoleSource(MoveSource):

    def play(self, hand, current_card) -> [Move]:
        print("Current card:\t" + str(current_card) + "\nYour hand:")
        for i, card in enumerate(hand):
            print(str(i) + ". " + str(card))
        while True:
            entry = input("Please enter a move: ")
            if entry.isdigit():
                move = int(entry)
                if 0 <= move < len(hand):
                    return [Move(Move.Type.SINGLE, [hand[move]])]
            else:
                if entry in ("p", "pass"):
                    return [Move(Move.Type.PASS)]
            print("Invalid move. Please enter the index of the move you would like to play.")
