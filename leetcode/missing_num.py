#
# Create on 5/17/2018
#
# Author: Sylvia
#

"""
268. Missing Number
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
"""


class Solution(object):
    @staticmethod
    def missing_number(nums):
        # """
        # :type nums: List[int]
        # :rtype: int
        # """
        max_num = max(nums)
        sum_all = max_num * (max_num + 1) / 2
        sum_num = sum(nums)
        if sum_num == sum_all:
            return 0 if max_num == len(nums) else max_num + 1
        return sum_all - sum_num


import pytest


class Test:
    @pytest.mark.parametrize('nums, expect', [([0], 1),
                                              ([1], 0),
                                              ([0, 1], 2),
                                              ([2, 1], 0),
                                              ([0, 1, 3], 2)])
    def test(self, nums, expect):
        assert Solution.missing_number(nums) == expect
