#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

from os import path
from random import Random
from scipy.misc import imread
from wordcloud import WordCloud

from segments.wordcloud.common.constants import FilePath, Color
from segments.wordcloud.config import logger_config, ROOT_PATH, CONFIG

Logger = logging.getLogger(__name__)
logger_config()


class WordCouldUtil:
    @staticmethod
    def formatter(backgroud, max_words, max_font_size, stopwords, font_path, random_state):
        color_map = Color.MAP[Random().randint(0, len(Color.MAP) - 1)]
        FilePath.RESULT_PATH = path.join(ROOT_PATH, CONFIG['FILE']['RESULT_FILE'].format(color_map))
        Logger.info('color_map is "{}"'.format(color_map))
        back_color = imread(FilePath.MASK_PATH)

        wc = WordCloud(background_color=backgroud,
                       max_words=max_words,
                       colormap=color_map,
                       mask=back_color,
                       max_font_size=max_font_size,
                       stopwords=stopwords,
                       font_path=font_path,
                       random_state=random_state,
                       )
        return wc
