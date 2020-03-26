import random


class Cards:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    def shuffle_deck(self):
        i = 0
        cards = list(range(1, 53))
        while i < 52:

            for j in self.name:
                for k in self.kind:
                    x = {"name": str(j["name"]) + "-" + str(k), "value": j["value"]}
                    cards[i] = x
                    i += 1
        return cards
