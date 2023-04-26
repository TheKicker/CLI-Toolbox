import time

rate = input("\n What are you paid per hour? ")
rate = float(rate)
decimal_places = 3
persec = round(rate * (1/3600), decimal_places)
wallet = 0

while True:
    time.sleep(1)
    wallet += persec
    print("${0}".format(round(wallet, decimal_places)))