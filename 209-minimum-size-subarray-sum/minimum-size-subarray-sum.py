class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        l=0
        total=0
        mini=n+1
        for r in range(n):
            total+=nums[r]
            while total>=target:
                mini=min(r-l+1,mini)
                total-=nums[l]
                l+=1
        return mini if mini!=n+1 else 0


        return 0 if mini==n+1 else mini