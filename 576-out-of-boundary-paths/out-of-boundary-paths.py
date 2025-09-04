class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD=10**9+7
        dest=[[-1,0],[1,0],[0,1],[0,-1]]
        dp=[[[-1]*(maxMove+1) for i in range(n)] for j in range(m)]
        def dfs(i,j,moves):
            if i<0 or i>=m or j<0 or j>=n:
                return 1
            if moves==0:
                return 0
            if dp[i][j][moves]!=-1:
                return dp[i][j][moves]
            pick=0
            for r,c in dest:
                nrow=i+r
                ncol=j+c
                pick+=dfs(nrow,ncol,moves-1)
            dp[i][j][moves]=pick
            return pick
        return dfs(startRow,startColumn,maxMove)%MOD