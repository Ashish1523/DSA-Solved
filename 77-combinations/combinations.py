class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        stack=[]
        def dfs(i,c):
            if c==k:
                ans.append(stack[:])
                return
            if i==n+1:
                return
            stack.append(i)
            dfs(i+1,c+1)
            stack.pop()
            dfs(i+1,c)
        dfs(1,0)
        return ans
