#
# Create on 4/27/2018
#
# Author: Sylvia
#

"""
540. Single Element in a Sorted Array
Given a sorted array consisting of only integers where every element appears twice except for one element which appears
once.
Find this single element that appears only once.
"""


class Solution(object):
    @staticmethod
    def single_non_duplicate_a(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, h = 0, len(nums) - 1
        while l <= h and int((l + h) // 2) < len(nums) - 1:
            mid = int((l + h) // 2)
            if mid % 2 == 0 and nums[mid] == nums[mid + 1]:
                l = mid + 1
            elif mid % 2 != 0 and nums[mid] == nums[mid - 1]:
                l = mid + 1
            elif nums[mid] not in [nums[mid - 1], nums[mid + 1]]:
                return nums[mid]
            else:
                h = mid - 1
        return nums[l]

    @staticmethod
    def single_non_duplicate_b(nums):
        value = 0
        for item in nums:
            value ^= item
        return value

    @staticmethod
    def single_non_duplicate_c(nums):
        return sum(set(nums)) * 2 - sum(nums)


import pytest


class Test:
    @pytest.mark.parametrize('nums, expect', [([1, 1, 2, 3, 3, 4, 4, 8, 8], 2),
                                              ([3, 3, 7, 7, 10, 11, 11], 10),
                                              ([1, 1, 5], 5)])
    def test_equal(self, nums, expect):
        assert Solution.single_non_duplicate_a(nums) is expect
        assert Solution.single_non_duplicate_b(nums) is expect
        assert Solution.single_non_duplicate_c(nums) is expect
