import time
print("----- Welcome to FizzBuzz -----")
fizz = input("What number should be Fizz? ")
buzz = input("What number should be Buzz? ")
limit = input("What number should we count to? ")
initial = 1
words = ""

with open("file.txt", 'w') as f:
    f.write("FizzBuzz 3.0 by Cav Lemasters (Fizz {0}/ Buzz {1} / Limit {2})".format(fizz, buzz, limit))
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
        
        f.write("\n{0}".format(words))
        initial += 1
    f.close()