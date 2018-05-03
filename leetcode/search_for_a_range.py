#
# Create on 4/17/2018
#
# Author: Sylvia
#

"""
34. Search for a Range
Given an array of integers nums sorted in ascending order, find starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).
"""


class Solution(object):
    @staticmethod
    def search_range(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0 or target < nums[0] or target > nums[len(nums) - 1] or target not in nums: return [-1, -1]
        start = Solution.binary_search(nums, target)
        last = Solution.binary_search(nums, target + 1) - 1
        return [start, last]

    @staticmethod
    def binary_search(nums, target):
        l, h = 0, len(nums) - 1
        while l <= h:
            mid = int((l + h) // 2)
            if nums[mid] >= target:
                h = mid - 1
            else:
                l = mid + 1
        return l


class Test:
    def test(self):
        assert Solution.search_range([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
        assert Solution.search_range([1, 2, 2, 2, 2, 2, 5], 2) == [1, 5]
