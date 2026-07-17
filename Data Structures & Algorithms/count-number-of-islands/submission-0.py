class Solution:
    def DFS(self, grid: List[List[str]], visited: List[List[str]], i: int, j: int):
        visited[i][j] = True
        if i - 1 >= 0 and grid[i-1][j] == "1" and visited[i-1][j] == False:
            self.DFS(grid, visited, i-1, j)
        if i + 1 < len(grid) and grid[i+1][j] == "1" and visited[i+1][j] == False:
            self.DFS(grid, visited, i+1, j)
        if j + 1 < len(grid[0]) and grid[i][j+1] == "1" and visited[i][j+1] == False:
            self.DFS(grid, visited, i, j+1)
        if j - 1 >= 0 and grid[i][j-1] == "1" and visited[i][j-1] == False:
            self.DFS(grid, visited, i, j-1)

        return

    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        result = 0

        for i in range(len(visited)):
            for j in range(len(visited[0])):
                if visited[i][j] == False and grid[i][j] == "1":
                    result+=1
                    self.DFS(grid, visited, i, j)
        
        return result