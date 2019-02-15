import move_source
import random
from move import Move


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
    def play(self, top_card) -> [Move]:
        return self.source.play(self.hand, top_card)


class Game:

    @staticmethod
    def simulate_game(players):
        """
        Sets up and runs a game by copying the given players and then shuffling decks using the default behavior
        :param players: The players to use in the game
        :return: The results of the game
        """
        # Make a copy of the list of players
        players_copy = players.copy()
        # Deal the players cards
        Game.distribute_cards(players_copy)

        # Get the index of the player who will play first and remove the three of hearts from their hand
        current_player = Game.set_up_first_player(players_copy)
        return Game.run_game(players_copy, current_player)

    @staticmethod
    def run_game(players, current_player=0, current_card=Card("Hearts", "3")):
        """
        Runs a game with the given initial conditions
        :param players: The players to use in this game. This will be modified
        :param current_player: The index of the starting player
        :param current_card: The current card at the top of the stack
        :return: The the placement of each player, the total number of moves made in the game (including passes),
            the number of illegal moves that each player made
        """
        scoreboard = []
        moves = 0
        consecutive_passes = 0
        illegal_moves = {player.name: 0 for player in players}
        while len(players) > 0:
            while current_player < len(players):
                # If the game has passed all the way around
                if consecutive_passes >= len(players) - 1:
                    current_card = None
                # Get move preference from the player
                card_play_preference = players[current_player].play(current_card)
                # Translate the preference into a move
                move, illegals = Game.move_from_preference(card_play_preference, players[current_player].hand, current_card)
                illegal_moves[players[current_player].name] += illegals
                if move.move_type == Move.Type.PASS:
                    consecutive_passes += 1
                    current_player += 1
                elif move.move_type == Move.Type.SINGLE:
                    players[current_player].remove_card(move.cards[0])
                    current_card = move.cards[0]
                    consecutive_passes = 0
                    if len(players[current_player].hand) == 0:
                        scoreboard.append(players[current_player])
                        del players[current_player]
                    else:
                        current_player += 1
                moves += 1
                if len(players) > 0:
                    current_player %= len(players)
        return scoreboard, moves, illegal_moves

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
    def move_from_preference(card_play_preference, hand, current_card) -> (Move, int):
        """
        Generates a move from a list of card preferences
        :param card_play_preference: The list of cards
        :param hand: The hand of the player making the move
        :param current_card: The current card at the top of the stack
        :return: The move to make and the number of illegal moves that preceded the returned move in the preference
            list
        """
        illegals = 0
        for move in card_play_preference:
            if move.move_type == Move.Type.PASS:
                return move, illegals
            elif move.move_type == Move.Type.SINGLE:
                if move.is_legal(hand, current_card):
                    return move, illegals
                else:
                    illegals += 1
                    continue
        illegals += 1
        return Move(Move.Type.PASS), illegals


def play_match(num_players=6):
    players = []
    for i in range(0, num_players):
        players.append(Player("Player: " + str(i), move_source.ConsoleSource()))
    game = Game(players)
    game.play_round()
    # TODO assign points to winners
    return
