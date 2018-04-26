#
# Create on 4/23/2018
#
# Author: Sylvia
#

"""
78. Subsets
Given a set of distinct integers, nums, return all possible subsets (the power set).
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            res += [item + [num] for item in res]
        return res


class Test:
    def test_true(self):
        nums = [1, 2, 3]
        expect = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        res = Solution()
        res_arr = res.subsets(nums)
        assert len(res_arr) == len(expect)
        for i in expect:
            assert i in res_arr
