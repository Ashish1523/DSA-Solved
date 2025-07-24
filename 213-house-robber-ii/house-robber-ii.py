class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        prev1=0
        prev2=0
        money=0
        for i in range(1,len(nums)):
            take=nums[i]+prev1
            notTake=prev2
            curr=max(take,notTake)
            # money+=curr
            prev1=prev2
            prev2=curr
        money=prev2
        # mone=0
        prev1=0
        prev2=0
        for i in range(len(nums)-1):
            take=nums[i]+prev1
            notTake=prev2
            curr=max(take,notTake)
            # mone+=curr
            prev1=prev2
            prev2=curr
        return max(money,prev2)

            