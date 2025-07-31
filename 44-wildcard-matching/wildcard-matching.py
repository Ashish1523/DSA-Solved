class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s1=len(s)
        s2=len(p)
        dp=[[-1 for _ in range(s2)] for _ in range(s1)]
        def dfs(ind1,ind2):
            if ind1<0 and ind2<0:
                return True
            if ind2<0:
                return False
            if ind1<0:
                # print(p[:ind2+1])
                for i in range(ind2+1):
                    if p[i]!='*':
                        return False
                return True
            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]
            if s[ind1]==p[ind2] or p[ind2]=="?":
                dp[ind1][ind2]=dfs(ind1-1,ind2-1)
                return dp[ind1][ind2]
            if p[ind2]=="*":
                dp[ind1][ind2]=dfs(ind1-1,ind2) or dfs(ind1,ind2-1)
                return dp[ind1][ind2]
            dp[ind1][ind2]=False
            return dp[ind1][ind2]
        return dfs(s1-1,s2-1)