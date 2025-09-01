class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n=len(nums)
        prevSmallEle=[-1]*n
        nextSmallEle=[-1]*n

        stack=[]
        for i in range(n):
            while stack and nums[i]<=nums[stack[-1]]:
                stack.pop()
            if stack:
                prevSmallEle[i]=stack[-1]
            stack.append(i)
        
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and nums[i]>=nums[stack[-1]]:
                stack.pop()
            if stack:
                nextSmallEle[i]=stack[-1]
            stack.append(i)
        
        for i in range(n):
            if prevSmallEle[i]!=-1 and nextSmallEle[i]!=-1:
                return True
        return False