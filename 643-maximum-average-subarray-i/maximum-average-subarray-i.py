class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max1=float("-inf")
        sum1=0
        for i in range(k):
            sum1+=nums[i]
        max1=max(sum1/k,max1)
        i=0
        for j in range(k,len(nums)):
            sum1-=nums[i]
            i+=1
            sum1+=nums[j]
            # print j
            max1=max(sum1/k,max1)
        return max1