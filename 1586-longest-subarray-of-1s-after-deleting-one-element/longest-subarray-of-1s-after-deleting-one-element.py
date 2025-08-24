class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        i=0
        j=0
        ans=0
        while j<n:
            if nums[j]==0:
                count+=1
            if count>1:
                if nums[i]==0:
                    count-=1
                i+=1
            ans=max(ans,j-i+1)
            j+=1
        return ans-1