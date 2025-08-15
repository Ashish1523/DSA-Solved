class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n=len(nums)
        count=0
        csum=0
        freq={}

        for num in nums:
            csum+=num
            if csum==goal:
                count+=1
            
            if csum -goal in freq:
                count+=freq[csum-goal]
            
            freq[csum]=freq.get(csum,0)+1
        return count
            