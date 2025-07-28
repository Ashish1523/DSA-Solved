class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        n=len(coins)
        # dp=[[-1 for _ in range(amount+1)] for _ in range(n)]
        # def dfs(i,amt):
        #     if i==0:
        #         if amt%coins[i]==0:
        #             dp[i][amt]=amt//coins[i]
        #             return dp[i][amt]
        #         dp[i][amt]=float('inf')
        #         return dp[i][amt]
        #     if dp[i][amt]!=-1:
        #         return dp[i][amt]
        #     notTake=dfs(i-1,amt)
        #     take=float('inf')
        #     if coins[i]<=amt:
        #         take=1+dfs(i,amt-coins[i])
        #     dp[i][amt]=min(take,notTake)
        #     return dp[i][amt]
        # dfs(n-1,amount)
        # return dp[n-1][amount] if dp[n-1][amount]!=float('inf') else -1

        dp=[float('inf')]*(amount+1)
        dp[0]=0
        
        for i in range(n):
            for t in range(coins[i],amount+1):
                notTake=dp[t]
                take=1+dp[t-coins[i]]
                dp[t]=min(take,notTake)
        print(dp)
        return dp[amount] if dp[amount]!=float('inf') else -1