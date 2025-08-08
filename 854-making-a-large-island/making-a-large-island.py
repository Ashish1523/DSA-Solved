class Disjoint:
    def __init__(self,nodes):
        self.parent=list(range(nodes))
        self.size=[1]*nodes
    
    def find(self,node):
        if self.parent[node]!=node:
            self.parent[node]=self.find(self.parent[node])
        return self.parent[node]
    
    def unionSet(self,node1,node2):
        xset=self.find(node1)
        yset=self.find(node2)

        if xset==yset:
            return
        if self.size[xset]<self.size[yset]:
            self.parent[xset]=yset
            self.size[yset]+=self.size[xset]
        else:
            self.parent[yset]=xset
            self.size[xset]+=self.size[yset]
        


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        ds=Disjoint(m*n)
        des=[[-1,0],[1,0],[0,-1],[0,1]]
        Zero=[]
        for row in range(m):
            for col in range(n):
                if grid[row][col]==0:
                    Zero.append((row,col))
                    continue
                for r,c in des:
                    nrow=r+row
                    ncol=c+col
                    if 0<=nrow<m and 0<=ncol<n and grid[nrow][ncol]==1:
                        nodeNo=row*m+col
                        adjNodeNo=nrow*m+ncol
                        ds.unionSet(nodeNo,adjNodeNo)
        mx=0
        for row,col in Zero:
            components=set()
            for r,c in des:
                nrow=row+r
                ncol=col+c
                if 0<=nrow<m and 0<=ncol<n and grid[nrow][ncol]==1:
                    components.add(ds.find(nrow*m+ncol))
            
            sizeT=0
            for i in components:
                sizeT+=ds.size[i]
            mx=max(mx,sizeT+1)

        # return max(mx,m*n-len(Zero))
        for cellNo in range(n):
            mx=max(mx,ds.size[ds.find(cellNo)])
        return mx