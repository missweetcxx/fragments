#
# Create on 2/6/2018
#
# Author: Sylvia
#

"""
Sort
Seven types of sorting.
"""


class Sort(list):
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

    @staticmethod
    def bubble_sort(my_list):
        circle_num = len(my_list) - 1

        for i in range(circle_num):
            for j in range(circle_num - i):
                if my_list[j] > my_list[j + 1]:
                    my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
        return my_list

    @staticmethod
    def selection_sort(my_list):
        for i in range(0, len(my_list) - 1):
            index = i
            for j in range(i + 1, len(my_list)):
                if my_list[index] > my_list[j]:
                    index = j
            my_list[i], my_list[index] = my_list[index], my_list[i]
        return my_list

    @staticmethod
    def insert_sort(my_list):
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
    def insert_sort_2(my_list):
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
    def quick_sort(my_list, start=None, end=None):
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
                Sort.quick_sort(my_list, start, i - 1)
                Sort.quick_sort(my_list, i + 1, end)

        return my_list

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
            left = Sort.merge_sort(my_list[:point])
            right = Sort.merge_sort(my_list[point:])
            return merge(left, right)

        else:
            return my_list

    @staticmethod
    def shell_sort(my_list):
        length = len(my_list)
        step = length // 2
        while step > 0:
            for i in range(step):
                list = [my_list[x] for x in range(i, length, step)]
                list = Sort.insert_sort(list)
                for x in range(len(list)):
                    my_list[x * step + i] = list[x]

            step = step // 2
        return my_list

    @staticmethod
    def shell_sort_2(lists):
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
