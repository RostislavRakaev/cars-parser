import pandas as pd

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