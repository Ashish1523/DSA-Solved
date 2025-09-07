class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        l=0
        h=n-1
        ans=0
        while l<h:
            val=nums[l]+nums[h]
            if val==k:
                ans+=1
                l+=1
                h-=1
            elif val<k:
                l+=1
            else:
                h-=1
        return ans