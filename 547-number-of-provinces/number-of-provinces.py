class UnionFind:
    def __init__(self,size):
        self.parent=list(range(size))
        self.rank=[0]*size

    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union_set(self,x,y):
        xset=self.find(x)
        yset=self.find(y)
        if self.rank[xset]<self.rank[yset]:
            self.parent[xset]=yset
        elif self.rank[yset]<self.rank[xset]:
            self.parent[yset]=xset
        else:
            self.parent[yset]=xset
            self.rank[xset]+=1

class Solution:
    # def dfs(self,node,isConnected,visit):
    #     visit[node]=True
    #     for i in range(len(isConnected)):
    #         if isConnected[node][i] and not visit[i]:
    #             self.dfs(i,isConnected,visit)


    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # size=len(isConnected)
        # no=0
        # visit=[False]*size

        # for i in range(size):
        #     if not visit[i]:
        #         no+=1
        #         self.dfs(i,isConnected,visit)
        # return no

        # Union Find
        n=len(isConnected)
        uf=UnionFind(n)
        numberOfComponents=n
        count=0
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j]==1 and uf.find(i)!=uf.find(j):
                    numberOfComponents-=1
                    uf.union_set(i,j)
        
        return numberOfComponents