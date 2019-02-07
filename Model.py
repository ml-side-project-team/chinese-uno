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

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        return Card.Ranks.get(self.rank) < Card.Ranks.get(other.rank)

    # returns an ordered deck
    @staticmethod
    def new_deck(self):
        deck = []
        for deck in range(0, numDecks):
            for suit in Card.Suits:
                for rank in Card.Ranks:
                    deck.append(Card(suit, rank))
        return deck

    @staticmethod
    def is_illegal(self, current_card, played_card):
        return not current_card < played_card


class Player:
    def __init__(self):
        self.points = 0
        self.hand = []

    def add_points(self, points):
        self.points = points

    def set_hand(self, hand):
        self.hand = hand

    def remove_card(self, card):
        self.hand.remove(card)

    def has_three_hearts(self):
        return Card("Hearts", "3") in self.hand

    # returns a list of cards you want to play in order

    # this is to help modularity of ai players so we don't
    # have to re-query them over and over for new plays if they
    # play something illegal
    # TODO
    def play(self, topCard):
        # should we check for illegal cards here?
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


def find_first_player(players):
    # find players with 3 of hearts
    competing_players = []
    for i in range(0, players.size()):
        if Player.has_three_hearts(players[i]):
            competing_players.append(i)
    # choose one at random
    first_player = competing_players[random.randrange(0, len(competing_players))]
    return first_player


# returns array with same order but player i up first
def set_first_player(players, i):
    if i > len(players):
        i = 0
    return players[i:] + players[:i]


def play_round(players):
    players_in_round = players.size()
    current_card = Card("Hearts", "3")
    # find players with 3 of hearts and choose one
    first_player = find_first_player()
    # make them play (remove card from their hand)
    players[first_player].removeCard(Card("Hearts", "3"))
    # set the player to be the second player (the first must play the 3 of hearts)
    players = set_first_player(players, first_player + 1)
    # TODO this should also check to see if everyone passed
    while playable_state(players):
        # cycle through players
        for current_player in range(0, players_in_round):
            # each player play their card
            card_play_preference = players[current_player].play()
            for i in range(0, card_play_preference):
                # check if illegal
                if Card.is_illegal(current_card, card_play_preference[i]):
                    # TODO dock points
                    pass
                else:
                    if card_play_preference:
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
