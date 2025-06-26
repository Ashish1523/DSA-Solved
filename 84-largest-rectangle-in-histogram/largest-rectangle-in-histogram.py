class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def prev_s_e(heights):
            stack=[]
            ans=[-1]*len(heights)
            for i in range(len(ans)):
                while stack and stack[-1][0]>heights[i]:
                    stack.pop()
                if stack:
                    ans[i]=stack[-1][1]
                stack.append([heights[i],i])
            return ans

        def nex_s_e(heights):
            stack=[]
            ans=[len(heights)]*len(heights)
            for i in range(len(ans)-1,-1,-1):
                while stack and stack[-1][0]>=heights[i]:
                    stack.pop()
                if stack:
                    ans[i]=stack[-1][1]
                stack.append([heights[i],i])
            return ans
        pse=prev_s_e(heights)
        nse=nex_s_e(heights)
        maxy=0
        for i in range(len(heights)):
            left=pse[i]
            right=nse[i]
            maxy=max(maxy,heights[i]*(right-left-1))
        return maxy