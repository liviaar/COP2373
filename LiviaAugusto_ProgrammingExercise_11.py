# This game program deals a Poker hand of five cards, then the user selects
# what cards they want replaced. - Livia Augusto Razera, Assignment 11.

import random

#
class Card:
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    values = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
              'Jack', 'Queen', 'King']

    def __init__(self, value, suit):
        self.value = value  # 1-13
        self.suit = suit    # 0-3

    def __str__(self):
        return f'{Card.values[self.value]} of {Card.suits[self.suit]}'

    def __repr__(self):
        return self.__str__()

# Class that represents a deck.
class Deck:
    def __init__(self):
        self.cards = [Card(value, suit)
                      for suit in range(4)
                      for value in range(1, 14)]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

# Deals a hand from the deck
def deal_hand(deck, hand_size=5):
        return [deck.deal() for _ in range(hand_size)]

# Replaces the cards selected.
def replace_cards(hand, deck, indexes_to_replace):
    for index in indexes_to_replace:
        if 0 <= index < len(hand):
            hand[index] = deck.deal()
    return hand

# Shows the hand
def display_hand(hand):
    print("\nYour current hand:")
    for idx, card in enumerate(hand, start=1):
        print(f"{idx}: {card}")

# Main function
def main():
    deck = Deck()
    deck.shuffle()

    # Initial deal
    hand = deal_hand(deck)
    display_hand(hand)

    # Ask the user which cards to replace
    user_input = input("\nEnter the card numbers to replace, or press Enter to "
                       "keep all: ").strip()

    if user_input:
        try:
            indexes = [int(x) - 1 for x in user_input.split(',') if
                           x.strip().isdigit()]
            hand = replace_cards(hand, deck, indexes)
        except Exception as e:
            print("Invalid input. No cards were replaced.")

    display_hand(hand)
    print("\nGood luck with your hand!")

# Call out the main function.
if __name__ == "__main__":
    main()

