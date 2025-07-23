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
    def removeStones(self, stones: List[List[int]]) -> int:
        maxRow=0
        maxCol=0
        for r,c in stones:
            maxRow=max(r,maxRow)
            maxCol=max(c,maxCol)
        ds=Disjoint(maxRow+maxCol+2)

        mapy={}
        for it in stones:
            nrow=it[0]
            ncol=it[1]+maxRow+1
            print(nrow,ncol)
            ds.unionSet(nrow,ncol)
            mapy[nrow]=1
            mapy[ncol]=1
        
        cnt=0
        for i in mapy:
            if ds.find(i)==i:
                cnt+=1
        return len(stones)-cnt

