class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # res=[-1]*len(nums)
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)+(len(nums))):
        #         if nums[j%len(nums)]>nums[i]:
        #             res[i]=nums[j%len(nums)]
        #             break
        # return res
        stack=[]
        res=[-1]*len(nums)
        for i in range(len(nums)+len(nums)-1,-1,-1):
            while stack and stack[-1]<=nums[i%len(nums)]:
                stack.pop()
            if i<len(nums):
                if stack:
                    res[i]=stack[-1]
            stack.append(nums[i%len(nums)])
            # print(stack)
        return res
