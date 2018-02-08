#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from segments.douban.config import CONFIG, ROOT_PATH


class ClearFile:
    @staticmethod
    def clear_records():
        if os.path.isfile(CONFIG['FILE']['RECORDS']):
            os.remove(CONFIG['FILE']['RECORDS'])

    @staticmethod
    def clear_imgs():
        img_dir = os.path.join(ROOT_PATH, CONFIG['FILE']['IMAGES_DIR'])
        for dirpath, dirnames, filenames in os.walk(img_dir):
            for file in filenames:
                img_path = os.path.join(img_dir, file)
                os.remove(img_path)

    @staticmethod
    def clear_classification():
        if os.path.isfile(CONFIG['FILE']['CLASSIFICATION']):
            os.remove(CONFIG['FILE']['CLASSIFICATION'])

    @staticmethod
    def clear_all():
        ClearFile.clear_records()
        ClearFile.clear_imgs()
        ClearFile.clear_classification()
