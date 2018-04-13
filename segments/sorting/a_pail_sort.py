#!/usr/bin/env python
# -*- coding: utf-8 -*-


class PailSort:
    @staticmethod
    def pail_sort(my_list):
        max_num, min_num = max(my_list), min(my_list)
        pail_list = [[i, 0] for i in range(min_num, max_num + 1)]

        for i in my_list:
            for pail in pail_list:
                pail[1] += 1 if pail[0] == i else 0
        result = list()

        for pail in pail_list:
            for t in range(0, pail[1]):
                result.append(pail[0])
        return result
