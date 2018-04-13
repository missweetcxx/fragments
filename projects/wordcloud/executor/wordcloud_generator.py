#!/usr/bin/env python
# -*- coding: utf-8 -*-
from wordcloud import STOPWORDS

from projects.wordcloud.common.constants import FilePath
from projects.wordcloud.utils.image_util import Image
from projects.wordcloud.utils.stop_words_util import StopWords
from projects.wordcloud.utils.word_could_util import WordCouldUtil

word_could = WordCouldUtil.formatter(backgroud='white',
                                     max_words=1000,
                                     max_font_size=40,
                                     stopwords=STOPWORDS,
                                     font_path=FilePath.FONT_PATH,
                                     random_state=16)

article = open(FilePath.ARTICLE_PATH, encoding='utf-8').read()

if __name__ == '__main__':
    text = StopWords.filter(article)
    # show
    Image.show(text, word_could)
    # save
    Image.save(word_could, FilePath.RESULT_PATH)
