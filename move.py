from enum import Enum, auto


class Move:
    class Type(Enum):
        PASS = auto()
        SINGLE = auto()

    def __init__(self, move_type, cards=[]):
        self.move_type = move_type
        self.cards = cards

    def is_legal(self, hand, current_card) -> bool:
        if self.move_type == Move.Type.PASS:
            return True
        elif self.move_type == Move.Type.SINGLE:
            if self.cards[0] in hand:
                if current_card is not None:
                    return current_card < self.cards[0]
                else:
                    return True
            else:
                return False
