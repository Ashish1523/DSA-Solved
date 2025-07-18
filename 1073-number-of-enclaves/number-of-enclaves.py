class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        count=0
        q=deque()

        m=len(grid)
        n=len(grid[0])

        for i in range(m):
            if grid[i][0]==1:
                grid[i][0]=0
                q.append((i,0))
            if grid[i][n-1]==1:
                grid[i][n-1]=0
                q.append((i,n-1))
        
        for j in range(n):
            if grid[0][j]==1:
                grid[0][j]=0
                q.append((0,j))
            if grid[m-1][j]==1:
                grid[m-1][j]=0
                q.append((m-1,j))
        des=[(-1,0),(1,0),(0,-1),(0,1)]
        while q:
            row,col=q.popleft()
            for r,c in des:
                nrow=r+row
                ncol=c+col
                if 0<=nrow<m and 0<=ncol<n and grid[nrow][ncol]==1:
                    grid[nrow][ncol]=0
                    q.append((nrow,ncol))
        # print(grid)
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    count+=1
        return count
        