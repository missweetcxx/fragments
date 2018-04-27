#
# Create on 4/27/2018
#
# Author: Sylvia
#

"""
278. First Bad Version
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of
your product fails the quality check. Since each version is developed based on the previous version, all the versions
after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following
ones to be bad.
"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    pass

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, h = 0, n - 1
        while l <= h:
            mid = int((l + h) // 2)
            if isBadVersion(mid):
                h = mid -1
            else:
                l = mid + 1
        return l
