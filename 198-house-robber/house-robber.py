class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        stash=[-1 for _ in range(n)]
        sum1=0
        def dfs(i):
            nonlocal sum1
            if i>=n:
                return 0
            if stash[i]!=-1:
                return stash[i]
            take=dfs(i+2)+nums[i]
            notTake=dfs(i+1)+0
            stash[i]=max(take,notTake)
            return stash[i]
        return dfs(0)


