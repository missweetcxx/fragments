#!/usr/bin/env python
# -*- coding: utf-8 -*-


class MergeSort:
    @staticmethod
    def merge_sort(my_list):
        def merge(left, right):
            left_point, right_point = 0, 0
            result = []
            while left_point < len(left) and right_point < len(right):
                if left[left_point] <= right[right_point]:
                    result.append(left[left_point])
                    left_point += 1
                else:
                    result.append(right[right_point])
                    right_point += 1
            result += left[left_point:]
            result += right[right_point:]

            return result

        if len(my_list) > 1:
            point = len(my_list) // 2
            left = MergeSort.merge_sort(my_list[:point])
            right = MergeSort.merge_sort(my_list[point:])
            return merge(left, right)

        else:
            return my_list
