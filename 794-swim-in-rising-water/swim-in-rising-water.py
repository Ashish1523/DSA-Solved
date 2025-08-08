class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])

        pq=[]
        direction=[(-1,0),(0,-1),(1,0),(0,1)]

        heapq.heappush(pq,(grid[0][0],0,0))
        visited=set()
        while pq:
            height,row,col=heapq.heappop(pq)
            if (row,col) in visited:
                continue
            visited.add((row,col))
            for r,c in direction:
                nrow=r+row
                ncol=c+col
                if 0<=nrow<m and 0<=ncol<n and (nrow,ncol) not in visited:
                    if nrow==m-1 and ncol==n-1:
                        return max(height,grid[nrow][ncol])
                    heapq.heappush(pq,(max(height,grid[nrow][ncol]),nrow,ncol))
        return grid[0][0]
        