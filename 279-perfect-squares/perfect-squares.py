class Solution:
    def numSquares(self, n: int) -> int:
        def squares(n):
            k=int(n**0.5)+1
            ans=[]
            for i in range(1,k):
                ans.append(i**2)
            return ans
        square=squares(n)
        square.sort(reverse=True)
        dp=[[-1]*(n+1) for _ in range(len(square))]
        def dfs(i,sum1):
            if sum1==n:
                return 0
            if i>=len(square) or sum1>n:
                return float('inf')
            if dp[i][sum1]!=-1:
                return dp[i][sum1]
            take=1+dfs(i,sum1+square[i])
            notTake=dfs(i+1,sum1)
            dp[i][sum1]=min(take,notTake)
            return dp[i][sum1]
        return dfs(0,0)