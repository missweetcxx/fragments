#
# Create on 5/2/2018
#
# Author: Sylvia
#

"""
695. Max Area of Island
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected
4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
"""


class Solution(object):
    def max_area_of_island(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if not grid: return

        rows, cols = len(grid), len(grid[0])
        max_area = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.dfs(grid, i, j, 1))

        res =  max(0, max_area)
        return res

    def dfs(self, grid, i, j, count):

        grid[i][j] = 0

        for m, n in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= m < len(grid) and 0 <= n < len(grid[0]) and grid[m][n] == 1:
                count = 1 + self.dfs(grid, m, n, count)

        return count


import pytest


class Test:
    @pytest.mark.parametrize('grid, expect', [([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                                                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                                                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                                                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]], 6),
                                              ([[0, 0, 0, 0, 0, 0, 0, 0]], 0)])
    def test(self, grid, expect):
        res = Solution()
        assert res.max_area_of_island(grid) == expect
