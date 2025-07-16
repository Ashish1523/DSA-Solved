class Solution:
    def bfs(self,grid,visited,i,j):
        visited[i][j]=True
        q=deque()
        q.append([i,j])
        dest=[[-1,0],[1,0],[0,1],[0,-1]]
        while q:
            row,col=q.popleft()
            for r,c in dest:
                nrow=row+r
                ncol=col+c
                if (0<=nrow<len(grid)) and (0<=ncol<len(grid[0])) and grid[nrow][ncol]=="1" and not visited[nrow][ncol]:
                    visited[nrow][ncol]=True
                    q.append([nrow,ncol])
        
        
    def numIslands(self, grid: List[List[str]]) -> int:
        visited=[[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and not visited[i][j]:
                    count+=1
                    self.bfs(grid,visited,i,j)
        return count