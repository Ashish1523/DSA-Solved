class Solution:
    def dfs(self,node,isConnected,visit):
        visit[node]=True
        for i in range(len(isConnected)):
            if isConnected[node][i] and not visit[i]:
                self.dfs(i,isConnected,visit)


    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        size=len(isConnected)
        no=0
        visit=[False]*size

        for i in range(size):
            if not visit[i]:
                no+=1
                self.dfs(i,isConnected,visit)
        return no