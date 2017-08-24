import random
list = [1,2,3,4,5,6,7,8,9,10,11,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print ("Welcome to Blackjack! ^^ My name is Luna and I will be your dealer for today.\nType 'quit' anytime if you would like to quit.")

while True:
    if len(list) == 4 or len(list) < 4:
        print ("out of cards")
        break
    a = random.choice(list)
    b = random.choice(list)
    dealer1 = random.choice(list)
    dealer2 = random.choice(list)
    list.remove(a)
    list.remove(b)
    list.remove(dealer1)
    list.remove(dealer2)
    print ("The dealer's card is", dealer1, "and your cards are", a,"and", str(b)+".  ")
    x = input("Type 'hit', 'stand', or 'double down.")
    if x == 'quit':
        print ("Thanks for playing!")
        break
    if a + b == 21:
        print ("You got a blackjack!")
        continue
    if dealer1 + dealer2 == 21:
        print ("I got a blackjack!")
        continue
    playersum = a + b
    while True:
        if x == 'hit':
            hit = random.choice(list)
            list.remove(hit)
            print (hit)
        if x == 'stand':
            print ('dealers cards are', dealer1,dealer2)
            print ('playersum =', playersum)
            break
        playersum += hit
        if playersum > 21:
            print ('bust')
            break
        x = input('hit or stand?')
    dealersum = dealer1 + dealer2
    print ("Dealer's cards:", dealer1,dealer2)
    while dealersum > 16:
        dealerhit = random.choice(list)
        list.remove(dealerhit)
        print (dealerhit)
        dealersum += dealerhit
    print ('dealer total:', dealersum)
    if dealersum > 21:
        print ("dealer busted")
    if dealersum < 22:
        if dealersum > playersum:
            print ("dealer wins!")
        if dealersum == playersum:
            print ('push')
        if dealersum < playersum:
            print ('you win')
'''
to do list

aces, kings, and queens 
double down and split

'''