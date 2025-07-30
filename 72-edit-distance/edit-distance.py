class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m=len(word1)
        n=len(word2)
        dp=[[-1 for _ in range(n+1)] for _ in range(m+1)]

        def dfs(ind1,ind2):
            if ind2<0:
                return ind1+1
            if ind1<0:
                return ind2+1
            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]
            if word1[ind1]==word2[ind2]:
                dp[ind1][ind2]=dfs(ind1-1,ind2-1)
                return dp[ind1][ind2]
            ins=1+dfs(ind1,ind2-1)
            dele=1+dfs(ind1-1,ind2)
            replace=1+dfs(ind1-1,ind2-1)
            dp[ind1][ind2]=min(ins,dele,replace)
            return dp[ind1][ind2]
        return dfs(m-1,n-1)