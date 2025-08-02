class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[-1 for _ in range(2)] for _ in range(n)]
        # print(dp)
        def dfs(i,buy):
            if i>=n:
                return 0
            print(i,buy)
            if dp[i][buy]!=-1:
                return dp[i][buy]
            if buy:
                dp[i][buy]=max(-prices[i]+dfs(i+1,0),dfs(i+1,1))
            else:
                dp[i][buy]=max(prices[i]+dfs(i+2,1),dfs(i+1,0))
            return dp[i][buy]
        return dfs(0,1)
        # return 0