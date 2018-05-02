#
# Create on 5/2/2018
#
# Author: Sylvia
#

"""
392. Is Subsequence
Given a string s and a string t, check if s is subsequence of t.
"""


class Solution(object):
    @staticmethod
    def is_subsequence(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) > len(t):
            return False
        index = 0
        for char in s:
            if index == len(t) and char != t[-1]:
                return False
            elif char not in t:
                return False
            index = t.index(char) + 1
            t = t[index:]
        return True


import random


class Test:
    ch = 'abcdefghijklmnopqrstuvwxyz'

    def test_true(self):
        length = random.randint(10, 20)
        s_index = set()
        t = ''.join([random.choice(Test.ch) for i in range(length)])
        for i in range(random.randint(0, length - 9)):
            s_index.add(random.randint(0, length - 1))
        s = ''.join(list(map(lambda x: t[x], sorted(list(s_index)))))

        res = Solution()
        assert res.is_subsequence(s, t) is True

    def test_false(self):
        t = ''.join([random.choice(Test.ch) for i in range(10)])
        s = ''.join([random.choice(Test.ch) for i in range(5)])

        res = Solution()
        assert res.is_subsequence(s, t) is False
