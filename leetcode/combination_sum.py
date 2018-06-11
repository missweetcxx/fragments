#
# Create on 5/14/2018
#
# Author: Sylvia
#

"""
39. Combination Sum
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique
combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.full_soln = []
        self.helper(sorted(candidates), target, [], 0)
        return self.full_soln

    def helper(self, candidates, target, step_soln, index):
        exceed = False
        for i in range(index, len(candidates)):
            if exceed:
                break
            step_soln.append(candidates[i])
            if target - candidates[i] > 0:
                self.helper(candidates, target - candidates[i], step_soln, i)
            elif target - candidates[i] == 0:
                self.full_soln.append(list(step_soln))
                exceed = True
            else:
                exceed = True
            step_soln.pop()
        return


class Test:
    def test(self):
        candidates = [2, 3, 6, 7]
        target = 7
        s = Solution()
        res = s.combinationSum(candidates, target)
        assert [2, 2, 3] in res
        assert [7] in res
        assert len(res) == 2
