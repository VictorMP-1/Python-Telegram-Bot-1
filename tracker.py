import requests


def get_prices():
    coins = ["BTC", "ETH", "XRP", "LTC", "BCH",
             "ADA", "DOT", "LINK", "BNB", "XLM"]

    crypto_data = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms=BRL".format(",".join(coins))).json()["RAW"]

    data = {}
    for i in crypto_data:
        data[i] = {
            "coin": i,
            "price": crypto_data[i]["BRL"]["PRICE"],
            "change_day": crypto_data[i]["BRL"]["CHANGEPCT24HOUR"],
            "change_hour": crypto_data[i]["BRL"]["CHANGEPCTHOUR"]
        }

    return data


if __name__ == "__main__":
    print(get_prices())
