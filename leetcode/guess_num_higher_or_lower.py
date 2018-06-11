#
# Create on 6/8/2018
#
# Author: Sylvia
#

"""
374. Guess Number Higher or Lower

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):
"""


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0

import random


class Prepare:
    def __init__(self, n):
        self.n = n
        self.pick = random.randint(0, n)
        print('pick is {}'.format(self.pick))

    def guess(self, num):
        if num > self.pick:
            return 1
        if num < self.pick:
            return -1
        else:
            return 0


class Solution(object):
    @staticmethod
    def guess_number_a(n):
        """
        :type n: int
        :rtype: int
        """
        pre = Prepare(n)
        num = n //2
        guess = pre.guess(num)
        l, h = 0, n
        while guess != 0:
            if guess == 1:
                h = num - 1
            else:
                l = num + 1
            num = (l+h) //2
            guess = pre.guess(num)
        return num

    @staticmethod
    def guess_number_b(n):
        pre = Prepare(n)

        def binary_search(start, end):
            if pre.guess((end-start)//2+start) == 0:
                return (end-start)//2 +start
            elif pre.guess((end-start)//2+start) == 1:
                return binary_search((end-start)//2+start+1, end)
            else:
                return binary_search(start, (end-start)//2 + start-1)

        return binary_search(0, n)
