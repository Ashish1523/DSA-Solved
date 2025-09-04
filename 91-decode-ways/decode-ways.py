class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        dp=[0]*n
        def dfs(i):
            if i==n:
                return 1
            if s[i]=="0":
                return 0
            if dp[i]:
                return dp[i]
            
            ways=dfs(i+1)

            if i+1<n and 10<=int(s[i]+s[i+1])<=26:
                ways+=dfs(i+2)
            dp[i]=ways
            return ways
        return dfs(0)
