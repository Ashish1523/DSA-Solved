class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prod=math.prod(nums)
        ans=[]
        print(prod)
        if prod==0:
            for i in range(len(nums)):
                ans.append(math.prod(nums[:i]+nums[i+1:]))
            return ans
        else:
            for i in nums:
                ans.append(prod//i)
            return ans