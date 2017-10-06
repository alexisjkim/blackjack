def deck(n):
    onedeck = []
    for num in [2, 3, 4]:
        for suit in ['heart', 'spade','club','diamond']:
            onedeck.append( (num, suit)  )
    alldecks = []
    for i in range(n):
        alldecks.extend(onedeck)
    return alldecks

def message(string,debug,f):
    if debug == True:
        f.write(string)
    else:
        f.write(string)
        return string

message_argument = True

def blackjack(debug, file=""):
    f = open('log.txt','w')
    #message(str(deck(1)),message_argument,f

    losses = 0
    coins = 5000
    wins = 0
    message("Welcome to Blackjack! ^^ My name is Luna and I will be your dealer for today.\nType 'quit' anytime if you would like to quit.",True,f)
    import random
    #random.seed(1)
    if debug == False:
        decks = eval(input("How many decks would you like?"))
    elif debug == True:
        decks = 100
    list = deck(decks)
    random.shuffle(list)
    debugcount = 0
    while True:
        if debug == True:
            debugcount += 1
        if debugcount == 10:
            break
        if coins == 0:
            message ("Haha you're out of money lol",message_argument,f)
            break
        message("wins, losses:"+ str(wins)+ ', '+str(losses),message_argument,f)
        message('\n\nNew Game',message_argument,f)
        message("\nYou have "+ str(coins)+ " coins.\n",message_argument,f)
        while True:
            if debug == True:
                bet = 100
                message("\nyour bet: "+str(bet),message_argument,f)
                break
            else:
                bet = eval(input("How many coins would you like to bet?"))
            if bet > coins:
                message ("Sorry, that's too high.",message_argument,f)
            if bet < coins or bet == coins:
                break
        if len(list) == 4 or len(list) < 4:
            message("\nout of cards, shuffling \n",message_argument,f)
            list = deck(decks)
            random.shuffle(list)
            continue
        a = list.pop()
        b = list.pop()
        dealer1 = list.pop()
        dealer2 = list.pop()
        message ("\nThe dealer's up card is" + str(dealer1)+ "and your cards are"+ str(a)+"and"+ str(b),message_argument,f)
        if a[0] == 'J' or a[0] == 'Q' or a[0] == 'K':
            a[0] = 10
        if b[0] == 'J' or b[0] == 'Q' or b[0] == 'K':
            b[0] = 10
        if dealer1[0] == 'J' or dealer1[0] == 'Q' or dealer1[0] == 'K':
            dealer1[0] = 10
        if dealer2[0] == 'J' or dealer2[0] == 'Q' or dealer2[0] == 'K':
            dealer2[0] = 10
        if a[0] == 'A':
            a[0] = 11
        if b[0] == 'A':
            b[0] = 11
        if dealer1[0] == 'A':
            dealer1[0] = 11
        if dealer2[0] == 'A':
            dealer2[0] = 11

        if a + b == 21:
            message ("You got a blackjack!",message_argument,f)
            wins += 1
            coins += bet*1.5
            continue
        if dealer1 + dealer2 == 21:
            message('\nI got a blackjack.\n',message_argument,f)
            coins = coins - bet*1.5
            continue
        if a == b:
            if debug == False:
                x=("Type hit, stand, cheat mode, double down, or split.")
        elif a != b:
            if debug == False:
                x=input("Type 'hit', 'stand', 'cheat mode', or 'double down.' ")
        playersum = a[0] + b[0]
        while True:
            if debug == True:
                while playersum < 17:
                    hit = list.pop()
                    message('\nplayer hit and got: '+str(hit),message_argument, f)
                    if hit[0] == 'J' or hit[0] == 'Q' or hit[0] == 'K':
                        hit[0] = 10
                    if hit[0] == 'A':
                        hit[0] = 11
                    playersum += hit[0]
                    message('\n\tPlayer sum: ' + str(playersum), message_argument, f)

                break
            if debug == False:
                if x == 'quit':
                    message('Thanks for playing.',message_argument,f)
                    break
                if x == 'split':
                    break
                if x == 'double down' or x == 'dd' or x == 'd':
                    bet = bet * 2
                    hit = list.pop()
                    if hit[0] == 'J' or hit[0] == 'Q' or hit[0] == 'K':
                        hit[0] = 10
                    if hit[0] == 'A':
                        hit[0] = 11
                    message ('Your new card:'+ str(hit[0])+'\n',message_argument,f)
                    playersum += hit[0]
                    message ("Your new total:"+ str(playersum)+'\n',message_argument,f)
                    break
                if x == 'cheat' or x == 'c':
                    message (list[::-1])
                if x == 'h' or x == 'hit':
                    hit = list.pop()
                    message ("your new card:"+str(hit)+'\n',message_argument,f)
                    if hit[0] == 'J' or hit[0] == 'Q' or hit[0] == 'K':
                        hit[0] = 10
                    if hit[0] == 'A':
                        hit[0] = 11
                    playersum += hit[0]
                    message ('your new total:'+ playersum,message_argument,f)
                if x == 's' or x == 'stand':
                    break
                if playersum > 21:
                    message ('bust, dealer wins',message_argument,f)
                    break
                x = input('hit or stand?')
                if x == 'split':
                    hit = list.pop()
                    hit2 = list.pop()
            #f.write(a,hit, '\n',b,hit2)
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
        dealersum = dealer1[0] + dealer2[0]
        while dealersum < 17:
            hit = list.pop()
            message('\ndealer hit and got:' + str(hit), message_argument, f)
            if hit[0] == 'J' or hit[0] == 'Q' or hit[0] == 'K':
                hit[0] = 10
            if hit[0] == 'A':
                hit[0] = 11
            dealersum += hit[0]
            message('\n\tDealer sum:' + str(dealersum), message_argument, f)
        if playersum > 21:
            message('\nyou busted\n',message_argument,f)
            coins = coins - bet
            losses += 1
            continue
        if dealersum > 21:
            print ("dealer busted",message_argument,f)
            wins += 1
            coins += bet
            continue
        if dealersum < 22:
            if dealersum > playersum:
                message("\ndealer wins!\n",message_argument,f)
                coins = coins - bet
                losses += 1
            if dealersum == playersum:
                message('push\n',message_argument,f)
            #f.write('\npush\n')
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