class Solution:


    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])

        memo = [[-1] * COLS for _ in range(ROWS)]

        return self.dfs(0, 0, memo, ROWS, COLS, obstacleGrid)
    def dfs(self, i, j, memo, ROWS, COLS, obstacleGrid):
        if i >= ROWS or j >= COLS:
            return 0

        if obstacleGrid[i][j] == 1:
            return 0

        if  i == ROWS-1 and j == COLS-1:
            return 1
        
        if memo[i][j] != -1:
            return memo[i][j]

        memo[i][j] = (
            self.dfs(i + 1, j, memo, ROWS, COLS, obstacleGrid)
            + self.dfs(i, j + 1, memo, ROWS, COLS, obstacleGrid)
        )

        return memo[i][j]