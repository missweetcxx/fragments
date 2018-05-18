#
# Create on 5/17/2018
#
# Author: Sylvia
#

"""
645. Set Mismatch
The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the
set got duplicated to another number in the set, which results in repetition of one number and loss of another number.
"""


class Solution(object):
    @staticmethod
    def find_error_nums(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n_s = list(set(nums))
        n_e = [x for x in range(1, len(nums) + 1)]
        d = sum(nums) - sum(n_s)
        m = sum(n_e) - sum(n_s)

        return [d, m]


class Test:
    def test(self):
        assert Solution.find_error_nums([1, 2, 2, 4]) == [2, 3]
