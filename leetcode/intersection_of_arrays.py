#
# Create on 5/17/2018
#
# Author: Sylvia
#

"""
349. Intersection of Two Arrays
Given two arrays, write a function to compute their intersection.
"""


class Solution(object):
    @staticmethod
    def intersection(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        res = []
        s = nums1 if len(nums1) < len(nums2) else nums2
        l = nums2 if len(nums1) < len(nums2) else nums1
        for item in s:
            if item in l:
                res.append(item)
        return res


import pytest


class Test:
    @pytest.mark.parametrize('num1, num2, res', [([], [], []),
                                                 ([1, 2, 2, 1], [2, 2], [2])])
    def test(self, num1, num2, res):
        assert Solution.intersection(num1, num2) == res
