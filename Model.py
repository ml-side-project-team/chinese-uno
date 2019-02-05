import random

numDecks = 2
current_type = "singleCard"
numPlayers = 6

class Move:
    Types = ["Pass", "SingleCard"]

    def __init__(self, type, cards):
        self.type = type
        self.cards = cards

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

    def __lt__(self, other):
        return Card.Ranks.get(self.rank) < Card.Ranks.get(other.rank)

    # returns an ordered deck
    def new_deck(self):
        deck = []
        for deck in range(0, numDecks):
            for suit in Card.Suits:
                for rank in Card.Ranks:
                    deck.append(Card(suit, rank))
        return deck

    def is_illegal(self, current_card_rank, played_card_rank):
        # TODO return whether or not is legal play
        return True


class Player:
    def __init__(self):
        self.points = 0
        self.hand = []

    def add_points(self, points):
        self.points = points

    def set_hand(self, hand):
        self.hand = hand

    # returns a list of cards you want to play in order

    # this is to help modularity of ai players so we don't
    # have to requery them over and over for new plays if they
    # play something illegal
    # TODO
    def play(self, topCard):
        pass


def shuffle(deck):
    return random.shuffle(deck)


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


def playable_state(players):
    # TODO check to see if at least two players have cards left in their hands
    return True


def find_first_player():
    # TODO find players with 3 of hearts
    # TODO choose one at random
    # TODO make them play (remove card from their hand)
    pass

def play_round(players):
    players_in_round = players.size()
    current_card = Card("Hearts", "3")
    # find players with 3 of hearts and choose one
    find_first_player()
    # TODO re order list so next player is first
    while playable_state(players):
        # cycle through players
        for current_player in range(0, players_in_round):
            # each player play their card
            card_play_preference = players[current_player].play()
            # TODO check if illegal
            for i in range(0, card_play_preference):
                if Card.is_illegal(current_card, card_play_preference[i]):
                    # TODO dock points
                    pass
                else:
                    if(card_play_preference):
                        current_card = card_play_preference[i]


def play_match():
    players = []
    for i in range(0, numPlayers):
        players.append(Player())
    distribute_cards(players)
    while playable_state():
        play_round()
    # TODO assign points to winners
    return
