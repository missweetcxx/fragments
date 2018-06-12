#
# Create on 6/7/2018
#
# Author: Sylvia
#

"""
283. Move Zeroes
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the
non-zero elements.
"""


class Solution(object):
    @staticmethod
    def move_zeroes_a(nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1

    @staticmethod
    def move_zeroes_b(nums):
        count = nums.count(0)
        nums[:] = [i for i in nums if i != 0]
        nums += [0] * count


import pytest


class Test:
    @pytest.mark.parametrize('nums, expect', [([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
                                              ([1], [1]),
                                              ([0, 1], [1, 0])])
    def test(self, nums, expect):
        Solution.move_zeroes_a(nums)
        assert nums == expect

        Solution.move_zeroes_b(nums)
        assert nums == expect
