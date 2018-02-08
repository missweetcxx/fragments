#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from lxml import etree

from segments.douban.common.constants import HEADER
from segments.douban.config import CONFIG


class MovieDatum:
    @staticmethod
    def get_movie_etree(id, url=CONFIG['HTTP']['URL'], headers=HEADER):
        movie_etree = list()
        response = requests.get(url, headers=headers, params=dict(start=id))
        reponse_etree = etree.HTML(response.content)
        movie_items = reponse_etree.xpath(CONFIG['PATH']['MOVIE_ITEMS'])

        for movie_item in movie_items:
            id = movie_item.xpath(CONFIG['PATH']['MOVIE_ID'])
            title = movie_item.xpath(CONFIG['PATH']['MOVIE_TITLE'])
            score = movie_item.xpath(CONFIG['PATH']['MOVIE_SCORE'])
            desc = movie_item.xpath(CONFIG['PATH']['MOVIE_DESC'])
            img_addr = movie_item.xpath(CONFIG['PATH']['MOVIE_IMG_ADDR'])
            movie_info = movie_item.xpath(CONFIG['PATH']['MOVIE_INFO'] + '[2]')[0].strip()

            movie_item_dict = dict()
            movie_item_dict['id'] = id
            movie_item_dict['title'] = title
            movie_item_dict['score'] = score
            movie_item_dict['desc'] = desc
            movie_item_dict['img_addr'] = img_addr
            movie_item_dict['movie_info'] = movie_info
            movie_etree.append(movie_item_dict)

        return movie_etree
