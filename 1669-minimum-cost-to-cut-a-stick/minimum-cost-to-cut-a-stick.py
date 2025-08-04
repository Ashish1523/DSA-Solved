class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.insert(0,0)
        cuts.append(n)
        cuts.sort()
        count=len(cuts)
        dp=[[-1 for i in range(count)] for _ in range(count)]
        def dfs(i,j):
            if i>j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            mini=float('inf')
            for k in range(i,j+1):
                val=cuts[j+1]-cuts[i-1]+dfs(i,k-1)+dfs(k+1,j)
                mini=min(val,mini)
            dp[i][j]=mini
            return dp[i][j]
        return dfs(1,count-2)

    