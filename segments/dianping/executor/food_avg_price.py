#!/usr/bin/env python
# -*- coding: utf-8 -*-
from segments.dianping.common.constants import Cities, ShopType, FoodCategory, RankType
from segments.dianping.common.file_path import FilePath
from segments.dianping.utils.clear_file_util import ClearFile
from segments.dianping.utils.shoplist_datum_util import ShoplistDatum


def get_food_avg_price_aggregation_by_popscore(rank_type):
    city_list = Cities.get_city_list()
    city_avg_price = {}
    for city in city_list:
        avg_price_avg = ShoplistDatum.get_avg_price_by_city(city=city, shop_type=ShopType.FOOD,
                                                            category=FoodCategory.ALL,
                                                            rank_type=rank_type)
        city_avg_price[Cities.get_cn_cities_by_value(city)] = avg_price_avg

    return city_avg_price


def city_avg_price_output(rank_type):
    with open(FilePath.AVG_PRICE_BY_CITY_POP, 'ab+') as f:
        city_avg_price = get_food_avg_price_aggregation_by_popscore(rank_type)
        sorted_list = sorted(city_avg_price.items(), key=lambda item: item[1], reverse=True)
        f.write('{}前100餐厅人均消费：\n'.format(RankType.get_cn_desc_by_value(rank_type)).encode('utf-8'))
        for item in sorted_list:
            record = '{}:{}元'.format(item[0], item[1]) + "\n"
            f.write(record.encode('utf-8'))
            print(record)


def main():
    ClearFile.clear_avg_price_records()

    city_avg_price_output(rank_type=RankType.TASTE)


if __name__ == '__main__':
    main()
