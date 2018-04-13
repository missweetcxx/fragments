#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BubbleSort:
    @staticmethod
    def bubble_sort(my_list):
        circle_num = len(my_list) - 1

        for i in range(circle_num):
            for j in range(circle_num - i):
                if my_list[j] > my_list[j + 1]:
                    my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
        return my_list
