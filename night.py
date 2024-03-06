#!/usr/bin/env python3
import random
import time

## Creates a list for the cards drawn to prevent double ups
cardsDrawn = []

print("\nWelcome to Victoria's Simple BJ.\nA Simple Command Line Blackjack Game\n")

play = input("Would you like to play a hand?\ny or n: ").lower()

if play == "yes" or "y":
    beginGame = True
    print("Yay, lets play :3\nThe rules are dealer draws to 16 and stands on all 17s.\n\n")
elif play == "no" or "n":
    print("All good, see you later.")
    quit()
else:
    print("I'll take that as a no, Byeee")
    quit()

def newCard():
    ## Establises Global variables so they can be called outside of function
    global cardSuit
    global cardNumber
    global cardSuitNum
    global card
    global cardName
    global playerTotal
    global cardsDrawn

    cardName = str

    ## Loop for checking and rerolling card to ensure no repetition
    cardRepCheck = True
    while cardRepCheck == True:

        ## Creates the newCard's values
        cardSuitNum = random.randint(1,4)
        cardNumber = random.randint(1,13)

        ## Sets the newCard's value and name
        if cardNumber == 13:
            cardName = "King"
            cardNumber = 10
        elif cardNumber == 12:
            cardName = "Queen"
            cardNumber = 10
        elif cardNumber == 11:
            cardName = "Jack"
            cardNumber = 10
        elif cardNumber == 1:
            cardName = "Ace"
            if playerTotal <= 10:
                cardNumber = 11
            else:
                cardNumber = 1
        else:
            cardName = cardNumber

        ## Sets the New Card's Suit
        if cardSuitNum == 1:
            cardSuit = "Clubs"
        elif cardSuitNum == 2:
            cardSuit = "Hearts"
        elif cardSuitNum == 3:
            cardSuit = "Diamonds"
        elif cardSuitNum == 4:
            cardSuit = "Spades"
    
        ## Creates string of card
        card = str(cardName) + cardSuit
        if card in cardsDrawn:
            print("dupe")
            cardRepCheck = True
        else:
            cardRepCheck = False
            cardsDrawn.append(card)

## Main Gameplay Loop
while beginGame == True:
    beginGame = False
    cardsDrawn = []
    playerTotal = 0
    
    ## Creates the player's starting hand
    newCard()
    print("Your first card is the", cardName, "of", cardSuit)
    firstCardNum = cardNumber
    firstCardSuit = cardSuit
    newCard()
    print("Your second card is the", cardName, "of", cardSuit, "\n\n")
    secondCardNum = cardNumber
    secondCardSuit = cardSuit

    ## Calculates the players total and asks if they want to hit (if applicable)
    playerTotal = firstCardNum + secondCardNum
    print("Your total is:", playerTotal)
    if playerTotal == 21:
        print("Well played you've hit 21. I better get lucky if I don't want to lose.\nNow let's move to my hand.\n")
        hit = False
    elif playerTotal >= 22:
        print("Uh oh... Its brokken")
    else:
        hitYN = input("Do you want to hit?\ny or n: ").lower()
        if hitYN == "y":
            hit = True
        elif hitYN == "n":
            hit = False
        else:
            print("I'll take that as a no.\n")
            hitYN = False
            
    ## Loop for Hitting (adding a new card to the players hand)        
    while hit == True:
        newCard()
        playerTotal = playerTotal + cardNumber
        print("\nYour new card is the", cardName, "of", cardSuit)
        if playerTotal > 21:
            print("Bust!,", playerTotal, "better hope I bust too.\n")   
            hit = False 
        if playerTotal == 21:
            print("Well played you've hit 21. I better get lucky if I don't want to lose.\nNow let's move to my hand.\n")
            hit = False
        elif playerTotal < 21:
            print("Your new total is:", playerTotal)
            hitAgain = input("Hit again? \ny or n: ").lower()
            if hitAgain == "y":
                hit = True
            elif hitAgain == "n":
                print("Ok lets move on to my hand.\n")
                hit = False
            else:
                print("I'll take that as a no. Lets move onto my hand./n")
                hit = False

    ## Creates the dealer's starting hand
    newCard()
    print("\n\nMy first card is the", cardName, "of", cardSuit)
    dealerFirstCardNum = cardNumber
    dealerFirstCardSuit = cardSuit
    newCard()
    print("My second card is the", cardName, "of", cardSuit, "\n\n")
    dealerSecondCardNum = cardNumber
    dealerSecondCardSuit = cardSuit

    ## Calculates the Dealer's total
    dealerTotal = dealerFirstCardNum + dealerSecondCardNum
    print("My total is:", dealerTotal)
    contDealerCalc = True
    time.sleep(0.5)

    ## Calculates win/loss/hit
    while contDealerCalc == True:
        ## Dealer and player hit 21
        if dealerTotal == 21 and playerTotal == 21:
            print("Ooh I've hit 21 thats very lucky.\n Result: Push\n\n")
            contDealerCalc= False

        ## Dealer hits 21 and player doesn't
        elif dealerTotal == 21 and playerTotal != 21:
            print("Yayyy, I win with 21.\nResult: Loss")
            contDealerCalc= False

        ## Dealer is under 17 (hit)
        elif dealerTotal <= 16:
                newCard()
                print("My new card is the", cardName, "of", cardSuit, "\n\n")
                dealerTotal = dealerTotal + cardNumber
                print("My new total is:", dealerTotal)

        ## Dealer goes bust Player Doesn't
        elif dealerTotal > 21 and playerTotal <= 21:
            print("I'm Bust, you win. Well played.\nResult: Win")
            contDealerCalc= False

        ## player goes bust dealer doesn't
        elif 17 <= dealerTotal < 21 and playerTotal > 21:
            print("A-hah you're bust and i'm not, unfortunate for you.\nResult: Loss")
            contDealerCalc= False

        ## Dealer and Player go bust
        elif dealerTotal > 21 and playerTotal > 21:
            print("We both go bust hahah. Lets go again.\nResult: Push")
            contDealerCalc= False

        ## Dealer stands on a 17
        elif dealerTotal >= 17 < 21:
            if dealerTotal > playerTotal:
                print("A-hah I win. Shall we play another?\nResult: Loss")
                contDealerCalc= False
            else:
                print("Awwww you win, ah well. Wanna play again?\nResult: Win")
                contDealerCalc= False
        else:
            print("error: unfinished")
            contDealerCalc= False
        print("Your score:", playerTotal, "Dealer Score:", dealerTotal)
    

    ## Repeat the beginGame loop
    print("Play Again?")
    playAgain = input("y or n: ")
    if playAgain == "y":
        beginGame = True
    elif playAgain =="n":
        beginGame = False
    else:
        print("I'll take that as a no. I'll see you next time.")