class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        
        n=len(values)
        dp=[[-1 for _ in range(n)] for _ in range(n)]
        def solve(i,j):
            if j-i+1<3:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            result=float("inf")
            for k in range(i+1,j):
                wt=values[i]*values[k]*values[j]+solve(i,k)+solve(k,j)
                result=min(result,wt)
            dp[i][j]=result
            return result
        ans=solve(0,n-1)
        return 0 if ans==float("inf") else ans