import random
from classes.person import Person
from classes.cards import Cards


name = [{"name": "A", "value": [1, 11]}, {"name": "2", "value": 2}, {"name": "3", "value": 3}, {"name": "4", "value": 4}
        , {"name": "5", "value": 5}, {"name": "6", "value": 6}, {"name": "7", "value": 7}, {"name": "8", "value": 8}
        , {"name": "9", "value": 9}, {"name": "10", "value": 10}, {"name": "jack", "value": 10}
        , {"name": "queen", "value": 10}, {"name": "king", "value": 10}]
kind = ["Hearts", "Clubs", "Diamonds", "Spades"]

# cards = list(range(1, 53))
cards = Cards(name, kind).shuffle_deck()


player = Person("player", "", 0, 0)
dealer = Person("dealer", "", 0, 0)

print("this is the game of blackjack")
wanna_play = input("do you wanna proceed? (y/n): ")
player.money = int(input("players credit: (ex. 500$ = 500) "))
dealer.money = int(input("bank's credit: "))

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

        dealer.dealer_first_turn_generator(cards)
        player.player_first_turn_generator(cards)
        print("cards count: " + str(len(cards)))

        bet = int(input("place your bet: "))
        player.money -= bet

        x = input("you want another card? (y/n): ")
        if x == "n":
            dealers_turn = True
        player_card_pick2 = ''
        if x == "y":

            while not dealers_turn:

                player_extra_card = player.cardgenerator(cards)
                print("cards count: " + str(len(cards)))
                player.card_holding_manager(player_extra_card)
                player.card_value_manager(player_extra_card)
                if player.value_sum > 21:
                    dealer.money += bet
                    print("you lost", "balance: player(" + str(player.money) + ") bank(" + str(dealer.money) + ")")
                    break
                elif player.value_sum == 21:
                    player.money += (2 * bet)
                    dealer.money -= bet
                    print("wow! you won!", "balance: player(" + str(player.money) + ") bank(" + str(dealer.money) + ")")
                    break
                else:
                    x = input("you want an extra card? (y/n): ")
                    if x == "n":
                        dealers_turn = True

        while dealers_turn:
            print("dealers cards are: " + dealer.cards_holding)

            if player.value_sum < dealer.value_sum < 21:
                dealer.money += bet
                print("dealer won! you lost", "balance: player(" + str(player.money) + ") bank(" + str(dealer.money) + ")")
                break

            elif player.value_sum > 21:
                player.money += (2 * bet)
                dealer.money -= bet
                print("you won!!", "balance: player(" + str(player.money) + ") bank(" + str(dealer.money) + ")")
                break

            while dealer.value_sum <= player.value_sum:

                dealers_card_extra = dealer.cardgenerator(cards)
                print("cards count: " + str(len(cards)))
                dealer.card_holding_manager(dealers_card_extra)
                dealer.card_value_manager(dealers_card_extra)

                if 21 > dealer.value_sum > player.value_sum:
                    dealer.money += bet
                    print("dealer won!", "balance: player(" + str(player.money) + ") bank(" + str(dealer.money) + ")")
                    break

                elif dealer.value_sum == 21:
                    dealer.money += bet
                    print("dealer won!", "balance: player(" + str(player.money) + ") bank(" + str(dealer.money) + ")")
                    break

                elif dealer.value_sum > 21:
                    player.money += (2 * bet)
                    dealer.money -= bet
                    print("you won!!", "balance: player(" + str(player.money) + ") bank(" + str(dealer.money) + ")")
            break
    elif wanna_play == "n":
        print("exiting game")
        break
