class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color=[-1]*len(graph)
        for start in range(len(graph)):
            if color[start]==-1:
                q=deque()
                q.append(start)
                color[start]=0

                while q:
                    node=q.popleft()
                    for i in graph[node]:
                        if color[i]==-1:
                            color[i]= 0 if color[node]==1 else 1
                            q.append(i)
                        elif color[node]==color[i]:
                            return False
        return True
