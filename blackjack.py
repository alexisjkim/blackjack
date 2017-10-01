def deck(n):
    onedeck = []
    for num in [2, 3, 4]:
        for suit in ['heart', 'spade','club','diamond']:
            onedeck.append( (num, suit)  )
    alldecks = []
    for i in range(n):
        alldecks.extend(onedeck)
    return alldecks

def blackjack(debug=False, file=""):
    round = 1
    losses = 0
    coins = 5000
    wins = 0
    print("Welcome to Blackjack! ^^ My name is Luna and I will be your dealer for today.\nType 'quit' anytime if you would like to quit.")
    import random
    random.seed(1)


    decks = eval(input("How many decks would you like?"))
    list = deck(decks)
    random.shuffle(list)
    f = open(file, 'w')
    if debug == True:
        event = 1
        for i in range(10):
            f.write('\n\n' + str(i)+'\n\n')
            a = list.pop()
            b = list.pop()
            dealer1 = list.pop()
            dealer2 = list.pop()
            if a[0] == 'A':
                f.write("player card"+a+'\n')
                a[0] = 11
            if b[0] == 'A':
                f.write("player card"+b+'\n')
                b[0] = 11
            if dealer1[0] == 'A':
                f.write("dealer card:" + dealer1+'\n')
                dealer1[0] = 11
            if dealer2[0] == 'A':
                f.write("dealer card:"+ dealer2)
                dealer2[0] = 11
            if a[0] == 'J' or a[0] == 'Q' or a[0] == 'K':
                f.write('player card:'+ a+'\n')
                a[0] = 10
            if b[0] == 'J' or b[0] == 'Q' or b[0] == 'K':
                f.write('player card:' + b + '\n')
                b[0] = 10
            if dealer1[0] == 'J' or dealer1[0] == 'Q' or dealer1[0] == 'K':
                f.write('dealer card:' + dealer1 + '\n')
                dealer1[0] = 10
            if dealer2[0] == 'J' or dealer2[0] == 'Q' or dealer2[0] == 'K':
                f.write('dealer card:' + dealer2 + '\n')
                dealer2[0] = 10
            f.write('Round '+str(round)+', event '+str(event)+': '+'      player cards are: '+str(a)+', '+str(b)+'   dealer cards are '+str(dealer1)+' and ?')
            playersum = a[0] + b[0]
            dealersum = dealer1[0] + dealer2[0]
            f.write('\nplayersum:'+str(playersum))
            f.write('   dealersum: '+str(dealersum)+'\n')
            while playersum < 17:
                hit = list.pop()
                if hit[0] == 'J' or hit[0] == 'Q' or hit[0] == 'K':
                    hit[0] = 10
                if hit[0] == 'A':
                    hit[0] = 11
                f.write('player hit and got:')
                f.write (str(hit))
                f.write ('\n')
                playersum += hit[0]
            while dealersum < 17:
                hit = list.pop()
                if hit[0] == 'J' or hit[0] == 'Q' or hit[0] == 'K':
                    hit[0] = 10
                if hit[0] == 'A':
                    hit[0] = 11
                f.write('\ndealer hit and got:')
                f.write (str(hit))
                f.write('\n')
                dealersum += hit[0]
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
            f.write("haha you're out of money lol")
            break
        print ("wins, losses:", wins, losses)
        print ('\nNew Game')
        print ("You have",coins,"coins.\n")
        f.write("wins, losses:"+ str(wins)+ str(losses))
        print('\nNew Game')
        print("You have", coins, "coins.\n")
        while True:
            bet = eval(input("How many coins would you like to bet?"))
            if bet > coins:
                print ("Sorry, that's too high.")
            if bet < coins or bet == coins:
                break
        if len(list) == 4 or len(list) < 4:
            print ("out of cards, shuffling")
            f.write("\nout of cards, shuffling \n")
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
            f.write("Type 'hit', 'stand', or 'cheat mode'. ")
        elif a != b:
            x = input("Type 'hit', 'stand', 'cheat mode', or 'double down.' ")
            f.write("\nType 'hit', 'stand', 'cheat mode', or 'double down.' \n")
        f.write(str(x))
        if x == 'quit':
            print("Thanks for playing!")
            f.write("Thanks for playing!")
            break
        if a + b == 21:
            print ("You got a blackjack!")
            f.write("You got a blackjack!")
            wins += 1
            coins += bet*1.5
        if dealer1 + dealer2 == 21:
            print ("I got a blackjack!")
            f.write('\nI got a blackjack.\n')
            coins = coins - bet*1.5
            continue
        playersum = a + b
        while True:
            if x == 'split':
                break
            if x == 'double down' or x == 'dd' or x == 'd':
                bet = bet * 2
                hit[0] = list.pop()
                if hit[0] == 'J' or hit[0] == 'Q' or hit[0] == 'K':
                    hit[0] = 10
                if hit[0] == 'A':
                    hit[0] = 11
                print ('Your new card:', hit[0])
                print('Your new card:' + hit[0])
                playersum += hit[0]
                print ("Your new total:", playersum)
                break
            if x == 'cheat' or x == 'c':
                print (list[::-1])
            if x == 'h' or x == 'hit':
                hit = list.pop()
                print ("your new card:",hit)
                if hit[0] == 'J' or hit[0] == 'Q' or hit[0] == 'K':
                    hit[0] = 10
                if hit[0] == 'A':
                    hit[0] = 11
                playersum += hit[0]
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
            if hit[0] == 'J' or hit[0] == 'K' or hit[0] == 'Q':
                hit[0] = 10
            if hit[0] == 'J' or hit[0] == 'Q' or hit[0] == 'K':
                hit[0] = 10
            if hit[0] == 'A':
                hit[0] = 11
            if hit2[0] == 'A':
                hit2[0] = 11
            split1 = a + hit[0]
            split2 = b + hit2[0]
            bet = bet * 2
            while True:
                x = input("hit or stand?")
                if x == 'h' or x == 'hit':
                    hit = list.pop()
                    print ("your new card is", hit)
                    if hit[0] == 'Q' or hit[0] == 'K' or hit[0] == 'J':
                        hit[0] = 10
                    if hit[0] == 'A':
                        hit[0] = 11
                    whichone = input ('do you want it on the first or second one')
                    if whichone == '1':
                        split1 += hit[0]
                    elif whichone == '2':
                        split2 += hit[0]
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
            f.write('\nyou busted\n')
            coins = coins - bet
            losses += 1
            continue
        dealersum = dealer1 + dealer2
        print ("Dealer's cards:", dealer1, dealer2)
        f.write("Dealer's cards:"+ dealer1+' ' + dealer2)
        while True:
            if dealersum > 16:
                break
            if dealersum > 21:
                break
            dealerhit = list[len(list)-1]
            list.pop()
            print ("the dealer hit and got:",dealerhit)
            f.write("the dealer hit and got:" + dealerhit)
            if dealerhit[0] == 'J' or dealerhit[0] == 'Q' or dealerhit[0] == 'K':
                dealerhit[0] = 10
            if dealerhit[0] == 'A':
                dealerhit[0] = 11
            dealersum += dealerhit[0]
        print ('dealer total:', dealersum)
        if dealersum > 21:
            print ("dealer busted")
            wins += 1
            coins += bet
            continue
        if dealersum < 22:
            if dealersum > playersum:
                print ("dealer wins!")
                f.write("\ndealer wins!\n")
                coins = coins - bet
                losses += 1
            if dealersum == playersum:
                print ('push')
                f.write('\npush\n')
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