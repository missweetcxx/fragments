#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import requests

from segments.douban.common.constants import HEADER, Tag
from segments.douban.config import CONFIG


class OutputUtils:
    @staticmethod
    def download_img(id, title, img_addr, headers=HEADER):
        os.makedirs(CONFIG['FILE']['IMAGES_DIR']) if not os.path.exists(CONFIG['FILE']['IMAGES_DIR']) else None

        image_data = requests.get(img_addr, headers=headers).content
        image_path = CONFIG['FORMAT']['IMG'].format(CONFIG['FILE']['IMAGES_DIR'], id[0], title[0])

        with open(image_path, "wb") as f:
            f.write(image_data)

    @staticmethod
    def classification(sort_by_count=True):
        for key, value in Tag.COUNT.items():
            avg_score = round(Tag.SCORE.get(key, 0) / value, 2)
            Tag.AVG[key] = avg_score

        with open(CONFIG['FILE']['CLASSIFICATION'], "wb") as f:
            if sort_by_count is True:
                tag_list = sorted(Tag.COUNT.items(), key=lambda item: item[1], reverse=True)
                for record in tag_list:
                    key, value = record[0], record[1]
                    tmp_data = '[{}]共有{}部，均分{}'.format(key, value, Tag.AVG[key]) + "\n"
                    f.write(tmp_data.encode("utf-8"))

            else:
                tag_list = sorted(Tag.AVG.items(), key=lambda item: item[1], reverse=True)
                for record in tag_list:
                    key, value = record[0], record[1]
                    tmp_data = '[{}]共有{}部，均分{}'.format(key, Tag.COUNT[key], value) + "\n"
                    f.write(tmp_data.encode("utf-8"))
