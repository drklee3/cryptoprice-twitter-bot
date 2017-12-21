import twitter
import requests
import time
import os
import datetime
from collections import OrderedDict

CRYPTO_API_URL = "https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,BCH,ETH,LTC,XRP,ZEC,ETC&tsyms=USD"

def login():
    return twitter.Api(consumer_key="",
        consumer_secret="",
        access_token_key="",
        access_token_secret="")

def format_data(data):
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    message = "{} UTC\n\n".format(now)
    for key, value in data.items():
        message += "{}: ${}\n".format(key, value["USD"])

    print(message)
    print(len(message))
    return message

def prices():
    r = requests.get(CRYPTO_API_URL)
    data = r.json()
    print(data)
    data = OrderedDict(sorted(data.items(), key=lambda i: i[1]["USD"], reverse=True))
    print(data)

    return format_data(data)


def main():
    # login to twitter
    api = login()
    msg = prices()
    # status = api.PostUpdate(msg, verify_status_length=False)


if __name__ == "__main__":
    main()
