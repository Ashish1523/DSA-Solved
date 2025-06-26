class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # ROWS,COLS=len(matrix),len(matrix[0])
        # cache={}

        # def helper(r,c):
        #     if r>=ROWS or c>=COLS:
        #         return 0
            
        #     if (r,c) not in cache:
        #         down=helper(r+1,c)
        #         right=helper(r,c+1)
        #         diag=helper(r+1,c+1)

        #         cache[(r,c)]=0
        #         if matrix[r][c]=="1":
        #             cache[(r,c)]=1+min(down,right,diag)
        #     return cache[(r,c)]

        # helper(0,0)
        # return max(cache.values())**2
        dp_mat=[]
        r,c=len(matrix),len(matrix[0])
        for i in range(len(matrix)):
            res=[]
            for j in range(len(matrix[0])):
                res.append(0)
            dp_mat.append(res)
        maxy=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=='1':
                    if i==0 or j==0:
                        dp_mat[i][j]=int(matrix[i][j])
                    else:
                        dp_mat[i][j]=min(dp_mat[i][j-1],dp_mat[i-1][j],dp_mat[i-1][j-1])+1
                    maxy=max(maxy,dp_mat[i][j])
        # print(dp_mat)
        return maxy**2
