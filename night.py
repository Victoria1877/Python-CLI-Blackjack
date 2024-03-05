import random

print("\nWelcome to Victoria's Simple BJ.\nA Simple Command Line Blackjack Game\n")

play = input("Would you like to play a hand?\nyes or no: ").lower()

if play == "yes":
    beginGame = True
    print("Yay, lets play :3\n\n")
elif play == "no":
    print("All good, see you later.")
    quit()
else:
    print("I'll take that as a no, Byeee")
    quit()

def newCard():
    global cardSuit
    global cardNumber
    global cardSuitNum
    global card
    global cardName
    cardSuitNum = random.randint(1,4)
    cardNumber = random.randint(1,13)
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
        
    
    if cardSuitNum == 1:
        cardSuit = "Clubs"
    elif cardSuitNum == 2:
        cardSuit = "Hearts"
    elif cardSuitNum == 3:
        cardSuit = "Diamonds"
    elif cardSuitNum == 4:
        cardSuit = "Spades"
    card = str(cardNumber) + cardSuit

while beginGame == True:
    beginGame = False
    newCard()
    print("Your first card is the", cardNumber, "of", cardSuit)
    firstCardNum = cardNumber
    firstCardSuit = cardSuit
    newCard()
    print("Your second card is the", cardNumber, "of", cardSuit, "\n\n")
    secondCardNum = cardNumber
    secondCardSuit = cardSuit

    playerTotal = firstCardNum + secondCardNum
    print("Your total is:", playerTotal)
    hit = input("Do you want to hit?\nyes or no: ").lower()
    if hit == "yes":
        newCard()
        print("Your new card is the", cardName, "of", cardSuit)