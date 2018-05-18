#
# Create on 5/18/2018
#
# Author: Sylvia
#

"""
507. Perfect Number
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
"""
from math import sqrt


class Solution(object):
    @staticmethod
    def check_perfect_number(num):
        """
        :type num: int
        :rtype: bool
        """
        if abs(num) in [0, 1]: return False
        sqr = int(sqrt(abs(num)))
        divisors = []
        s = 0
        for i in range(1, sqr + 1):
            if num % i == 0:
                divisors.append(i)
        for item in divisors:
            s += item + num // item
        return s - num == num


import random


class Test:
    @staticmethod
    def wiki(num):
        if num == 1:
            return False

        if num % 10 == 6 or num % 10 == 8:
            bitwise = bin(num)[2:]
            split_index = len(bitwise) // 2 + 1

            if bitwise[:split_index].count('0') == 0 and bitwise[split_index:].count('1') == 0:
                if bitwise[:split_index].count('1') - bitwise[split_index:].count('0') == 1:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def test(self):
        num = random.randint(0, 1000)
        expected = Test.wiki(num)
        assert Solution.check_perfect_number(num) == expected
