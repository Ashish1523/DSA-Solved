class Solution:
    def jump(self, nums: List[int]) -> int:
        # n=len(nums)
        # dp=[-1]*n
        # def dfs(i):
        #     if i>=n-1:
        #         return 0
        #     if nums[i]==0:
        #         return float("inf")
        #     if dp[i]!=-1:
        #         return dp[i]
        #     steps=float("inf")
        #     for j in range(nums[i],0,-1):
        #         steps=min(steps,1+dfs(i+j))
        #     dp[i]=steps
        #     return steps
        # ans=dfs(0)
        # return ans

        res=0
        l=r=0

        while r<len(nums)-1:
            farthest=0
            for i in range(l,r+1):
                farthest=max(farthest,i+nums[i])
            # print(farthest)
            l=r+1
            r=farthest
            res+=1
        return res