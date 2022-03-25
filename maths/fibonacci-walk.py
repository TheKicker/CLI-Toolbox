from time import sleep

limit = input("Enter the maximum level you want your Fibonacci sequence calculated to: ")
s = 1

a=0
b=1
i=0

def start():
    # Bandaid fix for the first number
    sleep(s)
    print("1: 1")

start()

while i < int(limit)-1:
    c = a + b
    a = b
    b = c
    sleep(s)
    i+=1
    d = i+1
    print("{0}: {1}".format(str(d),b))

