class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)
        s2=s[::-1]
        dp=[[-1 for _ in range(n)] for _ in range(n)]
        def long(ind1,ind2):
            if ind1<0 or ind2<0:
                return 0
            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]
            if s[ind1]==s2[ind2]:
                dp[ind1][ind2]=1+long(ind1-1,ind2-1)
                return dp[ind1][ind2]
            dp[ind1][ind2]=max(long(ind1-1,ind2),long(ind1,ind2-1))
            return dp[ind1][ind2]
        return long(n-1,n-1)