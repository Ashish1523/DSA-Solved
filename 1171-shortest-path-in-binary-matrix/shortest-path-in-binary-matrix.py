class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        if grid==[[0]]:
            return 1
        if grid[0][0] != 0 or grid[m - 1][n - 1] != 0:
            return -1
        dist=[[200 for _ in range(n)] for _ in range(m)]
        
        q=deque()
        dist[0][0]=1
        q.append([[0,0],1])

        while q:
            [row,col],steps=q.popleft()
            # print([row,col],steps)
            for i in range(-1,2):
                for j in range(-1,2):
                    nrow=row+i
                    ncol=col+j

                    if 0<=nrow<m and 0<=ncol<n and steps+1<dist[nrow][ncol] and grid[nrow][ncol]==0:
                        # print(nrow,ncol)
                        dist[nrow][ncol]=steps+1
                        if nrow==m-1 and ncol==n-1:
                            # print(dist)
                            return steps+1
                        q.append([[nrow,ncol],steps+1])
                    
                    
        return -1