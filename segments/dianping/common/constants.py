#!/usr/bin/env python
# -*- coding: utf-8 -*-
from segments.dianping.config import CONFIG

HEADER = {"User-Agent": CONFIG['HTTP']['USER_AGENT']}


class Cities:
    _VALUES_TO_CN_CITIES = {
        1: '上海',
        2: '北京',
        3: '杭州',
        4: '广州',
        5: '南京',
        6: '苏州',
        7: '深圳',
        8: '成都',
        9: '重庆',
        10: '天津',
        11: '宁波',
        12: '扬州',
        13: '无锡',
        14: '福州',
        15: '厦门',
        16: '武汉',
        17: '西安',
        18: '沈阳',
        19: '大连',
        21: '青岛',
        22: '济南',
        23: '海口',
        24: '石家庄'
    }

    @staticmethod
    def get_cn_cities_by_value(value):
        return Cities._VALUES_TO_CN_CITIES.get(value)

    @staticmethod
    def get_city_list():
        return Cities._VALUES_TO_CN_CITIES.keys()


class ShopType:
    FOOD = 10
    SHOPPING = 20


class FoodCategory:
    ALL = 0


class RankType:
    POPSCORE = 'popscore'
    COMMENT = 'score'
    TASTE = 'score1'
    ATMOSPHERE = 'score2'
    SERVICE = 'score3'

    _VALUES_TO_CN_DESC = {
        'popscore': '最热门',
        'score': '评价最好',
        'score1': '口味最好',
        'score2': '环境最好',
        'score3': '服务最好'
    }

    @staticmethod
    def get_cn_desc_by_value(value):
        return RankType._VALUES_TO_CN_DESC.get(value)
