"""
200. Number of Islands
Medium

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.
"""
from types import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        cnt = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    cnt += 1
                    self.visitAdjacent(i,j,grid,cnt)        
        return cnt
        
    def visitAdjacent(self, i, j, grid, cnt):
        n = len(grid)
        m = len(grid[0])
        
        if 0 <= i < n and 0 <= j < m and grid[i][j] == "1":
            grid[i][j] = cnt
            self.visitAdjacent(i,j+1,grid,cnt)
            self.visitAdjacent(i,j-1,grid,cnt)
            self.visitAdjacent(i-1,j,grid,cnt)
            self.visitAdjacent(i+1,j,grid,cnt)
        