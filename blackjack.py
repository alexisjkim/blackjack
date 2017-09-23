def deck(n):


    onedeck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K','A',
               2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K','A',
               2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K','A',
               2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K','A']
    alldecks = []
    for i in range(n):
        alldecks.extend(onedeck)
    return alldecks

def blackjack(debug=False, file=""):
    wins = 0
    losses = 0
    coins = 5000
    print("Welcome to Blackjack! ^^ My name is Luna and I will be your dealer for today.\nType 'quit' anytime if you would like to quit.")
    import random
    random.seed(1)


    decks = eval(input("How many decks would you like?"))
    list = deck(decks)
    random.shuffle(list)

    if debug == True:
        f = open(file,'w')
        for i in range(10):
            f.write('\n\n')
            f.write(str(i))
            f.write('\n\n')
            a = list.pop()
            b = list.pop()
            dealer1 = list.pop()
            dealer2 = list.pop()
            if a == 'A':
                a = 11
            if b == 'A':
                b = 11
            if dealer1 == 'A':
                dealer1 = 11
            if dealer2 == 'A':
                dealer2 = 11
            if a == 'J' or a == 'Q' or a == 'K':
                a = 10
            if b == 'J' or b == 'Q' or b == 'K':
                b = 10
            if dealer1 == 'J' or dealer1 == 'Q' or dealer1 == 'K':
                dealer1 = 10
            if dealer2 == 'J' or dealer2 == 'Q' or dealer2 == 'K':
                dealer2 = 10
            playersum = a + b
            dealersum = dealer1 + dealer2
            f.write('player card:')
            f.write(str(a))
            f.write('\nplayer card: ')
            f.write(str(b))
            f.write('\ndealer card: ')
            f.write(str(dealer1))
            f.write('\ndealer card: ')
            f.write(str(dealer2))
            f.write('\n')
            f.write('playersum:')
            f.write(str(playersum))
            f.write('dealersum:')
            f.write(str(dealersum))
            f.write('\n')
            while playersum < 17:
                hit = list.pop()
                if hit == 'J' or hit == 'Q' or hit == 'K':
                    hit = 10
                if hit == 'A':
                    hit = 11
                f.write('player hit and got:')
                f.write (str(hit))
                f.write ('\n')
                playersum += hit
            while dealersum < 17:
                hit = list.pop()
                if hit == 'J' or hit == 'Q' or hit == 'K':
                    hit = 10
                if hit == 'A':
                    hit = 11
                f.write('\ndealer hit and got:')
                f.write (str(hit))
                f.write('\n')
                dealersum += hit
            if playersum > 21:
                f.write ("player busted\n")
                next
            elif dealersum > 21:
                f.write ("dealer busted\n")
                next
            elif playersum > dealersum:
                f.write ("player won\n")
                next
            elif playersum < dealersum:
                f.write ('dealer won\n')
                next
            elif playersum == dealersum:
                f.write('push\n')
        done = "done"
        return done
    while True:
        if coins == 0:
            print ("Haha you're out of money lol")
        print ("wins, losses:", wins, losses)
        print ('\nNew Game')
        print ("You have",coins,"coins.\n")
        while True:
            bet = eval(input("How many coins would you like to bet?"))
            if bet > coins:
                print ("Sorry, that's too high.")
            if bet < coins or bet == coins:
                break
        if len(list) == 4 or len(list) < 4:
            print ("out of cards, shuffling")
            list = deck(decks)
            random.shuffle(list)
            continue
        a = list.pop()
        b = list.pop()
        dealer1 = list.pop()
        dealer2 = list.pop()
        if a == 'A':
            a = 11
        if b == 'A':
            b = 11
        if dealer1 == 'A':
            dealer1 = 11
        if dealer2 == 'A':
            dealer2 = 11
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
        if a == b:
            x = input ("Type hit, stand, cheat mode, double down, or split.")
        x = input("Type 'hit', 'stand', 'cheat mode', or 'double down.' ")
        if x == 'quit':
            print ("Thanks for playing!")
            break
        if a + b == 21:
            print ("You got a blackjack!")
            wins += 1
            coins += bet*1.5
        if dealer1 + dealer2 == 21:
            print ("I got a blackjack!")
            coins = coins - bet*1.5
            continue
        playersum = a + b
        while True:
            if x == 'split':
                break
            if x == 'double down' or x == 'dd' or x == 'd':
                bet = bet * 2
                hit = list.pop()
                if hit == 'J' or hit == 'Q' or hit == 'K':
                    hit = 10
                if hit == 'A':
                    hit = 11
                print ('Your new card:', hit)
                playersum += hit
                print ("Your new total:", playersum)
                break
            if x == 'cheat' or x == 'c':
                print (list[::-1])
            if x == 'h' or x == 'hit':
                hit = list.pop()
                print ("your new card:",hit)
                if hit == 'J' or hit == 'Q' or hit == 'K':
                    hit = 10
                if hit == 'A':
                    hit = 11
                playersum += hit
                print ('your new total:', playersum)
            if x == 's' or x == 'stand':
                break
            if playersum > 21:
                print ('bust, dealer wins')
                break
            x = input('hit or stand?')
        if x == 'split':
            hit = list.pop()
            hit2 = list.pop()
            print (a,hit, '\n',b,hit2)
            if hit == 'J' or hit == 'K' or hit == 'Q':
                hit = 10
            if hit2 == 'J' or hit2 == 'Q' or hit2 == 'K':
                hit = 10
            if hit == 'A':
                hit = 11
            if hit2 == 'A':
                hit2 = 11
            split1 = a + hit
            split2 = b + hit2
            bet = bet * 2
            while True:
                x = input("hit or stand?")
                if x == 'h' or x == 'hit':
                    hit = list.pop()
                    print ("your new card is", hit)
                    if hit == 'Q' or hit == 'K' or hit == 'J':
                        hit = 10
                    if hit == 'A':
                        hit = 11
                    whichone = input ('do you want it on the first or second one')
                    if whichone == '1':
                        split1 += hit
                    elif whichone == '2':
                        split2 += hit
                if x == 's' or x == 'stand':
                    break
                if split1 > 21:
                    print ("you busted")
                    coins = coins - bet
                    break
                if split2 > 21:
                    print("you busted")
                    coins = coins - bet
                    break
        if playersum > 21:
            print ('you busted')
            coins = coins - bet
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
            if dealerhit == 'A':
                dealerhit = 11
            dealersum += dealerhit
        print ('dealer total:', dealersum)
        if dealersum > 21:
            print ("dealer busted")
            wins += 1
            coins += bet
            continue
        if dealersum < 22:
            if dealersum > playersum:
                print ("dealer wins!")
                coins = coins - bet
                losses += 1
            if dealersum == playersum:
                print ('push')
            if dealersum < playersum:
                wins += 1
                coins += bet


a = blackjack(debug=True, file="log.txt")
print (a)
'''
to do list

fix coin thing
suits (spades, hearts, clubs, diamonds)

'''