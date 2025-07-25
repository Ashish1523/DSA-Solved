class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        dp=[[[-1 for _ in range(col)] for _ in range(col)] for _ in range(row)]
        # def dfs(r,c1,c2):
        #     if c1<0 or c1>=col or c2<0 or c2>=col:
        #         return float('-inf')
        #     if r==row-1:
        #         if c1==c2:
        #             return grid[r][c1]
        #         return grid[r][c1]+grid[r][c2]
        #     if dp[r][c1][c2]!=-1:
        #         return dp[r][c1][c2]
        #     maxi=float('-inf')
        #     for i in range(-1,2):
        #         for j in range(-1,2):
        #             value=0
        #             if c1==c2:
        #                 value=grid[r][c1]
        #             else:
        #                 value=grid[r][c1]+grid[r][c2]
        #             value+=dfs(r+1,c1+i,c2+j)
        #             maxi=max(value,maxi)
        #     dp[r][c1][c2]=maxi
        #     return dp[r][c1][c2]

        # return dfs(0,0,col-1)

        for c1 in range(col):
            for c2 in range(col):
                if c1==c2:
                    dp[row-1][c1][c2]=grid[row-1][c1]
                else:
                    dp[row-1][c1][c2]=grid[row-1][c1]+grid[row-1][c2]
        
        for r in range(row-2,-1,-1):
            for c1 in range(col):
                for c2 in range(col):
                    maxi=float('-inf')
                    for i in range(-1,2):
                        for j in range(-1,2):
                            value=0
                            if c1==c2:
                                value=grid[r][c1]
                            else:
                                value=grid[r][c1]+grid[r][c2]
                            value+=dp[r+1][c1+i][c2+j] if 0<=c1+i<col and 0<=c2+j<col else float('-inf')
                            maxi=max(value,maxi)
                    dp[r][c1][c2]=maxi

        return dp[0][0][col-1]
                            

