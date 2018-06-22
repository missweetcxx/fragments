#
# Create on 6/14/2018
#
# Author: Sylvia
#

"""
405. Convert a Number to Hexadecimal
Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is
used.
"""


class Solution(object):
    def to_hex(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = []
        dic = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}
        if num == 0:
            return "0"
        if num < 0:
            num = num + 2**32

        while num > 0:
            digit = num % 16
            num = (num - digit) // 16
            if 9 < digit < 16:
                digit = dic[digit]
            else:
                digit = str(digit)
            ans.append(digit)
        return "".join(ans[::-1])


import pytest


class Test:
    @pytest.mark.parametrize('num, hex', [(0, '0'), (-1, 'ffffffff'),
                                          (26, '1a'), (33, '21')])
    def test(self, num, hex):
        res = Solution()
        assert res.to_hex(num) == hex
