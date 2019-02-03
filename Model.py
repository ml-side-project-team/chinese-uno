class Card:
    Suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
    Ranks = {
        "3": 0,
        "4": 1,
        "5": 2,
        "6": 3,
        "7": 4,
        "8": 5,
        "9": 6,
        "10": 7,
        "J": 8,
        "Q": 9,
        "K": 10,
        "A": 11,
        "2": 12
    }

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


class Player:
    def __init__(self):
        self.points = 0
        self.hand = []

    def add_points(self, points):
        self.points = points

    def set_hand(self, hand):
        self.hand = hand

    def play(self):
        # return which card you want to play
        # should probably be handled by the controller
        return Card()


def shuffle():
    # randomly choose a deck
    deck = []
    return deck


def distribute_cards(players):
    deck = shuffle()
    player_num = 0
    player_hands = [[]]
    for i in range(0, deck.count()):
        player_hands[player_num].append(deck[i])
        player_num = player_num + 1
        if player_num == players.count():
            player_num = 0
    for j in range(0, players.count()):
        players[j].set_hand(player_hands[j])


def playable_state():
    # check to see if at least two players have cards left in their hands
    return True


def play_round():
    current_type = "singleCard"
    current_card_rank = -1
    # distribute the cards to players
    # find players with 3 of hearts and choose one
    # while people can play
        # cycle through players
            # each player play their card
            # assign points for different results (mostly illegal moves)


def game_loop():
    while playable_state():
        play_round()
    # assign points to winners
    return
