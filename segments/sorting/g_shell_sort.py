#!/usr/bin/env python
# -*- coding: utf-8 -*-
from segments.sorting.d_insert_sort import InsertSort


class ShellSort:
    @staticmethod
    def solution(my_list):
        length = len(my_list)
        step = length // 2
        while step > 0:
            for i in range(step):
                list = [my_list[x] for x in range(i, length, step)]
                list = InsertSort.solution(list)
                for x in range(len(list)):
                    my_list[x * step + i] = list[x]

            step = step // 2
        return my_list

    @staticmethod
    def solution_2(lists):
        length = len(lists)
        step = length // 2
        while step > 0:
            for i in range(0, step):
                j = i + step
                while j < length:
                    k = j - step
                    key = lists[j]
                    while k >= 0:
                        if lists[k] > key:
                            lists[k + step] = lists[k]
                            lists[k] = key
                        k -= step
                    j += step
            step //= 2
        return lists
