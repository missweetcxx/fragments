#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import requests
from lxml import etree

from segments.douban.config import CONFIG, ROOT_PATH


def download_img(id, title, img_addr, headers):
    os.makedirs(CONFIG['FILE']['IMAGES_DIR']) if not os.path.exists(CONFIG['FILE']['IMAGES_DIR']) else None

    image_data = requests.get(img_addr, headers=headers).content
    image_path = CONFIG['FORMAT']['IMG'].format(CONFIG['FILE']['IMAGES_DIR'], id[0], title[0])

    with open(image_path, "wb") as f:
        f.write(image_data)


def get_movies_datum(url, headers, id):
    response = requests.get(url, headers=headers, params=dict(start=id))
    reponse_etree = etree.HTML(response.content)
    movie_items = reponse_etree.xpath(CONFIG['PATH']['MOVIE_ITEMS'])

    for movie_item in movie_items:
        id = movie_item.xpath(CONFIG['PATH']['MOVIE_ID'])
        title = movie_item.xpath(CONFIG['PATH']['MOVIE_TITLE'])
        score = movie_item.xpath(CONFIG['PATH']['MOVIE_SCORE'])
        desc = movie_item.xpath(CONFIG['PATH']['MOVIE_DESC'])
        img_addr = movie_item.xpath(CONFIG['PATH']['MOVIE_IMG_ADDR'])

        print(CONFIG['FORMAT']['OUTPUT'].format(id, title, score, desc))

        with open(CONFIG['FILE']['RECORDS'], "ab+") as f:
            tmp_data = CONFIG['FORMAT']['OUTPUT'].format(id, title, score, desc) + "\n"
            f.write(tmp_data.encode("utf-8"))

        img_addr = str(img_addr[0].replace("\'", ""))
        download_img(id, title, img_addr, headers)


def clear_file():
    # remove txt file
    if os.path.isfile(CONFIG['FILE']['RECORDS']):
        os.remove(CONFIG['FILE']['RECORDS'])

    # remove img dictionary
    img_dir = os.path.join(ROOT_PATH, CONFIG['FILE']['IMAGES_DIR'])
    for dirpath, dirnames, filenames in os.walk(img_dir):
        for file in filenames:
            img_path = os.path.join(img_dir, file)
            os.remove(img_path)


def main():
    clear_file()
    ids = [i * 25 for i in range(10)]
    headers = {"User-Agent": CONFIG['HTTP']['USER_AGENT']}

    for id in ids:
        get_movies_datum(CONFIG['HTTP']['URL'], headers, id)


if __name__ == '__main__':
    main()
