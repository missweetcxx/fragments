#
# Create on 5/18/2018
#
# Author: Sylvia
#

"""
728. Self Dividing Numbers

A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
"""


class Solution(object):
    @staticmethod
    def self_dividing_numbers(left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for item in range(left, right + 1):
            if '0' not in str(item):
                flag = True
                for digit in str(item):
                    if item % int(digit) != 0:
                        flag = False
                        break
                if flag:
                    res.append(item)
        return res

    @staticmethod
    def self_dividing_numbers_lt(left, right):
        ret = []
        for i in range(left, right + 1):
            t = i
            while t != 0 and t % 10 != 0 and i % (t % 10) == 0:
                t = t // 10
            if t == 0:
                ret.append(i)
        return ret


import random


class Test:
    def test(self):
        a, b = random.randint(1, 10), random.randint(11, 100)
        assert Solution.self_dividing_numbers(a, b) == Solution.self_dividing_numbers_lt(a, b)
