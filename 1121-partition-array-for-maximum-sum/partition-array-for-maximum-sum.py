class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n=len(arr)
        dp=[-1]*n
        def dfs(i):
            if i==n:
                return 0
            if dp[i]!=-1:
                return dp[i]
            l=0
            maxi=float('-inf')
            max_ans=float('-inf')
            for j in range(i,min(n,i+k)):
                l+=1
                maxi=max(maxi,arr[j])
                sum1=l*maxi+dfs(j+1)
                max_ans=max(max_ans,sum1)
            dp[i]=max_ans
            return max_ans

        return dfs(0)


            