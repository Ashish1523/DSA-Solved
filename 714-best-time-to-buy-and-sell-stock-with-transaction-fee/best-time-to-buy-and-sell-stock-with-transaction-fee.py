class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n=len(prices)
        # dp=[[-1 for _ in range(2)] for _ in range(n)]
        # def dfs(i,buy):
        #     if i==n:
        #         return 0
        #     if dp[i][buy]!=-1:
        #         return dp[i][buy]
        #     if buy:
        #         dp[i][buy]=max(-prices[i]+dfs(i+1,0),dfs(i+1,1))
        #     else:
        #         dp[i][buy]=max(prices[i]-fee+dfs(i+1,1),dfs(i+1,0))
        #     return dp[i][buy]
        # return dfs(0,1)

        dp=[[0 for _ in range(2)] for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            dp[i][1]=max(-prices[i]+dp[i+1][0],dp[i+1][1])
            dp[i][0]=max(prices[i]-fee+dp[i+1][1],dp[i+1][0])
        return dp[0][1]