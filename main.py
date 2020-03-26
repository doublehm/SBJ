import random
from classes.person import Person


name = [{"name": "A", "value": [1, 11]}, {"name": "2", "value": 2}, {"name": "3", "value": 3}, {"name": "4", "value": 4}
        , {"name": "5", "value": 5}, {"name": "6", "value": 6}, {"name": "7", "value": 7}, {"name": "8", "value": 8}
        , {"name": "9", "value": 9}, {"name": "10", "value": 10}, {"name": "jack", "value": 10}
        , {"name": "queen", "value": 10}, {"name": "king", "value": 10}]
kind = ["Hearts", "Clubs", "Diamonds", "Spades"]
i = 0
cards = list(range(1, 53))
while i < 52:

    for j in name:
        for k in kind:
            x = {"name": str(j["name"]) + "-" + str(k), "value": j["value"]}
            cards[i] = x
            i += 1


def cardgenerator(cards):

    i = random.randrange(1, len(cards) + 1)
    generated_card = cards[i]
    del cards[i]
    return generated_card


player = Person("", 0, 0)
dealer = Person("", 0, 0)

print("this is the game of blackjack")
wanna_play = input("do you wanna proceed? (y/n): ")
running = True

cards_value = 0

while running:
    dealer.value_sum = 0
    dealer.cards_holding = ''
    player.value_sum = 0
    player.cards_holding = ''
    dealers_turn = False
    if wanna_play == "y":
        print("great lets start")

        random_card = cardgenerator(cards)
        print("cards count: " + str(len(cards)))
        dealer.cards_holding += random_card["name"]
        dealer.value_sum += random_card["value"]

        random_card = cardgenerator(cards)
        print("cards count: " + str(len(cards)))
        dealer.cards_holding += random_card["name"]
        dealer.value_sum += random_card["value"]

        random_card = cardgenerator(cards)
        print("cards count: " + str(len(cards)))
        player.cards_holding += random_card["name"]
        player.value_sum += random_card["value"]

        random_card = cardgenerator(cards)
        print("cards count: " + str(len(cards)))
        player.cards_holding += random_card["name"]
        player.value_sum += random_card["value"]
        print("your card is: " + player.cards_holding)

        print("player's hand value: ", str(player.value_sum))

        x = input("you want another card? (y/n): ")
        if x == "n":
            dealers_turn = True
        player_card_pick2 = ''
        if x == "y":
            while not dealers_turn:

                player_extra_card = cardgenerator(cards)
                print("cards count: " + str(len(cards)))
                print("your last card is: " + player_extra_card['name'])
                player.value_sum += player_extra_card["value"]
                print("your hands value is:", player.value_sum)
                if player.value_sum > 21:
                    print("you lost")
                    break
                elif player.value_sum == 21:
                    print("wow! you won!")
                    break
                else:
                    x = input("you want an extra card? (y/n): ")
                    if x == "n":
                        dealers_turn = True

        while dealers_turn:
            print("dealers cards are: " + dealer.cards_holding)

            if player.value_sum < dealer.value_sum < 21:
                print("dealer won! you lost")
                break
            elif dealer.value_sum > 21:
                print("dealer lost! you won")
                break

            while dealer.value_sum <= player.value_sum:

                dealers_card_extra = cardgenerator(cards)
                print("cards count: " + str(len(cards)))
                dealer.value_sum += dealers_card_extra["value"]
                dealer.cards_holding += dealers_card_extra["name"]
                print("dealers cards: " + dealer.cards_holding)
                print("dealers card value: " + str(dealer.value_sum))

                if 21 > dealer.value_sum > player.value_sum:
                    print("dealer won!")
                    break
                if dealer.value_sum > 21:
                    print("you won")

    elif wanna_play == "n":
        print("exiting game")
        break