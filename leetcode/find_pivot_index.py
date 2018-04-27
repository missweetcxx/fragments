#
# Create on 4/19/2018
#
# Author: Sylvia
#

"""
724. Find Pivot Index
Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the
numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot
index.
"""


class Solution(object):
    def pivotIndex(self, nums):
        # time limit exceeded
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i + 1:]):
                return i
        return -1

    def pivotIndex2(self, nums):
        left, right = 0, sum(nums)
        for index, num in enumerate(nums):
            right -= num
            if left == right:
                return index
            left += num
        return -1


import pytest


class Test:
    @pytest.mark.parametrize('nums, expect', [([1, 7, 3, 6, 5, 6], 3),
                                              ([-1, -1, -1, -1, -1, -1], -1),
                                              ([], -1),
                                              ([-1, 1, 2, 3], -1)])
    def test(self, nums, expect):
        res = Solution()
        assert res.pivotIndex2(nums) is expect
