class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n=len(nums)
        l=0
        r=0
        ans=0
        while r<n:
            if k==0 and nums[r]==0:
                while nums[l]!=0:
                    l+=1
                l+=1
                k+=1
                # print(l)
            if nums[r]==0:
                k-=1
            ans=max(ans,r-l+1)
            r+=1
        return ans
        
            
            