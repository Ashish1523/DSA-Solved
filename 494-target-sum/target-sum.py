class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        dp={}
        def recursion(i,target):
            if i<0:
                if target==0:
                    return 1
                return 0
            if (i,target) in dp:
                return dp[(i,target)]
            dp[(i,target)]=recursion(i-1,target-nums[i])+recursion(i-1,target+nums[i])
            return dp[(i,target)]
        count=recursion(n-1,target)
        return count
                