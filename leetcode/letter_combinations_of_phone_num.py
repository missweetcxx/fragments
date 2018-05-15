#
# Create on 5/8/2018
#
# Author: Sylvia
#

"""
17. Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could
represent.
"""
import itertools


class Solution(object):
    def __init__(self):
        self.mapper = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    def letter_combinations_a(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        pad_list = [x for x in digits]
        char_list = [self.mapper[int(x)] for x in pad_list]
        return [''.join(x) for x in list(itertools.product(*char_list)) if len(x) > 0]

    def helper(self, digits, cur_idx, tmp, result):
        if cur_idx == len(digits) - 1:
            result.append(tmp)
            return

        num = digits[cur_idx + 1]
        for char in self.mapper[int(num)]:
            self.helper(digits, cur_idx + 1, tmp + char, result)

    def letter_combinations_b(self, digits):
        if digits == '':
            return []
        res = []
        self.helper(digits, -1, '', res)
        return res


class Test:
    def test(self):
        res = Solution()
        assert res.letter_combinations_a('234') == res.letter_combinations_b('234')
        assert res.letter_combinations_a('') == res.letter_combinations_b('') == []
