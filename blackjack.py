import random
list = [1,2,3,4,5,6,7,8,9,10,10,10,
       1, 2, 3, 4, 5, 6, 7, 8, 9, 10,10,10,
        1,2,3,4,5,6,7,8,9,10,10,10,
        1,2,3,4,5,6,7,8,9,10,10,10]
random.shuffle(list)
suit = ['club', 'diamond', 'heart', 'spade']


print ("Welcome to Blackjack! ^^ My name is Luna and I will be your dealer for today.\nType 'quit' anytime if you would like to quit.")

wins = 0
losses = 0
while True:
    dealersuit = random.choice(suit)
    print ("wins, losses:", wins, losses)
    print ('\nNew Game')
    if len(list) == 4 or len(list) < 4:
        print ("out of cards, shuffling")
        list.shuffle()
        continue
    a = list.pop()
    b = list.pop()
    dealer1 = list.pop()
    dealer2 = list.pop()
    print ("The dealer's up card is", dealer1, random.choice(suit), "and your cards are\n", a,random.choice(suit),"and", str(b),random.choice(suit)+".  ")
    x = input("Type 'hit' or 'stand'.")
    if x == 'quit':
        print ("Thanks for playing!")
        break
    if a + b == 21:
        print ("You got a blackjack!")
        wins += 1
        continue
    if dealer1 + dealer2 == 21:
        print ("I got a blackjack!")
    playersum = a + b
    while True:
        if x == 'h' or x == 'hit':
            hit = list.pop()
            playersum += hit
            print ("your new card:",hit,random.choice(suit), "your new total:", playersum)
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
    print ("Dealer's cards:", dealer1,dealersuit, dealer2, random.choice(suit))
    while True:
        if dealersum > 16:
            break
        if dealersum > 21:
            break
        dealerhit = list[len(list)-1]
        list.pop()
        print ("the dealer hit and got:",dealerhit, random.choice(suit))
        dealersum += dealerhit
    print ('dealer total:', dealersum)
    if dealersum > 21:
        print ("dealer busted")
        wins += 1
    if dealersum < 22:
        if dealersum > playersum:
            print ("dealer wins!")
            losses += 1
        if dealersum == playersum:
            print ('push')
        if dealersum < playersum:
            print ('you win')
            wins += 1
'''
to do list

aces, kings, and queens 
double down and split
suits (spades, hearts, clubs, diamonds)
change 'hit' and 'stand' to 'h' and 's'

'''