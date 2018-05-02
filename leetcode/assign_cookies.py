#
# Create on 4/28/2018
#
# Author: Sylvia
#

"""
455. Assign Cookies
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most
one cookie. Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be content
with; and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i, and the child i will be
content. Your goal is to maximize the number of your content children and output the maximum number.
"""


class Solution(object):
    @staticmethod
    def find_content_children(g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g, s = sorted(g), sorted(s)
        g_index, s_index = 0, 0
        while g_index < len(g) and s_index < len(s):
            if g[g_index] <= s[s_index]:
                g_index += 1
            s_index += 1
        return g_index


class Test:
    def test(self):
        assert Solution.find_content_children([1, 2, 3], [1, 1]) is 1
        assert Solution.find_content_children([1, 2], [1, 2, 3]) is 2
