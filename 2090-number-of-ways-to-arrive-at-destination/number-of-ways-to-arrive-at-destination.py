class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod=10**9+7
        adj=[[] for _ in range(n)]
        for n1,n2,wt in roads:
            adj[n1].append([n2,wt])
            adj[n2].append([n1,wt])
        
        pq=[]
        dist=[float('inf') for _ in range(n)]
        ways=[0 for _ in range(n)]
        dist[0]=0
        ways[0]=1
        heapq.heappush(pq,[0,0])
        while pq:
            dis,node=heapq.heappop(pq)

            for adjNode,edW in adj[node]:
                if dis+edW<dist[adjNode]:
                    dist[adjNode]=dis+edW
                    heapq.heappush(pq,[dis+edW,adjNode])
                    ways[adjNode]=ways[node]
                elif (dis+edW==dist[adjNode]):
                    ways[adjNode]=(ways[adjNode]+ways[node])%mod
        
        return ways[n-1]%mod

