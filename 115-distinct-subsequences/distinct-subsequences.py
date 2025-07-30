class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m=len(s)
        n=len(t)
        dp=[[-1 for _ in range(n+1)] for _ in range(m+1)]
        def dfs(i,j):
            if j==0:
                return 1
            if i==0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if s[i-1]==t[j-1]:
                dp[i][j]=dfs(i-1,j-1)+dfs(i-1,j)
                return dp[i][j]
            dp[i][j]=dfs(i-1,j)
            return dp[i][j]
        
        return dfs(m,n)