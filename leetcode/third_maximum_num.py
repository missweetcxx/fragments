#
# Create on 6/11/2018
#
# Author: Sylvia
#

"""
414. Third Maximum Number

Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the
maximum number. The time complexity must be in O(n).
"""
import sys


class Solution(object):
    @staticmethod
    def third_max_a(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = -sys.maxsize - 1
        max2 = -sys.maxsize - 1
        max3 = -sys.maxsize - 1
        nums = list(set(nums))
        for i in range(len(nums)):
            if nums[i] > max1:
                max3 = max2
                max2 = max1
                max1 = nums[i]

            elif nums[i] > max2:
                max3 = max2
                max2 = nums[i]

            elif nums[i] > max3:
                max3 = nums[i]
        if max3 != (-sys.maxsize - 1):
            return max3
        else:
            return max1

    @staticmethod
    def third_max_b(nums):
        sorted_list = list(set(nums))
        sorted_list.sort()
        if len(sorted_list) > 2:
            return int(sorted_list[len(sorted_list) - 3])
        else:
            return int(sorted_list[-1])

res = Solution.third_max_a([1,2])
print(res)