class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        n=len(prices)
        dp=[[-1 for _ in range(2)] for _ in range(n)]
        def dfs(ind,buy):
            nonlocal maxProfit
            if ind==n:
                return 0
            if dp[ind][buy]!=-1:
                return dp[ind][buy]
            if buy:
                dp[ind][buy]=max(-prices[ind]+dfs(ind+1,0),dfs(ind+1,1))
                maxProfit=dp[ind][buy]
            else:
                dp[ind][buy]=max(prices[ind]+dfs(ind+1,1),dfs(ind+1,0))
                maxProfit=dp[ind][buy]
            return maxProfit
        
        return dfs(0,1)

            