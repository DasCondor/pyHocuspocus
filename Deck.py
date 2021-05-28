
import random


class Card(object):

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return self.show_card()

    def __repr__(self):
        return self.show_card()

    def show_card(self):
        return "{} of {}".format(self.value, self.suit)


class Deck(object):
    suits = {  # keys are unicode symbols for suits
        u'\u2660': "black",
        u'\u2665': "red",
        u'\u2663': "black",
        u'\u2666': "red",
    }
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]

    def __init__(self):
        self.deck = []
        # Directly with the creation of the object it will build and shuffle the deck
        self.build_deck()
        self.shuffle_cards()

    def build_deck(self):
        for suit in self.suits:
            for value in self.values:
                # Using the Card class to create all the cards and append it to the self.cards[] instance variable
                self.deck.append(Card(value, suit))

    def shuffle_cards(self):
        # Using the random.shuffle method to the self.cards list
        return random.shuffle(self.deck)

    def show_deck(self):
        for card in self.deck:
            # Using the Card class method show_card to show each card in the deck
            print(card.show_card())

    def empty_deck(self):
        self.deck = []
        

    def draw_card(self):
        # It will draw the last (random) card in the deck and will remove it from self.cards list
        return self.deck.pop()
