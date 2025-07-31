class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        n=len(prices)
        dp=[[[-1 for _ in range(2+1)] for _ in range(2)] for _ in range(n)]
        # print(dp)
        def dfs(ind,buy,cap):
            maxProfit=0
            if cap==0:
                return 0
            if ind==n:
                return 0
            if dp[ind][buy][cap]!=-1:
                return dp[ind][buy][cap]
            if buy:
                dp[ind][buy][cap]=max(-prices[ind]+dfs(ind+1,0,cap),dfs(ind+1,1,cap))
                maxProfit=dp[ind][buy][cap]
            else:
                dp[ind][buy][cap]=max(prices[ind]+dfs(ind+1,1,cap-1),dfs(ind+1,0,cap))
                maxProfit=dp[ind][buy][cap]
            return maxProfit
        
        return dfs(0,1,2)