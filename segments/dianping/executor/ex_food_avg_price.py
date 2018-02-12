#!/usr/bin/env python
# -*- coding: utf-8 -*-
from segments.dianping.common.constants import EX_CITIES
from segments.dianping.common.file_path import FilePath
from segments.dianping.utils.clear_file_util import ClearFile
from segments.dianping.utils.shoplist_datum_util import ShoplistDatum


def get_avg_price_by_city():
    ex_avg_price = dict()
    for city in EX_CITIES:
        avg_price = ShoplistDatum.get_exotic_shoplist_items(city)
        ex_avg_price[city] = avg_price
    return ex_avg_price


def ex_avg_price_output():
    ex_avg_price = get_avg_price_by_city()
    sorted_list = sorted(ex_avg_price.items(), key=lambda item: item[1], reverse=True)
    with open(FilePath.EX_AVG_PRICE_BY_CITY, 'ab+') as f:
        f.write('Average Consumption for Top15 Restaurants:\n\n'.encode('utf-8'))
        for item in sorted_list:
            record = '{} : {} CNY'.format(item[0].upper(), item[1]) + '\n'
            f.write(record.encode('utf-8'))
            print(record)


if __name__ == '__main__':
    ClearFile.clear_ex_avg_price_records()
    ex_avg_price_output()
