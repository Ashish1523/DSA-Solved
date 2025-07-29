class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        t1=len(text1)
        t2=len(text2)
        dp=[[-1 for _ in range(t2)] for _ in range(t1)]
        def dfs(ind1,ind2):
            if ind1<0 or ind2<0:
                return 0
            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]
            if text1[ind1]==text2[ind2]:
                return 1+dfs(ind1-1,ind2-1)
            dp[ind1][ind2]=max(dfs(ind1-1,ind2),dfs(ind1,ind2-1))
            return dp[ind1][ind2]
        return dfs(t1-1,t2-1)