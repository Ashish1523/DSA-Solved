class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)

        # dp=[[-1 for _ in range((k*2)+1)]for _ in range(n+1)]
        # def dfs(ind,trans):
        #     maxProfit=0
        #     if trans==0:
        #         return 0
        #     if ind==n:
        #         return 0
        #     if dp[ind][trans]!=-1:
        #         return dp[ind][trans]
        #     if (trans%2==0):
        #         dp[ind][trans]=max(-prices[ind]+dfs(ind+1,trans-1),dfs(ind+1,trans))
        #         maxProfit=dp[ind][trans]
        #     else:
        #         dp[ind][trans]=max(prices[ind]+dfs(ind+1,trans-1),dfs(ind+1,trans))
        #         maxProfit=dp[ind][trans]
        #     return maxProfit
        
        # return dfs(0,k*2)

        dp=[[0 for _ in range((k*2)+1)] for _ in range(n+1)]
        for ind in range(n-1,-1,-1):
            for trans in range(1,k*2+1):
                if trans%2==0:
                    dp[ind][trans]=max(-prices[ind]+dp[ind+1][trans-1],dp[ind+1][trans])
                else:
                    dp[ind][trans]=max(prices[ind]+dp[ind+1][trans-1],dp[ind+1][trans])
        return dp[0][2*k]