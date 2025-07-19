class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj=[[] for _ in range(numCourses)]
        for course,pre in prerequisites:
            adj[pre].append(course)
        # print(adj)
        indegree=[0]*numCourses
        for i in range(numCourses):
            for j in adj[i]:
                indegree[j]+=1
        
        q=deque()
        for i in range(len(indegree)):
            if indegree[i]==0:
                q.append(i)
        
        ans=[0]*numCourses
        ind=0

        while q:
            node=q.popleft()
            ans[ind]=node
            ind+=1

            for i in adj[node]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
        # print(ans)
        return ans if ind==numCourses else []
            
