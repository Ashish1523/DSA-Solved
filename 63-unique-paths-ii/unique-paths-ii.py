class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        if obstacleGrid[0][0]==1:
            return 0
        memo=[[1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue
                if obstacleGrid[i][j]==1:
                    memo[i][j]=0
                    continue
                memo[i][j]=memo[i-1][j] if i-1>=0 else 0
                memo[i][j]+=memo[i][j-1] if j-1>=0 else 0
        # print(memo)
        return memo[m-1][n-1]