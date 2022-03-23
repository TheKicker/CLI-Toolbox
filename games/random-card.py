import random

families = ["Clubs", "Hearts", "Spades", "Diamonds"]
values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

j = random.randint(0,54)

if(j > 52):
    print("Joker")
else:
    f = random.randint(0, len(families)-1)
    v = random.randint(0, len(values)-1)
    print("{0} of {1}".format(values[v], families[f]))