import sys
from typing import List

sys.setrecursionlimit(10000)

class Solution:
    def DFS(self, grid: List[List[int]], visited: List[List[bool]], i: int, j: int) -> int:
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return 0
        if visited[i][j] or grid[i][j] == 0:
            return 0
        visited[i][j] = True
        area = 1
        area += self.DFS(grid, visited, i-1, j)
        area += self.DFS(grid, visited, i+1, j)
        area += self.DFS(grid, visited, i, j-1)
        area += self.DFS(grid, visited, i, j+1)
        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not visited[i][j]:
                    area = self.DFS(grid, visited, i, j)
                    max_area = max(max_area, area)
        return max_area