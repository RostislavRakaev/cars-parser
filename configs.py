import pandas as pd

HEADERS = {
    'authority': 'www.test.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
    'sec-fetch-dest': 'document',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'accept-language': 'en-US,en;q=0.9',
}

class Car:
    def __init__(self, name, price, link):
        self.name = name
        self.price = price
        self.link = link

    def __repr__(self):
        return str(self.__dict__)


def parseTable(table):
    res = pd.DataFrame()

    res = res.append(
        pd.DataFrame([[table.name, table.price, table.link]], columns=['name', 'price', 'link']))
    return res