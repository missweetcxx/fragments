#!/usr/bin/env python
# -*- coding: utf-8 -*-
from xml import etree

import requests

from projects.dianping.common.constants import HEADER
from projects.dianping.config import CONFIG


class ShoplistDatum:
    @staticmethod
    def get_shoplist_items(city, shop_type, category, rank_type):
        params = {
            'cityId': city,
            'shopType': shop_type,
            'categoryId': category,
            'rankType': rank_type
        }
        response = requests.get(url=CONFIG['HTTP']['SHOPLIST_URL'], params=params, headers=HEADER).json()
        shop_items = response['shopBeans']

        return shop_items

    @staticmethod
    def get_avg_price_by_city(city, shop_type, category, rank_type):
        avg_price_sum = 0
        shop_items = ShoplistDatum.get_shoplist_items(city, shop_type, category, rank_type)
        for item in shop_items[:100]:
            avg_price_sum += item['avgPrice']
        avg_price_avg = avg_price_sum / 100
        return avg_price_avg

    @staticmethod
    def get_exotic_shoplist_items(city):
        response = requests.get(CONFIG['HTTP']['EX_SHOPLIST_URL'].format(city), headers=HEADER)
        reponse_etree = etree.HTML(response.content)
        shop_items = reponse_etree.xpath(CONFIG['PATH']['EX_SHOP_ITEMS'])[0]

        avg_price_list = [int(item) for item in shop_items.xpath(CONFIG['PATH']['EX_SHOP_PRICES'])]

        avg_price = round(sum(avg_price_list) / len(avg_price_list), 2)

        return avg_price
