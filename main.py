import requests

from bs4 import BeautifulSoup

import pandas as pd

import sys
import os

from configs import Car, parseTable
from constantes import HEADERS, RESULTS_PATH

arguments = sys.argv[1:]

for arg in arguments:

    URL = f'https://auto.ria.com/uk/car/{arg}/'

    results = pd.DataFrame()

    parsedPages = 0

    for it in range(1, 30):

        url = f'{URL}?page={it}'

        session = requests.session()

        response = session.get(url, headers=HEADERS)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            carSection = soup.find_all('section', class_='ticket-item')

            if carSection != None:
                for idx, element in enumerate(carSection):
                    a = element.find('a', class_='address')
                    link = a.get('href')

                    for span in element.select('a span'):
                        if span.text != None:
                            name = span.text

                    price = element.find('span', class_='size22').text

                    data = Car(name, price, link)
                    res = parseTable(data)
                    results = results.append(res, ignore_index=True)

                parsedPages = parsedPages + 1

        else:
            break

    print(f'{arg} / Parsed pages: {parsedPages}')

    if not os.path.exists(RESULTS_PATH):
        os.mkdir(RESULTS_PATH)

    results.to_excel(f'./results/{arg}.xlsx')





