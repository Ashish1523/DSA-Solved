class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # n=len(nums)
        # l=0
        # total=0
        # mini=n+1
        # for r in range(n):
        #     total+=nums[r]
        #     while total>=target:
        #         mini=min(r-l+1,mini)
        #         total-=nums[l]
        #         l+=1
        # return mini if mini!=n+1 else 0

        n=len(nums)
        prefix=[0]*(n+1)
        for i in range(1,n+1):
            prefix[i]=prefix[i-1]+nums[i-1]
        
        res=n+1

        for i in range(n):
            required=target+prefix[i]
            left,right=i+1,n
            pos=-1
            while left<=right:
                mid=(left+right)//2
                if prefix[mid]>=required:
                    pos=mid
                    right=mid-1
                else:
                    left=mid+1
            
            if pos!=-1:
                res=min(res,pos-i)
        return 0 if res==n+1 else res


