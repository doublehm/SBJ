import random
from classes.cards import Cards


class Person:
    def __init__(self, name, cards_holding, value_sum, money):

        self.name = name
        self.value_sum = value_sum
        self.money = money
        self.cards_holding = cards_holding

    def dealer_first_turn_generator(self, cards, running, name, kind):
        dealers_first_card = self.cardgenerator(cards, running, name, kind)
        dealers_second_card = self.cardgenerator(cards, running, name, kind)

        self.cards_holding = dealers_first_card["name"] + " - " + dealers_second_card["name"]

        if dealers_first_card["value"] == [1, 11]:
            self.value_sum = dealers_first_card["value"][1] + dealers_second_card["value"]

        elif dealers_second_card["value"] == [1, 11]:
            self.value_sum = dealers_first_card["value"] + dealers_second_card["value"][1]

        elif dealers_first_card["value"] ==[1, 11] and dealers_second_card["value"] == [1, 11]:
            self.value_sum = 21

        else:
            self.value_sum = dealers_first_card["value"] + dealers_second_card["value"]

    def player_first_turn_generator(self, cards, running, name, kind):

        players_first_card = self.cardgenerator(cards, running, name, kind)
        players_second_card = self.cardgenerator(cards, running, name, kind)

        self.cards_holding = players_first_card["name"] + " - " + players_second_card["name"]

        if players_first_card["value"] == [1, 11]:
            self.value_sum = players_first_card["value"][1] + players_second_card["value"]

        elif players_second_card["value"] == [1, 11]:
            self.value_sum = players_first_card["value"] + players_second_card["value"][1]

        elif players_first_card["value"] ==[1, 11] and players_second_card["value"] == [1, 11]:
            self.value_sum = 21

        else:
            self.value_sum = players_first_card["value"] + players_second_card["value"]

        print(self.name + " is holding", self.cards_holding)
        print(self.name, "cards value:", self.value_sum)

    def card_holding_manager(self, item):
        self.cards_holding += " - " + item["name"]
        print(self.name + " is holding", self.cards_holding)

    def cardgenerator(self, cards, running, name, kind):

        i = random.randrange(0, len(cards))
        generated_card = cards[i]
        del cards[i]
        if len(cards) == 0:
            x = input("no card left, do you wanna continue? (y/n) ")
            if x == "y":
                cards = Cards(name, kind).shuffle_deck()
                #self.cardgenerator(cards, running, name, kind)
                return cards
            else:
                cards = Cards(name, kind).shuffle_deck()
                running = False
                return running, cards

        return generated_card

    def card_value_manager(self, item):
        if item["value"] == [1, 11]:

            if self.value_sum <11:
                self.value_sum += item["value"][1]
                print(self.name, "cards value:", self.value_sum)

            else:
                self.value_sum += item["value"][0]
                print(self.name, "cards value:", self.value_sum)

        else:
            self.value_sum += item["value"]
            print(self.name, "cards value:", self.value_sum)
