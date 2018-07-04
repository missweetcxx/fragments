#!/usr/bin/env python
# -*- coding: utf-8 -*-


class InsertSort:
    """
    Insert Sort
    divide list into two lists: sorted one and unsorted one;
    each time insert an element from unsorted list into sorted one at correct position;

    Complexity: O(n^2) in worst case
    Memory: O(1)
    """

    @staticmethod
    def solution(my_list):
        for r in range(1, len(my_list)):
            l = r - 1
            if my_list[r] < my_list[l]:
                temp = my_list[r]
                my_list[r] = my_list[l]
                l = l - 1
                while l >= 0 and my_list[l] > temp:
                    my_list[l + 1] = my_list[l]
                    l = l - 1
                my_list[l + 1] = temp
        return my_list

    @staticmethod
    def solution_2(my_list):
        for r in range(1, len(my_list)):
            l = r - 1
            point = r
            while l >= 0:
                if my_list[l] > my_list[point]:
                    my_list[l], my_list[point] = my_list[point], my_list[l]
                    point = l
                l -= 1
        return my_list

    @staticmethod
    def solution_3(my_list):
        for i in range(len(my_list)):
            for j in range(1, i + 1)[::-1]:
                if my_list[j] < my_list[j - 1]:
                    my_list[j - 1], my_list[j] = my_list[j], my_list[j - 1]
                else:
                    break
        return my_list

    @staticmethod
    def solution_4(my_list):
        for i in range(1, len(my_list)):
            cur = my_list[i]
            j = i - 1
            while j >= 0 and my_list[j] > cur:
                my_list[j + 1] = my_list[j]
                j = j - 1
            my_list[j + 1] = cur
        return my_list

    @staticmethod
    def solution_5(my_list):
        for i in range(1, len(my_list)):
            cur = my_list[i]
            for j in range(0, i):
                if my_list[i] < my_list[j]:
                    my_list = my_list[:i] + my_list[i + 1:]
                    my_list.insert(j, cur)
        return my_list
