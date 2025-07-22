class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist=[[float('inf') for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dist[i][i]=0
        
        for s,d,wt in edges:
            dist[s][d]=wt
            dist[d][s]=wt
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
        min_reachable = n + 1
        result_city = -1
        
        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and dist[i][j] <= distanceThreshold:
                    count += 1
            if count <= min_reachable:
                min_reachable = count
                result_city = i
        
        return result_city