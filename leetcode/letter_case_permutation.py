#
# Create on 4/23/2018
#
# Author: Sylvia
#

"""
784. Letter Case Permutation
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.
Return a list of all possible strings we could create.
"""


class Solution(object):
    @staticmethod
    def letter_case_permutation_a(S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = ['']
        for char in S:
            if char.isalpha():
                res = [x + y for x in res for y in [char.upper(), char.lower()]]
            else:
                res = [x + char for x in res]
        return res

    @staticmethod
    def letter_case_permutation_b(S):
        res = ['']
        for char in S:
            if char.isalpha():
                temp = []
                for i in range(len(res)):
                    temp.append(res[i] + char.upper())
                    temp.append(res[i] + char.lower())
                res = temp
            else:
                for i in range(len(res)):
                    res[i] = res[i] + char
        return res


class Test:
    def test(self):
        S = 'x1y2a'
        res = Solution.letter_case_permutation_a(S)
        assert len(res) is 8
        for i in ['X1Y2A', 'X1Y2a', 'X1y2A', 'X1y2a', 'x1Y2A', 'x1Y2a', 'x1y2A', 'x1y2a']:
            assert i in res
