class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        dp=[[-1 for _ in range(amount+1)] for _ in range(n)]
        def dfs(i,amt):
            if i<0 or amt<0:
                if amt==0:
                    return 1
                return 0
            if dp[i][amt]!=-1:
                return dp[i][amt]
            pick=dfs(i,amt-coins[i])
            notPick=dfs(i-1,amt)
            dp[i][amt]=pick+notPick
            return dp[i][amt]
        count=dfs(n-1,amount)
        return count