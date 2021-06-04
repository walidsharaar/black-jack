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

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#todo 1: create function for 2 selected card of user and computer
"""returns random cards"""
def deal_card():
    # cards =[Ace,2,3,4,5,6,7,8,9,10,Jack,Queen,King]
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

user_card=[]
computer_card=[]



#todo 2: Create function that take a list of cards as input and return the result

def score_sum_up(cards):
    """Take list of card and return the score"""
# Inside the method check for a blackjack and return 0 instead of the actual score cause 0 will represent a black in the game
    if 11 in cards and 10 in cards and len(cards)==2:
        return 0
#Checking ace (11) if the score is over 21, will remove 11 and replace it one
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# todo Create a function called compare() and pass in the user score and computer score.
#  If the computer and user both have the same score, then it's a draw.
#  If the computer has a blackjack (0), then the user loses.
#  If the user has a blackjack (0), then the user wins.
#  If the user score is over 21, then the user loses.
#  If the computer score is over 21, then the computer loses.
#  If none of the above, then the player with the highest score wins

def compare (user_score , computer_score):
    if user_score > 21 and computer_score >21:
        return "You Lose :("
    if user_score == computer_score:
        return "Draw :_"
    elif computer_score == 0:
        return "Lose , Opponent has Black Jack"
    elif user_score == 0:
        return "Win , You have Black Jack"
    elif computer_score >21:
        return "Opponent went over , You Win!"
    elif user_score>21:
        return "You went over,You Lose!"
    elif user_score>computer_score:
        return "You Win!"
    else:
        return "You Lose!"

def play():
    print(logo)
 # empty lists to append the random generate item to it

    user_cards=[]
    computer_cards=[]
    game_over=False

#we used underscore cause we don't the variable of for loop
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = score_sum_up(user_cards)
        computer_score=score_sum_up(computer_cards)
        print(f" Your cards:  {user_cards}, current score is : {user_score}")
        print(f" First Card of Computer is :{ computer_cards[0]}")

        if user_score==0 or computer_score == 0 or user_score>21:
            game_over = True
        else:
            user_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_deal == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score !=0 and computer_score <17:
        computer_cards.append(deal_card())
        computer_score=score_sum_up(computer_cards)
    print(f" Final hand is : {user_cards}, final score:{user_score}")
    print(f" Computer hand is: {computer_cards}, final score:{computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want to continue: Type 'y' or 'n': ") =="y":
    os.system('cls')
    play()


