#
# Create on 5/17/2018
#
# Author: Sylvia
#

"""
287. Find the Duplicate Number
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one
duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
"""


class Solution(object):
    @staticmethod
    def find_duplicate_a(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = nums[0]
        while i != nums[i]:
            nums[i], i = i, nums[i]
        return i

    @staticmethod
    def find_duplicate_b(nums):
        for num in nums:
            temp = abs(num)
            if nums[temp] < 0:
                return temp
            else:
                nums[temp] *= -1

    @staticmethod
    def find_duplicate_c(nums):
        for i in range(len(nums)):
            while (nums[i] != i) and (nums[i] != nums[nums[i]]):
                nums[i], i = i, nums[i]
            if nums[i] != i and nums[i] == nums[nums[i]]:
                return nums[i]


import copy

import pytest


class Test:
    @pytest.mark.parametrize('nums, expected', [([1, 3, 4, 2, 2], 2),
                                                ([2, 2, 2], 2)])
    def test(self, nums, expected):
        nums_a, nums_b, nums_c = copy.deepcopy(nums), copy.deepcopy(nums), copy.deepcopy(nums)
        assert Solution.find_duplicate_a(nums_a) == expected
        assert Solution.find_duplicate_b(nums_b) == expected
        assert Solution.find_duplicate_c(nums_c) == expected
