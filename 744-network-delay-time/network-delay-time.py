class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=[[] for _ in range(n)]

        for s,d,w in times:
            adj[s-1].append([d-1,w])
        
        dist=[float('inf') for _ in range(n)]
        dist[k-1]=0
        pq=[]
        heapq.heappush(pq,[0,k-1])
        visited=set()

        while pq:
            distance,node=heapq.heappop(pq)
            visited.add(node)
            for adjNode,weight in adj[node]:
                # print(adjNode)
                if distance+weight<dist[adjNode]:
                    dist[adjNode]=distance+weight
                    heapq.heappush(pq,[distance+weight,adjNode])
        
        if len(visited)<n:
            return -1
        return max(dist)
            