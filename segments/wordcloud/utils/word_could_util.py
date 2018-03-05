#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scipy.misc import imread
from wordcloud import WordCloud

from segments.wordcloud.common.constants import FilePath


class WordCouldUtil:
    @staticmethod
    def formatter(backgroud, max_words, max_font_size, stopwords, font_path, random_state):
        back_color = imread(FilePath.MASK_PATH)
        wc = WordCloud(background_color=backgroud,
                       max_words=max_words,
                       mask=back_color,
                       max_font_size=max_font_size,
                       stopwords=stopwords,
                       font_path=font_path,
                       random_state=random_state,
                       )
        return wc
