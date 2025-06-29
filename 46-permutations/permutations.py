class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        stack=[]
        used=[False]*len(nums)
        def com():
            if len(stack)==len(nums):
                res.append(stack[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i]=True
                stack.append(nums[i])
                com()
                stack.pop()
                used[i]=False
        com()
        return res