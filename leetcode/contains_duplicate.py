#
# Create on 4/17/2018
#
# Author: Sylvia
#

"""
217. Contains Duplicate
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value
appears at least twice in the array, and it should return false if every element is distinct.
"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_set = set(nums)
        return len(nums) == len(nums_set)


class Test:
    def test_true(self):
        p = [1, 3, 12, 4, 8]
        res = Solution()
        assert res.containsDuplicate(p) is True

    def test_false(self):
        p = [1, 3, 1, 5, 2]
        res = Solution()
        assert res.containsDuplicate(p) is False
