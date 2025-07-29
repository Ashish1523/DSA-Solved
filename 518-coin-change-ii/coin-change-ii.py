class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        dp=[[-1 for _ in range(amount+1)] for _ in range(n)]
        # def dfs(i,amt):
        #     if i<0:
        #         if amt==0:
        #             return 1
        #         return 0
        #     if dp[i][amt]!=-1:
        #         return dp[i][amt]
        #     pick=0
        #     if coins[i]<=amt:
        #         pick=dfs(i,amt-coins[i])
        #     notPick=dfs(i-1,amt)
        #     dp[i][amt]=pick+notPick
        #     return dp[i][amt]
        # count=dfs(n-1,amount)
        # return count
        for i in range(amount+1):
            dp[0][i]=1 if i%coins[0]==0 else 0
        
        for ind in range(1,n):
            for tar in range(amount+1):
                notPick=dp[ind-1][tar]
                pick=dp[ind][tar-coins[ind]] if coins[ind]<=tar else 0
                dp[ind][tar]=pick+notPick
        return dp[n-1][amount]
