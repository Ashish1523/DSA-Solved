class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.append([[i,j],0])
        coord=[[0,1],[0,-1],[-1,0],[1,0]]
        time=0
        while q:
            [row,col],t=q.popleft()
            time=max(time,t)
            for r,c in coord:
                nrow=row+r
                ncol=col+c
                if 0<=nrow<len(grid) and 0<=ncol<len(grid[0]) and grid[nrow][ncol]==1:
                    q.append([[nrow,ncol],t+1])
                    grid[nrow][ncol]=2
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return -1
        return time
