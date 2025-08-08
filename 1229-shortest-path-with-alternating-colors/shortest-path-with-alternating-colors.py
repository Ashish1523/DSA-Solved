class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        ans=[-1]*n
        G =[[] for _ in range(n)]
        for src,dest in redEdges:
            G[src].append((dest,1))
        for src,dest in blueEdges:
            G[src].append((dest,0))

        q=deque()
        q.append((0,-1))

        step=0
        visited=set()
        while q:
            for _ in range(len(q)):
                u,prevColor=q.popleft()
                if (u,prevColor) in visited:
                    continue
                visited.add((u,prevColor))
                if ans[u]==-1:
                    ans[u]=step
                for i,(v,edgeColor) in enumerate(G[u]):
                    if edgeColor!=prevColor:
                        q.append((v,edgeColor))
            step+=1
        
        return ans
        