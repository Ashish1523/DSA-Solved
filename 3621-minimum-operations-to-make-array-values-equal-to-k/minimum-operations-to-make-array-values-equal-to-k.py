class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if k>max(nums) or k>min(nums):
            return -1
        count=0
        c=Counter(nums)
        for i in c:
            if c[i]>0 and i>k:
                count+=1
        return count