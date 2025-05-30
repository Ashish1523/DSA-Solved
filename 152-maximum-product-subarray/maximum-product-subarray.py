class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # maxy=float("-inf")
        # for i in range(len(nums)):
        #     prod=nums[i]
        #     maxy=max(prod,maxy)
        #     for j in range(i+1,len(nums)):
        #         prod*=nums[j]
        #         maxy=max(prod,maxy)
        # return maxy
        res=max(nums)
        curMin,curMax=1,1

        for n in nums:
            # if n==0:
            #     curMin,curMax=1,1
            #     continue
            tmp=curMax*n
            curMax=max(n*curMax,n*curMin,n)
            curMin=min(tmp,n*curMin,n)
            res=max(res,curMax)
        return res
