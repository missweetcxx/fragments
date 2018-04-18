#
# Create on 4/18/2018
#
# Author: Sylvia
#

"""
53. Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and
return its sum.
"""


class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if not A:
            return 0

        cur_sum = max_sum = A[0]
        for num in A[1:]:
            cur_sum = max(num, cur_sum + num)
            max_sum = max(max_sum, cur_sum)

        return max_sum


import pytest


class Test:
    @pytest.mark.parametrize('array, expect', [([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6)])
    def test(self, array, expect):
        res = Solution()
        assert res.maxSubArray(array) is expect
