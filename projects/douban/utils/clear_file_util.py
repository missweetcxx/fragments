#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from projects.douban.common.constants import FilePath
from projects.douban.config import CONFIG, ROOT_PATH


class ClearFile:
    @staticmethod
    def clear_records():
        if os.path.isfile(FilePath.RECORDS_PATH):
            os.remove(FilePath.RECORDS_PATH)

    @staticmethod
    def clear_imgs():
        img_dir = os.path.join(ROOT_PATH, CONFIG['FILE']['IMAGES_DIR'])
        for dirpath, dirnames, filenames in os.walk(img_dir):
            for file in filenames:
                img_path = os.path.join(img_dir, file)
                os.remove(img_path)

    @staticmethod
    def clear_classification():
        if os.path.isfile(FilePath.CLASSIFY_PATH):
            os.remove(FilePath.CLASSIFY_PATH)

    @staticmethod
    def clear_all():
        ClearFile.clear_records()
        ClearFile.clear_imgs()
        ClearFile.clear_classification()