class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        n=len(coins)
        dp=[[-1 for _ in range(amount+1)] for _ in range(n)]
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

        for i in range(amount+1):
            if i%coins[0]==0:
                dp[0][i]=i//coins[0]
            else:
                dp[0][i]=float('inf')
        
        for i in range(1,n):
            for t in range(amount+1):
                notTake=dp[i-1][t]
                take=float('inf')
                if coins[i]<=t:
                    take=1+dp[i][t-coins[i]]
                dp[i][t]=min(take,notTake)
        return dp[n-1][amount] if dp[n-1][amount]!=float('inf') else -1