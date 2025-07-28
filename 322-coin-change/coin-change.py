class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        n=len(coins)
        dp=[[-1 for _ in range(amount+1)] for _ in range(n)]
        def dfs(i,amt):
            if i==0:
                if amt%coins[i]==0:
                    dp[i][amt]=amt//coins[i]
                    return dp[i][amt]
                dp[i][amt]=float('inf')
                return dp[i][amt]
            if dp[i][amt]!=-1:
                return dp[i][amt]
            notTake=dfs(i-1,amt)
            take=float('inf')
            if coins[i]<=amt:
                take=1+dfs(i,amt-coins[i])
            dp[i][amt]=min(take,notTake)
            return dp[i][amt]
        dfs(n-1,amount)
        # print(dp)
        return dp[n-1][amount] if dp[n-1][amount]!=float('inf') else -1