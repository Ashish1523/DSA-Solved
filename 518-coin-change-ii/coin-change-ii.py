class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        # dp=[[-1 for _ in range(amount+1)] for _ in range(n)]
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
        prev=[0]*(amount+1)
        prev[0]=1
        curr=prev
        for ind in range(n):
            for tar in range(coins[ind],amount+1):
                notPick=prev[tar]
                pick=prev[tar-coins[ind]]
                curr[tar]=pick+notPick
            prev=curr
        return prev[amount]
