class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        memo=[0 for _ in range(n)]
        # memo[0]=grid[0][0]

        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    memo[j]=grid[0][0]
                elif i==0:
                    memo[j]=memo[j-1]+grid[i][j]
                elif j==0:
                    memo[j]=memo[j]+grid[i][j]
                else:
                    memo[j]=min(memo[j],memo[j-1])+grid[i][j]
        return memo[n-1]