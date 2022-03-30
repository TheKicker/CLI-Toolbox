from dotenv import dotenv_values
config = dotenv_values("../.env")
from time import sleep

import finnhub

# Setup client
finnhub_client = finnhub.Client(api_key=config["finnhub_api"])

ticker = input("What is the ticker symbol for the stock you would like to see? ")


while True:
    res = finnhub_client.quote(ticker.upper())
    print("-------------------------")
    print("{0}     {1} ({2}%)       ".format(ticker.upper(), res["c"], res["dp"]))
    print("-------------------------")
    sleep(2.5)
