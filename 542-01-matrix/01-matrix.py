class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        visited=[[0 for i in range(n)] for i in range(m)]
        dist=[[0 for i in range(n)] for i in range(m)]
        q=deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    q.append([[i,j],0])
                    visited[i][j]=1
                else:
                    visited[i][j]=0
        
        dest=[[0,1],[0,-1],[-1,0],[1,0]]

        while q:
            [row,col],steps=q.popleft()
            dist[row][col]=steps

            for r,c in dest:
                nrow=row+r
                ncol=col+c
                if (0<=nrow<m) and (0<=ncol<n) and visited[nrow][ncol]==0:
                    visited[nrow][ncol]=1
                    q.append([[nrow,ncol],steps+1])
        
        return dist