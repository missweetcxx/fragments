#
# Create on 5/11/2018
#
# Author: Sylvia
#

"""
77. Combinations
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
"""
import itertools
import random


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        step_soln, full_soln = [], []
        self._backtrack(n, k, step_soln, full_soln, 1)
        return full_soln

    def _backtrack(self, n, k, step_soln, full_soln, start):
        if len(step_soln) == k:
            full_soln.append(step_soln[:])
        else:
            for i in range(start, n + 1):
                step_soln.append(i)
                self._backtrack(n, k, step_soln, full_soln, i + 1)
                step_soln.pop()

    @staticmethod
    def combine_builtin(n, k):
        return list(itertools.combinations([x for x in range(1, n + 1)], k))


class Test:
    def test(self):
        n = random.randint(1, 10)
        k = random.randint(1, 10)
        s = Solution()
        res = s.combine(n, k)
        assert len(res) == len(Solution.combine_builtin(n, k))
        for item in res:
            assert item in Solution.combine_builtin(n, k)
