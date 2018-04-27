#
# Create on 4/26/2018
#
# Author: Sylvia
#

"""
744. Find Smallest Letter Greater Than Target
Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the
smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.
"""


class Solution(object):
    @staticmethod
    def next_greatest_letter(letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if target > letters[-1] or target < letters[0]:
            return letters[0]
        l, h = 0, len(letters) - 1
        while l <= h:
            mid = int((l + h) // 2)
            if letters[mid] <= target:
                l = mid + 1
            else:
                h = mid - 1

        return letters[l] if l < len(letters) else letters[0]


import pytest


class Test:
    @pytest.mark.parametrize('letters, target, expect', [(["c", "f", "j"], "j", "c"),
                                                         (["c", "f", "j"], "d", "f"),
                                                         (["c", "f", "j"], "c", "f")])
    def test(self, letters, target, expect):
        assert Solution.next_greatest_letter(letters, target) is expect
