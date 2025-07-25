class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        dp=matrix
        for i in range(n-2,-1,-1):
            for j in range(n):
                d_l=dp[i+1][j-1] if 0<j else float('inf')
                d_r=dp[i+1][j+1] if j<n-1 else float('inf')
                bottom=dp[i+1][j]
                dp[i][j]=min(d_l,d_r,bottom)+matrix[i][j]
        return min(dp[0])