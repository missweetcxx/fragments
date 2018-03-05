#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import path
from scipy.misc import imread

from segments.wordcloud.config import CONFIG, ROOT_PATH


class FilePath:
    MASK_PATH = path.join(ROOT_PATH, CONFIG['FILE']['MASK'])
    FONT_PATH = path.join(ROOT_PATH, CONFIG['FILE']['FONT'])
    ARTICLE_PATH = path.join(ROOT_PATH, CONFIG['FILE']['ARTICLE'])
    STOPWORDS_PATH = path.join(ROOT_PATH, CONFIG['FILE']['STOPWORDS'])
    RESULT_PATH = path.join(ROOT_PATH, CONFIG['FILE']['RESULT_FILE'])


class Color:
    BACK_COLOR = imread(FilePath.MASK_PATH)
