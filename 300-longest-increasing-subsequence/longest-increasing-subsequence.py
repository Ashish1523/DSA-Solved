class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # LIS=[1]*len(nums)
        # for i in range(len(nums)-1,-1,-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]<nums[j]:
        #             LIS[i]=max(LIS[i],1+LIS[j])
        # return max(LIS)
        n=len(nums)
        # dp=[[-1 for _ in range(n+1)] for _ in range(n)]
        # def dfs(ind,prev):
        #     if ind==n:
        #         return 0
        #     if dp[ind][prev+1]!=-1:
        #         return dp[ind][prev+1]
        #     notPick=dfs(ind+1,prev)
        #     pick=0
        #     if prev==-1 or nums[ind]>nums[prev]:
        #         pick=1+dfs(ind+1,ind)
        #     dp[ind][prev+1]=max(pick,notPick)
        #     return dp[ind][prev+1]
        # return dfs(0,-1)

        dp=[0 for _ in range(n+1)]
        for ind in range(n-1,-1,-1):
            prev_r=dp[:]
            for prev in range(ind-1,-2,-1):
                notPick=prev_r[prev+1]
                pick=0
                if prev==-1 or nums[ind]>nums[prev]:
                    pick=1+prev_r[ind+1]
                dp[prev+1]=max(pick,notPick)
        return dp[prev+1]