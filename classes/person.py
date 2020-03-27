import random

class Person:
    def __init__(self, name, cards_holding, value_sum, money):

        self.name = name
        self.value_sum = value_sum
        self.money = money
        self.cards_holding = cards_holding

    def dealer_first_turn_generator(self, cards):
        dealers_first_card = self.cardgenerator(cards)
        dealers_second_card = self.cardgenerator(cards)
        self.cards_holding = dealers_first_card["name"] + " - " + dealers_second_card["name"]
    #    self.value_sum = self.card_value_manager(dealers_first_card) + self.card_value_manager(dealers_second_card)
    #    self.value_sum = dealers_first_card["value"] + dealers_second_card["value"]
        if dealers_first_card["value"] == [1, 11]:
            self.value_sum = dealers_first_card["value"][1] + dealers_second_card["value"]
        elif dealers_second_card["value"] == [1, 11]:
            self.value_sum = dealers_first_card["value"] + dealers_second_card["value"][1]
        elif dealers_first_card["value"] ==[1, 11] and dealers_second_card["value"] == [1, 11]:
            self.value_sum = 21
        else:
            self.value_sum = dealers_first_card["value"] + dealers_second_card["value"]

    def player_first_turn_generator(self, cards):
        players_first_card = self.cardgenerator(cards)
        players_second_card = self.cardgenerator(cards)
        self.cards_holding = players_first_card["name"] + " - " + players_second_card["name"]
    #    self.value_sum = self.card_value_manager(players_first_card) + self.card_value_manager(players_second_card)
#        self.value_sum = players_first_card["value"] + players_second_card["value"]
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

    def cardgenerator(self, cards):

        i = random.randrange(0, len(cards))
        generated_card = cards[i]
        del cards[i]
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
