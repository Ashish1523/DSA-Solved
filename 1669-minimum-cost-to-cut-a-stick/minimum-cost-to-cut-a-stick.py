class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.insert(0,0)
        cuts.append(n)
        cuts.sort()
        count=len(cuts)
        # dp=[[-1 for _ in range(count)] for _ in range(count)]
        # def dfs(i,j):
        #     if i>j:
        #         return 0
        #     if dp[i][j]!=-1:
        #         return dp[i][j]
        #     mini=float('inf')
        #     for k in range(i,j+1):
        #         val=cuts[j+1]-cuts[i-1]+dfs(i,k-1)+dfs(k+1,j)
        #         mini=min(val,mini)
        #     dp[i][j]=mini
        #     return dp[i][j]
        # return dfs(1,count-2)
        c=count-2
        dp=[[0 for _ in range(c+2)] for _ in range(c+2)]
        
        for i in range(c,0,-1):
            for j in range(1,c+1):
                if i>j:
                    continue
                mini=float('inf')
                for k in range(i,j+1):
                    val=cuts[j+1]-cuts[i-1]+dp[i][k-1]+dp[k+1][j]
                    mini=min(val,mini)
                dp[i][j]=mini
        # print(dp)
        return dp[1][c]
    