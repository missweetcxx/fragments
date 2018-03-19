#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup as bs


def get_historical_data(name, number_of_days):
    data = []
    url = "https://finance.yahoo.com/quote/" + name + "/history/"
    content = requests.get(url).content
    rows = bs(content, 'html.parser').findAll('table')[0].tbody.findAll('tr')

    for each_row in rows:
        divs = each_row.findAll('td')
        if divs[1].span.text != 'Dividend':
            data.append({'Date': divs[0].span.text, 'Open': float(divs[1].span.text.replace(',', ''))})

    return data[:number_of_days]


if __name__ == '__main__':
    get_historical_data('AAPL', 10)
