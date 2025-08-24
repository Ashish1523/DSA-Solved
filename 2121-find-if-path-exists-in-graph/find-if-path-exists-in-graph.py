class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # n=len(edges)
        adj=[[] for _ in range(n)]
        # print(adj)
        for src,dest in edges:
            # print(src,dest)
            adj[src].append(dest)
            adj[dest].append(src)
            # print(adj)
        # print(adj)
        visited=[False]*n
        # visited[source]=True
        def dfs(node):
            # print(node)
            visited[node]=True
            if node==destination:
                return True
            
            for child in adj[node]:
                if not visited[child]:
                    if dfs(child):
                        return True
            return False
        return dfs(source)