class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        maxRow=-1
        maxCol=-1
        
        m=len(grid)
        n=len(grid[0])
        minRow=m+1
        minCol=n+1
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    maxRow=max(maxRow,i)
                    maxCol=max(maxCol,j)
                    minRow=min(minRow,i)
                    minCol=min(minCol,j)
        
        return (maxRow-minRow+1)*(maxCol-minCol+1)
        
