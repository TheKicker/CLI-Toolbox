import time
limit = input("Welcome to FizzBuzz! What number would you like to go to?  ")
initial = 1
words = ""

while initial <= int(limit):
    if (initial % 3 == 0):
        if (initial % 5 == 0):
            words = "FizzBuzz"
        else:
            words = "Fizz"
    elif (initial % 5 == 0):
        words = "Buzz"
    else:
        words = str(initial)
    
    print(words)
    initial += 1
    time.sleep(1)