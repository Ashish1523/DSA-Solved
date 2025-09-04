class Solution:
    def numDecodings(self, s: str) -> int:
        # n=len(s)
        # dp=[0]*n
        # def dfs(i):
        #     if i==n:
        #         return 1
        #     if s[i]=="0":
        #         return 0
        #     if dp[i]:
        #         return dp[i]
            
        #     ways=dfs(i+1)

        #     if i+1<n and 10<=int(s[i]+s[i+1])<=26:
        #         ways+=dfs(i+2)
        #     dp[i]=ways
        #     return ways
        # ans=dfs(0)
        # return ans

        n=len(s)
        if n==0 or s[0]=="0":
            return 0
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1

        for i in range(2,n+1):
            if s[i-1]!="0":
                dp[i]+=dp[i-1]
            
            no=int(s[i-2]+s[i-1])
            if 10<=no<=26:
                dp[i]+=dp[i-2]
        return dp[n]
        
