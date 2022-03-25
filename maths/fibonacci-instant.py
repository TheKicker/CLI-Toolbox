limit = input("Enter the maximum level you want your Fibonacci sequence calculated to: ")

a=0
b=1
i=0

while i < int(limit)-1:
    c = a + b
    a = b
    b = c
    i+=1
    d = i+1

print("{0}: {1}".format(str(d),b))