class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)-2):
            if nums[i]==0:
                nums[i]=1
                nums[i+1]=0 if nums[i+1]==1 else 1
                nums[i+2]=0 if nums[i+2]==1 else 1
                count+=1
                
        if sum(nums)==len(nums):
            return count
        return -1
