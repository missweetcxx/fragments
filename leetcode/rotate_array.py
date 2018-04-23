#
# Create on 4/23/2018
#
# Author: Sylvia
#

"""
189. Rotate Array
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
"""


class Solution(object):
    def rotate_a(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            temp = nums.pop()
            nums.insert(0, temp)

    def rotate_b(self, nums, k):
        p = k % len(nums)
        temp = nums[len(nums) - p:]
        nums[:] = temp + nums[0:len(nums) - p]


import pytest


class Test:
    @pytest.mark.parametrize('nums, k, expect', [([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4])])
    def test_equal(self, nums, k, expect):
        res = Solution()
        res.rotate_a(nums, k)
        assert nums == expect
