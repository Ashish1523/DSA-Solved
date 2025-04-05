class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # result=[]
        # subset=[]
        # def dfs(i):
        #     if i>=len(nums):
        #         result.append(subset.copy())
        #         return
        #     subset.append(nums[i])
        #     dfs(i+1)

        #     subset.pop()
        #     dfs(i+1)
        # dfs(0)
        # f_res=0
        # for i in result:
        #     s=0
        #     for j in i:
        #         s^=j
        #     f_res+=s
        # return f_res
        ans = 0
        for i in nums:
            ans |= i
        return ans << (len(nums)-1)