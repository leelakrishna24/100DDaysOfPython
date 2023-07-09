#CS50p Libraries
import random
from random import choice

coin = choice(["Heads","Tails"])
#print(coin)

number = random.randint(1, 10)

#print(number)

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
random.shuffle(cards)

#for card in cards:
 #   print(card)

import statistics

#print(statistics.mean([100,90]))

import sys

# print("Hello, my name is",sys.argv[1])

if len(sys.argv) > 2:
    sys.exit("Too many arguments")
elif len(sys.argv) < 1:
    sys.exit("argument missing")

print("Hello my name is",sys.argv[1])