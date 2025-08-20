class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ROWS,COLS=len(matrix),len(matrix[0])
        # cache={}
        # def dfs(r,c):
        #     if r==ROWS or c==COLS or not matrix[r][c]:
        #         return 0
        #     if (r,c) in cache:
        #         return cache[(r,c)]
        #     cache[(r,c)]=1+min(
        #         dfs(r+1,c),
        #         dfs(r,c+1),
        #         dfs(r+1,c+1)
        #     )
        #     return cache[(r,c)]
        # res=0
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         res+=dfs(r,c)
        # return res


        dp=defaultdict(int)
        res=0
        for r in range(ROWS):
            curr_dp=defaultdict(int)
            for c in range(COLS):
                if matrix[r][c]:
                    curr_dp[c]=1+min(
                        dp[c],
                        curr_dp[c-1],
                        dp[c-1]
                    )
                    res+=curr_dp[c]
            dp=curr_dp 
        return res

        