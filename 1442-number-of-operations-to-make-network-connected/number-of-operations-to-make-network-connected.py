class Disjoint:
    def __init__(self,size):
        self.parent=list(range(size))
        self.rank=[0]*size

    def find(self,node):
        if self.parent[node]!=node:
            self.parent[node]= self.find(self.parent[node])
        return self.parent[node]
    
    def unionSet(self,node1,node2):
        xset=self.find(node1)
        yset=self.find(node2)
        if self.rank[xset]<self.rank[yset]:
            self.parent[xset]=yset
        elif self.rank[yset]<self.rank[xset]:
            self.parent[yset]=xset
        else:
            self.parent[yset]=xset
            self.rank[xset]+=1


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        ds=Disjoint(n)
        cntExtras=0
        for n1,n2 in connections:
            if ds.find(n1)==ds.find(n2):
                cntExtras+=1
            else:
                ds.unionSet(n1,n2)
        cntC=0
        for i in range(n):
            if ds.find(i)==i:
                cntC+=1
        ans=cntC-1
        if cntExtras>=ans:
            return ans
        return -1

        