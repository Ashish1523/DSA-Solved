class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s1=len(s)
        s2=len(p)
        # dp=[[-1 for _ in range(s2+1)] for _ in range(s1+1)]
        # def dfs(ind1,ind2):
        #     if ind1==0 and ind2==0:
        #         return True
        #     if ind2==0:
        #         return False
        #     if ind1==0:
        #         for i in range(ind2):
        #             if p[i]!='*':
        #                 return False
        #         return True
        #     if dp[ind1][ind2]!=-1:
        #         return dp[ind1][ind2]
        #     if s[ind1-1]==p[ind2-1] or p[ind2-1]=="?":
        #         dp[ind1][ind2]=dfs(ind1-1,ind2-1)
        #         return dp[ind1][ind2]
        #     if p[ind2-1]=="*":
        #         dp[ind1][ind2]=dfs(ind1-1,ind2) or dfs(ind1,ind2-1)
        #         return dp[ind1][ind2]
        #     dp[ind1][ind2]=False
        #     return dp[ind1][ind2]
        # return dfs(s1,s2)

        dp=[False for _ in range(s2+1)]
        dp[0]=True
        for j in range(1, s2+1):
            if p[j-1] == '*':
                dp[j] = dp[j-1]
            else:
                break

        for ind1 in range(1,s1+1):
            prev=dp[:]
            dp[0]=False
            for ind2 in range(1,s2+1):
                if s[ind1-1]==p[ind2-1] or p[ind2-1]=="?":
                    dp[ind2]=prev[ind2-1]
                elif p[ind2-1]=="*":
                    dp[ind2]=prev[ind2] or dp[ind2-1]
                else:
                    dp[ind2]=False
        return dp[s2]