#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from wordcloud import ImageColorGenerator

from segments.wordcloud.common.constants import Color


class Image:
    @staticmethod
    def show(text, word_cloud, mask_color=False):
        word_cloud.generate(text)
        if mask_color:
            image_colors = ImageColorGenerator(Color.BACK_COLOR)
            plt.imshow(word_cloud.recolor(color_func=image_colors))
        else:

            plt.imshow(word_cloud)
        plt.axis('off')
        plt.show(word_cloud)

    @staticmethod
    def save(word_cloud, file_path):
        word_cloud.to_file(file_path)
