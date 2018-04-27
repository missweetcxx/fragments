#
# Create on 4/18/2018
#
# Author: Sylvia
#

"""
697. Degree of an Array
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of
any one of its elements.

Your task is to find the smallest possible length of a (contiguous) sub-array of nums, that has the same degree as nums.
"""

import collections


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first, last = {}, {}
        for i, v in enumerate(nums):
            first.setdefault(v, i)
            last[v] = i
        c = collections.Counter(nums)
        degree = max(c.values())
        res_list = []
        for v in c.keys():
            if c[v] == degree:
                res_list.append(last[v] - first[v] + 1)
        return min(res_list)


import pytest


class Test:
    @pytest.mark.parametrize('nums, expect', [([1, 2, 2, 3, 1], 2), ([1, 2, 2, 3, 1, 4, 2], 6)])
    def test(self, nums, expect):
        res = Solution()
        assert res.findShortestSubArray(nums) is expect
