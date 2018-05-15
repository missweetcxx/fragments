#
# Create on 5/8/2018
#
# Author: Sylvia
#

"""
200. Number of Islands
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and
is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.
"""

import collections


class Solution(object):
    def __init__(self, grid):
        self.grid = grid

    def is_valid(self, r, c):
        m, n = len(self.grid), len(self.grid[0])
        if r < 0 or c < 0 or r >= m or c >= n:
            return False
        return True

    def num_islands_dfs(self):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not self.grid or not self.grid[0]:
            return 0

        m, n = len(self.grid), len(self.grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if self.grid[i][j] == '1':
                    self.dfs(i, j)
                    count += 1
        return count

    def dfs(self, r, c):
        self.grid[r][c] = '0'
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for d in directions:
            nr, nc = r + d[0], c + d[1]
            if self.is_valid(nr, nc) and self.grid[nr][nc] == '1':
                self.dfs(nr, nc)

    def num_islands_bfs(self):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not self.grid or not self.grid[0]:
            return 0

        m, n = len(self.grid), len(self.grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if self.grid[i][j] == '1':
                    self.bfs(i, j)
                    count += 1
        return count

    def bfs(self, r, c):
        queue = collections.deque()
        queue.append((r, c))
        self.grid[r][c] = '0'
        while queue:
            directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            r, c = queue.popleft()
            for d in directions:
                nr, nc = r + d[0], c + d[1]
                if self.is_valid(nr, nc) and self.grid[nr][nc] == '1':
                    queue.append((nr, nc))
                    self.grid[nr][nc] = '0'


import copy


class Test:
    def test(self):
        grid = [['1', '1', '0', '1', '0'],
                ['1', '1', '0', '1', '0'],
                ['1', '1', '0', '0', '0'],
                ['0', '0', '0', '0', '0']]
        grid_dfs = copy.deepcopy(grid)
        grid_bfs = copy.deepcopy(grid)
        res_dfs = Solution(grid_dfs)
        res_bfs = Solution(grid_bfs)
        assert res_dfs.num_islands_dfs() == res_bfs.num_islands_bfs() == 2
