rate = input("\n What are you paid per hour? ")
rate = float(rate)
decimal_places = 3

def calculate(rate):
    sixty = round(rate * 1, decimal_places)
    fourtyfive = round(rate * 0.75, decimal_places)
    thirty = round(rate * 0.5, decimal_places)
    twenty = round(rate * 0.33, decimal_places)
    fifteen = round(rate * 0.25, decimal_places)
    ten = round(rate * 0.166666666, decimal_places)
    permin = round(rate * (1/60), decimal_places)
    perhalfmin = round(rate * (1/120), decimal_places)
    perquamin = round(rate * (1/240), decimal_places)
    perfivesec = round(rate * (1/720), decimal_places)
    persec = round(rate * (1/3600), decimal_places)
    print("\n 60 min: {0} \n 45 min: {1} \n 30 min: {2} \n 20 min: {3} \n 15 min: {4} \n 10 min: {5} \n 01 min: {6} \n 30 sec: {7} \n 15 sec: {8} \n 05 sec: {9} \n 01 sec: {10} \n".format(
        sixty, fourtyfive, thirty, twenty, fifteen, ten, permin, perhalfmin, perquamin, perfivesec, persec))


calculate(rate)