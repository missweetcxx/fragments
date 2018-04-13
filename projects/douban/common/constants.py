#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import path

from projects.douban.config import CONFIG, ROOT_PATH

HEADER = {"User-Agent": CONFIG['HTTP']['USER_AGENT']}


class FilePath:
    RECORDS_PATH = path.join(ROOT_PATH, CONFIG['FILE']['RECORDS'])
    IMG_PATH = path.join(ROOT_PATH, CONFIG['FILE']['IMAGES_DIR'])
    CLASSIFY_PATH = path.join(ROOT_PATH, CONFIG['FILE']['CLASSIFICATION'])


class Tag:
    COUNT = {}
    SCORE = {}
    AVG = {}
