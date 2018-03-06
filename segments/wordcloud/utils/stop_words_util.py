#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jieba

from segments.wordcloud.common.constants import FilePath


class StopWords:
    @staticmethod
    def filter(texts):
        jieba.add_word('')
        word_list = []
        word_generator = jieba.cut(texts, cut_all=False)
        with open(FilePath.STOPWORDS_PATH, encoding='utf-8') as f:
            stop_text = f.readlines()
            stop_list = [word.strip() for word in stop_text]
            f.close()
        for word in word_generator:
            if word.strip() not in stop_list:
                word_list.append(word)

        res = ' '.join(word_list)
        return res
