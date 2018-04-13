#!/usr/bin/env python
# -*- coding: utf-8 -*-


class SelectionSort:
    """
    Selection Sort
    select one element at a time, compare it to all other element in list;
    the largest/smallest one would be moved to correct position at first,
    then the second largest/smallest one would;
    after n-1 times' pass, the list would be sorted.

    Complexity: O(n^2) in worst case
    Memory: O(1)
    """

    @staticmethod
    def solution(my_list):
        for i in range(0, len(my_list) - 1):
            index = i
            for j in range(i + 1, len(my_list)):
                if my_list[index] > my_list[j]:
                    index = j
            my_list[i], my_list[index] = my_list[index], my_list[i]
        return my_list

    @staticmethod
    def solution_2(my_list):
        for i in range(len(my_list)):
            for j in range(i + 1, len(my_list)):
                if my_list[i] > my_list[j]:
                    my_list[j], my_list[i] = my_list[i], my_list[j]
        return my_list
