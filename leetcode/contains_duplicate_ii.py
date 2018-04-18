#
# Create on 4/18/2018
#
# Author: Sylvia
#

"""
219. Contains Duplicate II
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such
that nums[i] = nums[j] and the absolute difference between i and j is at most k.
"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict = {}
        for i, v in enumerate(nums):
            if dict.get(v) is not None:
                if i - dict[v] <= k:
                    return True
            dict[v] = i
        return False


import pytest


class Test:
    @pytest.mark.parametrize('nums, k, result', [([1, 2, 1, 3], 2, True),
                                                 ([1, 2, 3, 1, 4], 2, False),
                                                 ([], 0, False)])
    def test(self, nums, k, result):
        res = Solution()
        assert res.containsNearbyDuplicate(nums, k) is result
