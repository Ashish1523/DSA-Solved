class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        dp=[[False for _ in range(n)] for _ in range(n)]
        count=0
        for l in range(1,n+1):
            for i in range(n-l+1):
                j=i+l-1
                if i==j:
                    dp[i][j]=True
                elif i+1==j:
                    dp[i][j]=(s[i]==s[j])
                else:
                    dp[i][j]=((s[i]==s[j]) and dp[i+1][j-1])
                if dp[i][j]==True:
                    count+=1
        return count
                
