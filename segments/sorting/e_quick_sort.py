#!/usr/bin/env python
# -*- coding: utf-8 -*-


class QuickSort:
    """
    Quick sort is default sorting algo in many standard libraries,
    as its name implies, it is very fast.
    Divide and conquer algorithm.  The difference between merge sort
    and quick sort is that the partition is not based on length or an
    artificial index, but on a 'pivot'.
    A pivot is an element from the list. The list is partitioned with
    all elements smaller than the pivot on one side and larger than
    the pivot on the other.
    This pivot partition is applied to all sub-lists till the list is sorted.
    There is no exact science behind the pivot, usually the first or last elements
    of the sublist are chosen.
    Complexity: O(NLOGN) on average
        - O(n^2) in worst case
    Stable: No
        - does not preserve relevant ordering
    Memory: O(LOGN)
        - call stack in recursion
    Adaptivity: No
        -  no way to know whether list is already sorted before iterations
           are done
    Discussion:
        - usually preferable to merge sort, better cache performance
    """

    @staticmethod
    def solution(my_list, start=None, end=None):
        start = 0 if start is None else start
        end = len(my_list) - 1 if end is None else end

        if start < end:
            i, j = start, end
            point = i
            while i != j:
                while my_list[j] >= my_list[point] and i < j:
                    j = j - 1
                while my_list[i] <= my_list[point] and i < j:
                    i = i + 1
                my_list[i], my_list[j] = my_list[j], my_list[i]
                if i == j:
                    my_list[i], my_list[point] = my_list[point], my_list[i]
                QuickSort.solution(my_list, start, i - 1)
                QuickSort.solution(my_list, i + 1, end)

        return my_list

    @staticmethod
    def solution_2(input_list):
        def partition(list_to_sort, start, end):
            pivot = list_to_sort[start]
            left = start
            right = end

            # figure out where pivot should go
            while left < right:
                while list_to_sort[left] <= pivot and left < right:
                    left += 1
                while list_to_sort[right] > pivot:
                    right -= 1
                if left < right:
                    # move items around if they are in wrong position relative to pivot value
                    list_to_sort[left], list_to_sort[right] = list_to_sort[right], list_to_sort[left]

            # finally, put pivot in the correct spot
            list_to_sort[start], list_to_sort[right] = list_to_sort[right], list_to_sort[start]

            return right

        def quick_sort_helper(list_to_sort, start, end):
            # if segment only has one element, return
            # also takes care of possibility for invalid input
            if start < end:
                partition_index = partition(list_to_sort, start, end)
                quick_sort_helper(list_to_sort, start, partition_index - 1)
                quick_sort_helper(list_to_sort, partition_index + 1, end)

        quick_sort_helper(input_list, 0, len(input_list) - 1)
        return input_list
