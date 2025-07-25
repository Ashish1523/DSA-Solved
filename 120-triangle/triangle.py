class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        # def dfs(i,j):
        #     if i>n-1 or j>n:
        #         return 0
        #     left=dfs(i+1,j)
        #     right=dfs(i+1,j+1)
        #     return min(left,right)+triangle[i][j]
        # return dfs(0,0)
        dp=triangle
        for i in range(n-2,-1,-1):
            for j in range(len(triangle[i])):
                bottom=dp[i+1][j]
                bottom_left=dp[i+1][j+1]
                dp[i][j]=min(bottom,bottom_left)+triangle[i][j]
        return dp[0][0]