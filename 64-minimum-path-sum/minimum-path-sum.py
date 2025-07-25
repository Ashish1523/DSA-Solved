class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        memo=[[0 for i in range(n)] for _ in range(m)]
        memo[0][0]=grid[0][0]

        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue
                left=memo[i][j-1] if j>0 else float('inf')
                right=memo[i-1][j] if i>0 else float('inf')
                memo[i][j]=min(left,right)+grid[i][j]
        return memo[m-1][n-1]