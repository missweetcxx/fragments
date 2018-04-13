#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from lxml import etree
from segments.douban.common.constants import HEADER

from projects.douban.config import CONFIG


class BookDatum:
    @staticmethod
    def get_book_etree(id, url=CONFIG['HTTP']['BOOK_URL'], headers=HEADER):
        book_etree = list()
        response = requests.get(url, headers=headers, params=dict(start=id))
        reponse_etree = etree.HTML(response.content)
        book_items = reponse_etree.xpath(CONFIG['PATH']['BOOK_ITEMS'])[0]

        title = [str(item) for item in book_items.xpath(CONFIG['PATH']['BOOK_TITLE'])]
        score = [float(item) for item in book_items.xpath(CONFIG['PATH']['BOOK_SCORE'])]
        desc = [str(item) for item in book_items.xpath(CONFIG['PATH']['BOOK_DESC'])]

        for i in range(len(title)):
            book_item_dict = dict()
            book_item_dict['title'] = title[i]
            book_item_dict['score'] = score[i]
            book_item_dict['desc'] = desc[i]
            book_etree.append(book_item_dict)

        return book_etree
