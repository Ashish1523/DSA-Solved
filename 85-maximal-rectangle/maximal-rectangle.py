class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def calcArea(height):
            stack=[]
            maxA=0
            n=len(height)
            for i in range(n+1):
                while stack and (i==n or height[stack[-1]]>=height[i]):
                    h=height[stack.pop()]
                    width=0
                    if not stack:
                        width=i
                    else:
                        width=i-stack[-1]-1
                    maxA=max(maxA,width*h)
                stack.append(i)
            return maxA
                    
        m=len(matrix[0])
        n=len(matrix)
        maxArea=0
        height=[0]*m
        for i in range(n):
            for j in range(m):
                if matrix[i][j]=="1":
                    height[j]+=1
                else:
                    height[j]=0
            area=calcArea(height)
            maxArea=max(maxArea,area)
        return maxArea