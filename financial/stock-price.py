from dotenv import dotenv_values
config = dotenv_values("../.env")

import finnhub

# Setup client
finnhub_client = finnhub.Client(api_key=config["finnhub_api"])

ticker = input("What is the ticker symbol for the stock you would like to see? ")

res = finnhub_client.quote(ticker.upper())

print("")
print("------------------------------------------------")
print("{0}                            {1} ({2}%)       ".format(ticker.upper(), res["c"], res["dp"]))
print("------------------------------------------------")
print("")