#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uuid
from random import Random


class RandUtils(object):
    @staticmethod
    def rand_str(prefix='', suffix='', length=8):
        t = ''
        while len(t) < length:
            t += str(uuid.uuid4()).replace('-', '')

        return prefix + t[:length] + suffix

    @staticmethod
    def rand_int(prefix=0, length=8):
        s = str(prefix)
        chars = '0123456789'
        random = Random()
        for i in range(length):
            if i == 0:
                s += chars[random.randint(1, len(chars) - 1)]
            else:
                s += chars[random.randint(0, len(chars) - 1)]

        return int(s)

    @staticmethod
    def rand_cn_str(prefix='', suffix='', length=3):
        s = prefix
        chars = ['筠', '柔', '竹', '霭', '凝', '晓', '欢', '霄', '枫', '芸',
                 '菲', '寒', '伊', '亚', '宜', '可', '姬', '舒', '影', '荔',
                 '枝', '思', '丽', '秀', '娟', '英', '华', '慧', '巧', '美',
                 '雍', '怀', '北', '耘', '玄', '霁', '澜', '馨', '卉', '闽',
                 '令', '异', '淞', '财', '领', '律', '墨', '垣', '深', '陵']
        random = Random()
        for i in range(length):
            s += chars[random.randint(0, len(chars) - 1)]
        return s + suffix
