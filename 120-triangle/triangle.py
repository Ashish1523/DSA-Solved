class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        # def dfs(i,j):
        #     if i>n-1 or j>n:
        #         return 0
        #     left=dfs(i+1,j)
        #     right=dfs(i+1,j+1)
        #     return min(left,right)+triangle[i][j]
        # return dfs(0,0)
        front=[0 for _ in range(n)]
        for j in range(n):
            front[j]=triangle[n-1][j]
        curr=front
        for i in range(n-2,-1,-1):
            for j in range(len(triangle[i])):
                bottom=front[j]
                bottom_left=front[j+1]
                curr[j]=min(bottom,bottom_left)+triangle[i][j]
            front=curr
        return front[0]