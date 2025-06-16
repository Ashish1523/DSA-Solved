class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        subset=[]
        
        def dfs(i):
            if i==len(nums):
                result.append(subset[::])
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            dfs(i+1)
        dfs(0)
        print(result)
        # unique_matrix = [list(row) for row in set(tuple(row) for row in result)]
        return result