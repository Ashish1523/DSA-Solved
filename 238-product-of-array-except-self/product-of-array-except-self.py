class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # ans=Counter(nums)
        # if ans[0]>1:
        #     return [0]*len(nums)
        # prod=1
        # for i in nums:
        #     if i!=0:
        #         prod*=i
        # res=[]
        # for i in nums:
        #     if ans[0]==1:
        #         if i!=0:
        #             res.append(0)
        #         else:
        #             res.append(prod)
        #     else:
        #         res.append(prod//i)
        # return res

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