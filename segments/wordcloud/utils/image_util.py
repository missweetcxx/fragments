#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from wordcloud import ImageColorGenerator

from segments.wordcloud.common.constants import Color


class Image:
    @staticmethod
    def show(text, wc, mask_color=False):
        wc.generate(text)
        if mask_color:
            image_colors = ImageColorGenerator(Color.BACK_COLOR)
            plt.imshow(wc.recolor(color_func=image_colors))
        else:

            plt.imshow(wc)
        plt.axis('off')
        plt.show(wc)

    @staticmethod
    def save(word_cloud, file_path):
        word_cloud.to_file(file_path)
