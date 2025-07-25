class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        dp=[]
        for i in range(n):
            dp.append(matrix[n-1][i])
        for i in range(n-2,-1,-1):
            curr=[0]*n
            for j in range(n):
                d_l=dp[j-1] if 0<j else float('inf')
                d_r=dp[j+1] if j<n-1 else float('inf')
                bottom=dp[j]
                curr[j]=min(d_l,d_r,bottom)+matrix[i][j]
            dp=curr
        return min(dp)