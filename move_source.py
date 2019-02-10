from abc import ABCMeta, abstractmethod


class MoveSource:
    __metaclass__ = ABCMeta

    # Return a priority list of moves to make
    @abstractmethod
    def play(self, hand, current_card):
        pass


class ConsoleSource(MoveSource):

    def play(self, hand, current_card):
        print("Current card:\t" + str(current_card) + "\nYour hand:")
        for i, card in enumerate(hand):
            print(str(i) + ". " + str(card))
        while True:
            move = int(input("Please enter a move: "))
            print(move)
            if 0 <= move < len(hand):
                print(hand[move])
                return [hand[move]]
            else:
                print("Invalid move. Please enter the index of the move you would like to play.")
