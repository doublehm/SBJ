import random

class Person:
    def __init__(self, name, cards_holding, value_sum, points):

        self.name = name
        self.value_sum = value_sum
        self.points = points
        self.cards_holding = cards_holding

    def dealer_first_turn_generator(self, cards):
        dealers_first_card = self.cardgenerator(cards)
        dealers_second_card = self.cardgenerator(cards)
        self.cards_holding = dealers_first_card["name"] + " - " + dealers_second_card["name"]
        self.value_sum = dealers_first_card["value"] + dealers_second_card["value"]

    def player_first_turn_generator(self, cards):
        players_first_card = self.cardgenerator(cards)
        players_second_card = self.cardgenerator(cards)
        self.cards_holding = players_first_card["name"] + " - " + players_second_card["name"]
        self.value_sum = players_first_card["value"] + players_second_card["value"]
        print(self.name + " is holding", self.cards_holding)
        print(self.name, "cards value:", self.value_sum)

    def card_holding_manager(self, item):
        self.cards_holding += " - " + item["name"]
        print(self.name + " is holding", self.cards_holding)

    def cardgenerator(self, cards):

        i = random.randrange(1, len(cards) + 1)
        generated_card = cards[i]
        del cards[i]
        return generated_card

    def card_value_manager(self, item):
        self.value_sum += item["value"]
        print(self.name, "cards value:", self.value_sum)
