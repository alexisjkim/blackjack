import random
list = ['A','2','3','4','5','6','7','8','9','10','J','Q','K',
'A','2','3','4','5','6','7','8','9','10','J','Q','K',
'A','2','3','4','5','6','7','8','9','10','J','Q','K'
'A','2','3','4','5','6','7','8','9','10','J','Q','K']

print ("Welcome to Blackjack! ^^ My name is Luna and I will be your dealer for today.\nType 'quit' anytime if you would like to quit.")

while True:
    a = random.choice(list)
    b = random.choice(list)
    dealer1 = random.choice(list)
    dealer2 = random.choice(list)
    list.remove(a)
    list.remove(b)
    list.remove(dealer1)
    list.remove(dealer2)
    print ("The dealer's card is", dealer1, "and your cards are", a,"and", str(b)+". ")
    x = input("Type 'hit', 'stand', or 'double down.")
    if x == 'hit':
        hit = random.choice(list)
        list.remove(hit)
        print (hit)
