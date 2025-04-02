class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # a=0
        # for n in nums:
        #     a^=n
        # return a
        if len(nums)==1:
            return nums[0]
        l=0
        h=len(nums)-1
        while(l<=h):
            m=(l+h)//2
            if m==len(nums)-1:
                return nums[m]
            if nums[m]==nums[m+1]:
                if m%2==0:
                    l=m+1
                else:
                    h=m-1
            elif nums[m]==nums[m-1]:
                if m%2==0:
                    h=m-1
                else:
                    l=m+1
            else:
                return nums[m]
