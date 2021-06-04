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

import random
# cards =[Ace,2,3,4,5,6,7,8,9,10,Jack,Queen,King]
cards_number = [11,2,3,4,5,6,7,8,9,10,10,10,10]



#todo 4: create function for 2 selected card of user and computer
"""returns random cards"""
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card
# empty lists to append the random generate item to it
user_card=[]
computer_card=[]

#we used underscore cause we don't the variable of for loop
for _ in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card())

#todo 5: Create function that take a list of cards as input and return the result

def score_sum_up(cards):
# Inside the method check for a blackjack and return 0 instead of the actual score cause 0 will represent a black in the game
    if 11 in cards and 10 in cards and len(cards)==2:
        return 0
#Checking ace (11) if the score is over 21, will remove 11 and replace it one
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

#todo 6: sum the result and annouce the winner