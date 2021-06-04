############### The Game Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
#todo 1: Go to this website and try out the Blackjack game: https://games.washingtonpost.com/games/blackjack/

#todo 2: Create flowchart

#todo 3 : create list of the card numbers
logo ='''
   (   (                )                       )  
 ( )\  )\    )       ( /(     (      )       ( /(  
 )((_)((_)( /(   (   )\())    )\  ( /(   (   )\()) 
((_)_  _  )(_))  )\ ((_)\    ((_) )(_))  )\ ((_)\  
 | _ )| |((_)_  ((_)| |(_)  _ | |((_)_  ((_)| |(_) 
 | _ \| |/ _` |/ _| | / /  | || |/ _` |/ _| | / /  
 |___/|_|\__,_|\__| |_\_\   \__/ \__,_|\__| |_\_\  
'''


import random
import os


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(array):

    score = sum(array)

    if score == 21:
        return 0
    elif score > 21:
        if 11 in array:
            array.remove(11)
            array.append(1)
            score = sum(array)

    return score


def compare(player_value, computer_value):
    if player_value > 21 and computer_value > 21:
        return f"\nYou lost with a score of {player_value}"

    if player_value == computer_value:
        return f"\nIts a tie, you both had {player_value}."
    elif computer_value == 0:
        return "\nYou lost, computer has a blackjack."
    elif player_value == 0:
        return "\nYou won, you got a blackjack."
    elif player_value > 21:
        return f"\nYou lost with a score of {player_value} compared to {computer_value}."
    elif computer_value > 21:
        return f"\nYou won with a score of {player_value} compared to {computer_value}"
    elif player_value > computer_value:
        return f"\nYou won with a score of {player_value} compared to {computer_value}"
    else:
        return f"\nYou lost with a score of {player_value} compared to {computer_value}"


def blackjack():
    print(logo)

    player = []
    computer = []



    for i in range(0, 2):
        player.append(deal_card())
        computer.append(deal_card())

    print(f"Your score = {calculate_score(player)}")

    picking = True
    while picking is True:

        if (calculate_score(player) == 0) or (calculate_score(computer) > 21):
            print(compare(calculate_score(player), calculate_score(computer)))
            picking = False

        elif (calculate_score(computer) == 0) or (calculate_score(player) > 21):
            print(compare(calculate_score(player), calculate_score(computer)))
            picking = False

        else:
            pick = input("\nDo you want to pick another card? Y or N > ").upper()

            if pick == "Y":
                player.append(deal_card())
                print(f"\nYour score = {calculate_score(player)}")

            elif pick == "N":
                while calculate_score(computer) < 17:
                    computer.append(deal_card())
                picking = False
                print(compare(calculate_score(player), calculate_score(computer)))

    play_again = input("\nDo you want to play again? Y or N > ").upper()

    if play_again == "Y":
        os.system('cls')
        blackjack()


blackjack()



