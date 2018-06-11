#
# Create on 6/8/2018
#
# Author: Sylvia
#

"""
520. Detect Capital

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

1. All letters in this word are capitals, like "USA".
2. All letters in this word are not capitals, like "leetcode".
3. Only the first letter in this word is capital if it has more than one letter, like "Google".
"""


class Solution(object):
    @staticmethod
    def detect_capital_use_a(word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) > 1:
            if word[0].isupper() and word[1].isupper():
                for char in word[1:]:
                    if char.islower():
                        return False
            if word[0].isupper() and word[1].islower():
                for char in word[1:]:
                    if char.isupper():
                        return False
            if word[0].islower():
                for char in word[1:]:
                    if char.isupper():
                        return False
        if len(word) == 0:
            return False
        return True

    @staticmethod
    def detect_capital_use_b(word):
        if len(word) > 0:
            return word.lower() == word or word.upper() == word or word.lower().capitalize() == word
        return False


import pytest


class Test:
    @pytest.mark.parametrize('word, expect', [('USA', True), ('Detect', True),
                                              ('FRog', False), ('A', True),
                                              ('capital', True), ('', False)])
    def test(self, word, expect):
        assert Solution.detect_capital_use_a(word) is expect
        assert Solution.detect_capital_use_b(word) is expect
