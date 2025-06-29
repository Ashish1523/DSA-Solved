class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # res=[]
        # stack=[]
        # used=[False]*len(nums)
        # def com():
        #     if len(stack)==len(nums):
        #         res.append(stack[:])
        #         return
        #     for i in range(len(nums)):
        #         if used[i]:
        #             continue
        #         used[i]=True
        #         stack.append(nums[i])
        #         com()
        #         stack.pop()
        #         used[i]=False
        # com()
        # return res

        res=[]
        def per(k):
            if k==len(nums):
                res.append(nums[:])
                return
            for i in range(k,len(nums)):
                nums[k],nums[i]=nums[i],nums[k]
                per(k+1)
                nums[k],nums[i]=nums[i],nums[k]
        per(0)
        return res