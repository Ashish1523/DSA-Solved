class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1]*n
        count=[1]*n
        maxi=1
        for ind in range(n):
            for prev in range(ind):
                if nums[prev]<nums[ind] and dp[prev]+1>dp[ind]:
                    dp[ind]=dp[prev]+1
                    count[ind]=count[prev]
                elif nums[prev]<nums[ind] and dp[prev]+1==dp[ind]:
                    count[ind]+=count[prev]

            if dp[ind]>maxi:
                maxi=dp[ind]
            
        cnt=0
        for i in range(n):
            if dp[i]==maxi:
                cnt+=count[i]

        return cnt
