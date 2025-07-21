class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=[[] for _ in range(n)]

        for s,d,w in times:
            adj[s-1].append([d-1,w])
        
        dist=[float('inf') for _ in range(n)]
        dist[k-1]=0
        pq=[]
        heapq.heappush(pq,[0,k-1])

        while pq:
            distance,node=heapq.heappop(pq)

            for adjNode,weight in adj[node]:
                # print(adjNode)
                if distance+weight<dist[adjNode]:
                    dist[adjNode]=distance+weight
                    heapq.heappush(pq,[distance+weight,adjNode])
        ans=0
        for i in dist:
            if i==float('inf'):
                return -1
            ans=max(i,ans)
        return ans
            