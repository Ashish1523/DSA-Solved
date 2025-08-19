class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans=0
        n=len(nums)
        count=0
        i=0
        j=0
        while j<n:
            if nums[j]==0:
                j+=1
            else:
                val=(j-i)
                count+=val*(val+1)//2
                j+=1
                i=j
        val=j-i
        count+=val*(val+1)//2
        



        
        return count


