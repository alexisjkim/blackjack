import random
decks = eval(input("How many decks would you like?"))

def deck(n):
    onedeck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
               1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
               1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
               1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    alldecks = []
    for i in range(n):
        alldecks.extend(onedeck)
    return alldecks

list = deck(decks)
random.shuffle(list)

print ("Welcome to Blackjack! ^^ My name is Luna and I will be your dealer for today.\nType 'quit' anytime if you would like to quit.")

wins = 0
losses = 0
yourcoins = 5000

while True:
    print ("wins, losses:", wins, losses)
    print ('\nNew Game')
    print ("You have",yourcoins,"coins.\n")
    while True:
        bet = eval(input("How many coins would you like to bet?"))
        if bet > yourcoins:
            print ("Sorry, that's too high.")
        if bet < yourcoins or bet == yourcoins:
            break
    yourcoins = yourcoins - bet
    if len(list) == 4 or len(list) < 4:
        print ("out of cards, shuffling")
        list = deck(decks)
        random.shuffle(list)
        continue
    a = list.pop()
    b = list.pop()
    dealer1 = list.pop()
    dealer2 = list.pop()
    if a == 'J' or a == 'Q' or a == 'K':
        a = 10
    if b == 'J' or b == 'Q' or b == 'K':
        b = 10
    if dealer1 == 'J' or dealer1 == 'Q' or dealer1 == 'K':
        dealer1 = 10
    if dealer2 == 'J' or dealer2 == 'Q' or dealer2 == 'K':
        dealer2 = 10
    print ("The dealer's up card is", dealer1, "and your cards are\n", a,"and", b)
    if a == 'J' or a == 'Q' or a == 'K':
        a = 10
    if b == 'J' or b == 'Q' or b == 'K':
        b = 10
    if dealer1 == 'J' or dealer1 == 'Q' or dealer1 == 'K':
        dealer1 = 10
    if dealer2 == 'J' or dealer2 == 'Q' or dealer2 == 'K':
        dealer2 = 10
    x = input("Type 'hit' or 'stand' or 'cheat mode.'")
    if x == 'quit':
        print ("Thanks for playing!")
        break
    if a + b == 21:
        print ("You got a blackjack!")
        wins += 1
        yourcoins += bet*2
        continue
    if dealer1 + dealer2 == 21:
        print ("I got a blackjack!")
        continue
    playersum = a + b
    while True:
        if x == 'cheat' or x == 'c':
            print (list[::-1])
        if x == 'h' or x == 'hit':
            hit = list.pop()
            print ("your new card:",hit)
            if hit == 'J' or hit == 'Q' or hit == 'K':
                hit = 10

            playersum += hit
            print ('your new total:', playersum)
        if x == 's' or x == 'stand':
            break
        if playersum > 21:
            print ('bust, dealer wins')
            break
        x = input('hit or stand?')
    if playersum > 21:
        print ('you busted')
        losses += 1
        continue
    dealersum = dealer1 + dealer2
    print ("Dealer's cards:", dealer1, dealer2)
    while True:
        if dealersum > 16:
            break
        if dealersum > 21:
            break
        dealerhit = list[len(list)-1]
        list.pop()
        print ("the dealer hit and got:",dealerhit)
        if dealerhit == 'J' or dealerhit == 'Q' or dealerhit == 'K':
            dealerhit = 10

        dealersum += dealerhit
    print ('dealer total:', dealersum)
    if dealersum > 21:
        print ("dealer busted")
        wins += 1
        continue
        yourcoins += bet*2
    if dealersum < 22:
        if dealersum > playersum:
            print ("dealer wins!")
            losses += 1
        if dealersum == playersum:
            print ('push')
        if dealersum < playersum:
            print ('you win')
            wins += 1
            yourcoins += bet*2
'''
to do list

aces, kings, and queens 
double down and split
suits (spades, hearts, clubs, diamonds)
change 'hit' and 'stand' to 'h' and 's'

'''