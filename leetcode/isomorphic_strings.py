#
# Create on 4/12/2018
#
# Author: Sylvia
#

"""
205. Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        else:
            record_a, record_b = dict(), dict()
            for i in range(len(s)):
                point_s = s[i]
                point_t = t[i]
                if record_a.get(point_s):
                    if record_a[point_s] != point_t:
                        return False
                else:
                    record_a[point_s] = point_t
                if record_b.get(point_t):
                    if record_b[point_t] != point_s:
                        return False
                else:
                    record_b[point_t] = point_s
            return True

    def isIsomorphic1(self, s, t):
        d1, d2 = {}, {}
        for i, val in enumerate(s):
            d1[val] = d1.get(val, []) + [i]
        for i, val in enumerate(t):
            d2[val] = d2.get(val, []) + [i]
        return sorted(d1.values()) == sorted(d2.values())


s = Solution()
res = s.isIsomorphic1('title', 'paper')
print(res)
