class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m=len(heights)
        n=len(heights[0])
        dist=[[float('inf') for _ in range(n)] for _ in range(m)]
        start=[0,0]
        end=[m-1,n-1]
        pq=[]
        heapq.heappush(pq,[0,0,0])
        dist[0][0]=0
        dest=[[0,1],[0,-1],[-1,0],[1,0]]
        while pq:
            diff,row,col=heapq.heappop(pq)
            if [row,col]==end:
                return diff
            for r,c in dest:
                nrow=row+r
                ncol=col+c

                if 0<=nrow<m and 0<=ncol<n:
                    newDiff=max(abs(heights[nrow][ncol]-heights[row][col]),diff)
                    if newDiff<dist[nrow][ncol]:
                        dist[nrow][ncol]=newDiff
                        heapq.heappush(pq,[newDiff,nrow,ncol])
        # return dist[m-1][n-1]
        
            