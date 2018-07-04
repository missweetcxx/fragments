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


rr = MergeSort.merge_sort([2, 3, 1, 4, 2, 4, 5])
print(rr)


class Sort:
    def mergesort(self, alist):
        if len(alist) <= 1:
            return alist
        mid = len(alist) // 2
        left = self.mergesort(alist[:mid])
        right = self.mergesort(alist[mid:])
        return Sort._merge_sorted_array(left, right)

    @staticmethod
    def _merge_sorted_array(A, B):
        sorted_array = []
        l = 0
        r = 0
        while l < len(A) and r < len(B):
            if A[l] < B[r]:
                sorted_array.append(A[l])
                l += 1
            else:
                sorted_array.append(B[r])
                r += 1
        sorted_array += A[l:]
        sorted_array += B[r:]
        return sorted_array
