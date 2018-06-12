#
# Create on 6/7/2018
#
# Author: Sylvia
#

"""
383. Ransom Note
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function
that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.
"""


class Solution(object):
    @staticmethod
    def can_construct(ransom_note, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransom, magazine = list(ransom_note), list(magazine)
        for char in ransom:
            if char not in magazine:
                return False
            else:
                magazine.remove(char)
        return True


import pytest


class Test:
    @pytest.mark.parametrize('ransom_note, magazine, expect', [('a', 'b', False),
                                                               ('aa', 'ab', False),
                                                               ('aa', 'aab', True),
                                                               ('red', 'adeser', True)])
    def test(self, ransom_note, magazine, expect):
        assert Solution.can_construct(ransom_note, magazine) is expect
