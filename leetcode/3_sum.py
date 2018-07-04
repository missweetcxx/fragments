#
# Create on 6/19/2018
#
# Author: Sylvia
#

"""
15. 3Sum
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets
in the array which gives the sum of zero.
"""


class Solution(object):
    @staticmethod
    def three_sum(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if len(nums) < 3:
            return result
        nums.sort()
        i = 0
        while i < len(nums) - 2:
            l, r = i + 1, len(nums) - 1
            b = nums[i]
            while l < r:
                a, c = nums[l], nums[r]
                if nums[l] + nums[i] + nums[r] == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    while l < r and a == nums[l]:
                        l += 1
                    while l < r and c == nums[r]:
                        r -= 1
                elif nums[l] + nums[i] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1

            while i < len(nums) and b == nums[i]:
                i += 1

        return result


import pytest


class Test:
    @pytest.mark.parametrize('nums, expect',
                             [([-1, 0, 1, 2, -1, -4], [[-1, 0, 1], [-1, -1, 2]]), ([0], [])])
    def test(self, nums, expect):
        res = Solution()
        assert len(expect) == len(res.three_sum(nums))
        for item in res.three_sum(nums):
            assert item in expect
