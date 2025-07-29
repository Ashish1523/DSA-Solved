class Solution:
    def minInsertions(self, s: str) -> int:
        n=len(s)
        s1=s[::-1]
        dp=[[-1 for _ in range(n)] for _ in range(n)]
        def match(ind1,ind2):
            if ind1<0 or ind2<0:
                return 0
            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]
            if s[ind1]==s1[ind2]:
                dp[ind1][ind2]=1+match(ind1-1,ind2-1)
                return dp[ind1][ind2]
            dp[ind1][ind2]=max(match(ind1-1,ind2),match(ind1,ind2-1))
            return dp[ind1][ind2]
        length=match(n-1,n-1)

        return n-length