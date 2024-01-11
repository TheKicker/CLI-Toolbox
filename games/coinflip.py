import random
decision = input('Heads or tails? (write 1 for heads and 2 for tails) : ')
flippedcoin = random.randint(1,2)
if flippedcoin == 1:
    print('It landed on heads.')
elif flippedcoin == 2:
    print('It landed on tails.')

if flippedcoin == int(decision):
    print('You Won!')
else:
    print('You Lost.')
