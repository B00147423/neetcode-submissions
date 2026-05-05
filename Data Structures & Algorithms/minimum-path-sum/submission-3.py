class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:


        ROWS = len(grid)
        COLS = len(grid[0])

        memo = [[-1] * COLS for _ in range(ROWS)]

    
        def dfs(i, j):
            if i >= ROWS or j >= COLS:
                return float("inf")
                
            if  i == ROWS-1 and j == COLS-1:
                return grid[i][j]

            if memo[i][j] != -1:
                return memo[i][j]
            
            memo[i][j] = grid[i][j] + min(dfs(i+1, j), dfs(i, j+1))


            return memo[i][j]
        return dfs(0, 0)

