class Solution:
    def minDifficulty(self, jd: List[int], d: int) -> int:
        
        def solve(idx,d):
            if d==1:
                maxD=max(jd[idx:])
                return maxD
            if dp[idx][d]!=-1:
                return dp[idx][d]
            maxD=jd[idx]
            finalRes=float('inf')
        
            for i in range(idx,n-d+1):
                maxD=max(maxD,jd[i])
                result=maxD+solve(i+1,d-1)
                finalRes=min(finalRes,result)
            dp[idx][d]=finalRes
            return finalRes


        n=len(jd)
        dp=[[-1 for _ in range(d+1)] for _ in range(n)]
        if n<d:
            return -1
        return solve(0,d)
        
        
        

        