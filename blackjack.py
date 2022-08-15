import random

# Array of possible values of cards
# 3 values of 10 because each face card has value of 10 
deck=[2,3,4,5,6,7,8,9,10,10,10,11]  

# Functions to deal a card
# ACE will default to 1 if 11 would cause player/dealer to lose
def deal_card_player(deck):
    x=random.choice(deck)
    if x==11 and playerhand>=11:
        return 1
    else:
        return x
 
def deal_card_dealer(deck):
    x=random.choice(deck)
    if x==11 and dealerhand>=11:
        return 1
    else:
        return x

# Totals of both players hands
dealerhand=deal_card_player(deck)
playerhand=deal_card_dealer(deck)+deal_card_dealer(deck)
 
print("Dealer's total ", dealerhand)
print("Your total is ", playerhand)
 
# Gives player option to Hit or Stick if hand value under 21
while playerhand<=21:
    HorS=input("Hit or Stick? ")
 
    if HorS.upper()=="HIT":
       
        playerhand+=deal_card_player(deck)
        if playerhand>21: 
            print("Your total is now ", playerhand)
            print("You lose :(")
            quit()
        elif playerhand==21:
            print("Your total is now ", playerhand)
            print("You win!!!")
            quit()
        else:
            print("Your total is now ", playerhand)
 
    elif HorS.upper()=="STICK":
        break
    else:
        print("invalid input ")
 
 
 
#If player sticks and hand is under 21 simulates dealer
while dealerhand<playerhand and dealerhand<=17:
    dealerhand+=deal_card_dealer(deck)
    print("The dealer hit and total is now ", dealerhand)
   
    if dealerhand>=playerhand and dealerhand<=21:
            print("Dealer wins")
            quit()
if playerhand>dealerhand and playerhand<=21 or dealerhand>21:
        print("You Win!!!! ")
        quit()
    
 
 

