class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        n=len(nums)
        ans=0
        for num in nums:
            ans^=num
        count=0
        while ans or k:
            if ans&1 !=k&1:
                count+=1
            ans=ans>>1
            k=k>>1
        return count
        

        