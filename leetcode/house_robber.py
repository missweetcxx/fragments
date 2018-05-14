#
# Create on 5/10/2018
#
# Author: Sylvia
#

"""
198. House Robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it
will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
money you can rob tonight without alerting the police.
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        else:
            dp = dict()
            dp[0] = nums[0]
            dp[1] = nums[1]
            dp[2] = nums[2] + nums[0]
            for i in range(3, n):
                dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i]
            return max(dp[n - 1], dp[n - 2])


import pytest


class Test:
    @pytest.mark.parametrize('nums, amount', [([2, 7, 9, 3, 1, 1, 2, 4, 1], 16),
                                             ([1, 2, 3, 1], 4)])
    def test(self, nums, amount):
        res = Solution()
        assert res.rob(nums) == amount
