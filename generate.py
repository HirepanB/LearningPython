import random #import a module called 'random.py'
#from random import chice #only you can use 'choice'

coin = random.choice(["heads","tails"])  #return one value, this return is with the same probalility
print(coin)


numer = random.randint(1,10) #return a number between 1 to 10
print(numer)

cards = ["jack","queen","king"]
print(cards)

random.shuffle(cards)
print(cards)

for card in cards:
    print(card)
 
