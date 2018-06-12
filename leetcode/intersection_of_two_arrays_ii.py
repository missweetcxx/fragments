#
# Create on 6/12/2018
#
# Author: Sylvia
#

"""
350. Intersection of Two Arrays II

Given two arrays, write a function to compute their intersection.
"""


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        section = list()
        if len(nums1) <= len(nums2):
            for d in nums1:
                if d in nums2:
                    nums2.remove(d)
                    section.append(d)
        else:
            for d in nums2:
                if d in nums1:
                    nums1.remove(d)
                    section.append(d)
        return section
