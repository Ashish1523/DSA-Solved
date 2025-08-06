class Solution:
    def minCut(self, s: str) -> int:
        n=len(s)
        # def palindrome(l,u):
        #     while l<u:
        #         if s[l]!=s[u]:
        #             return False
        #         l+=1
        #         u-=1
        #     return True
        # print(palindrome("aaab"))
        # dp=[-1]*n
        # def dfs(i):
        #     if i>=n:
        #         return 0
        #     if dp[i]!=-1:
        #         return dp[i]
        #     mini=float('inf')
            # for k in range(i,n):
            #     if palindrome(i,k):
            #         val=1+dfs(k+1)
            #         mini=min(val,mini)
            # dp[i]=mini
        #     return mini
        # return dfs(0)-1
        is_palindrome = [[False]*n for _ in range(n)]

        for i in range(n):
            is_palindrome[i][i] = True

        for i in range(n - 1):
            is_palindrome[i][i + 1] = (s[i] == s[i + 1])

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                is_palindrome[i][j] = (s[i] == s[j]) and is_palindrome[i + 1][j - 1]

        dp=[0]*(n+1)
        # dp[n]=0
        for i in range(n-1,-1,-1):
            mini=float('inf')
            for k in range(i,n):
                if is_palindrome[i][k]:
                    val=1+dp[k+1]
                    mini=min(val,mini)
            dp[i]=mini
        return dp[0]-1

