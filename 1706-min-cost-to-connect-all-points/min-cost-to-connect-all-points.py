class UnionFind:
    def __init__(self,n):
        self.parent=list(range(n))
        self.rank=[0]*n
    
    def find(self,u):
        if self.parent[u]==u:
            return u
        self.parent[u]=self.find(self.parent[u])
        return self.parent[u]
    
    def union(self,u,v):
        u=self.find(u)
        v=self.find(v)

        if u==v:
            return False
        
        if self.rank[u]>self.rank[v]:
            u,v=v,u

        self.parent[u]=v

        if self.rank[u]==self.rank[v]:
            self.rank[v]+=1
        
        return True



class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #Prims Algo
        # n=len(points)
        # min_cost=0
        # visited=[False]*n
        # pq=[(0,0)] #cost,vertex
        # cache={0:0}

        # while pq:
        #     cost,u=heapq.heappop(pq)

        #     if visited[u]:
        #         continue
            
        #     visited[u]=True
        #     min_cost+=cost

        #     for v in range(n):
        #         if not visited[v]:
        #             dist=abs(points[u][0]- points[v][0])+abs(points[u][1]-points[v][1])
        #             if dist<cache.get(v,float('inf')):
        #                 cache[v]=dist
        #                 heapq.heappush(pq,(dist,v))
        
        # return min_cost

        #Kruskal's algo

        n=len(points)
        uf=UnionFind(n)

        edges=[]
        for i in range(n):
            for j in range(i+1,n):
                dist=abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(edges,(dist,i,j))
        
        mst_wt=0
        mst_edg=0

        while edges:
            w,u,v =heapq.heappop(edges)
            if uf.union(u,v):
                mst_wt+=w
                mst_edg+=1
                if mst_edg==n-1:
                    break
        return mst_wt

