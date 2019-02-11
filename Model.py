import random
import move_source

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

    def __str__(self):
        return str(self.rank) + " of " + str(self.suit)

    # returns an ordered deck
    @staticmethod
    def new_deck(num_decks=2):
        deck = []
        for _ in range(0, num_decks):
            for suit in Card.Suits:
                for rank in Card.Ranks:
                    deck.append(Card(suit, rank))
        return deck

    @staticmethod
    def is_illegal(current_card, played_card):
        if current_card is None:
            return False
        else:
            return not current_card < played_card


class Player:
    def __init__(self, name, source):
        self.points = 0
        self.hand = []
        self.name = name
        self.source = source

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
    def play(self, top_card):
        return self.source.play(self.hand, top_card)


class Game:
    def __init__(self, players):
        self.players = players
        self.scoreboard = []

    def play_round(self):
        # Make a copy of the list of players
        players_copy = self.players.copy()
        # Deal the players cards
        self.distribute_cards(players_copy)

        # Get the index of the player who will play first and remove the three of hearts from their hand
        current_player = self.set_up_first_player(players_copy)
        self.run_game(players_copy, current_player)

    def run_game(self, players, current_player=0, current_card=Card("Hearts", "3")):
        consecutive_passes = 0
        while len(players) > 1:
            while current_player < len(players):
                # If the game has passed all the way around
                if consecutive_passes >= len(players) - 1:
                    current_card = None
                print(players[current_player].name + "'s Turn:")
                # Get move preference from the player
                card_play_preference = players[current_player].play(current_card)
                # Translate the preference into a move
                move = self.move_from_preference(card_play_preference, current_card)
                if move is None:
                    print(players[current_player].name + " Passed")
                    consecutive_passes += 1
                    current_player += 1
                else:
                    players[current_player].remove_card(move)
                    current_card = move
                    consecutive_passes = 0
                    # If the player has no cards left after they make the move
                    if len(players[current_player].hand) == 0:
                        self.scoreboard.append(players[current_player])
                        del players[current_player]
                    else:
                        current_player += 1
                current_player %= len(players)

    @staticmethod
    def shuffle(deck):
        random.shuffle(deck)

    @staticmethod
    def distribute_cards(players):
        deck = Card.new_deck()
        Game.shuffle(deck)
        player_num = 0
        player_hands = [[] for _ in range(0, len(players))]
        for i in range(0, len(deck)):
            player_hands[player_num].append(deck[i])
            player_num = player_num + 1
            if player_num == len(players):
                player_num = 0
        for j in range(0, len(players)):
            players[j].set_hand(player_hands[j])

    @staticmethod
    def set_up_first_player(players) -> int:
        """
        Finds all the players with the three of hearts and then picks a random one to be the first player.
        :param players: The players from which the first will be determined
        :return: The index of the first player

        """
        # find players with 3 of hearts
        competing_players = []
        for i in range(0, len(players)):
            if Player.has_three_hearts(players[i]):
                competing_players.append(i)
        # choose one at random
        first_player = competing_players[random.randrange(0, len(competing_players))]
        players[first_player].remove_card(Card("Hearts", "3"))
        return first_player

    @staticmethod
    def move_from_preference(card_play_preference, current_card):
        """
        Generates a move from a list of card preferences
        :param card_play_preference: The list of cards
        :param current_card: The current card at the top of the stack
        :return: The card to play or None if the player is passing
        """
        if card_play_preference is None:
            return None
        for i in range(0, len(card_play_preference)):
            # check if illegal
            if Card.is_illegal(current_card, card_play_preference[i]):
                # TODO dock points
                return None
            else:
                return card_play_preference[i]
        return None


def play_match(num_players=6):
    players = []
    for i in range(0, num_players):
        players.append(Player("Player: " + str(i), move_source.ConsoleSource()))
    game = Game(players)
    game.play_round()
    # TODO assign points to winners
    return


play_match()
