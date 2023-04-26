import time
print("----- Welcome to FizzBuzz -----")
fizz = input("What number should be Fizz? ")
buzz = input("What number should be Buzz? ")
limit = input("What number should we count to? ")
initial = 1
words = ""

while initial <= int(limit):
    if (initial % int(fizz) == 0):
        if (initial % int(buzz) == 0):
            words = "FizzBuzz"
        else:
            words = "Fizz"
    elif (initial % int(buzz) == 0):
        words = "Buzz"
    else:
        words = str(initial)
    
    print(words)
    initial += 1
    time.sleep(1)