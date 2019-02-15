from abc import ABCMeta, abstractmethod
from move import Move


class MoveSource:
    __metaclass__ = ABCMeta

    # Return a priority list of moves to make
    @abstractmethod
    def play(self, hand, current_card) -> [Move]:
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