class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod=10**9+7
        dp=[0]*(n+1)
        dp[0]=1
        powers=[]
        i=1
        while(True):
            power=pow(i,x)
            if power>n:
                break
            powers.append(power)
            i+=1
        for p in powers:
            for j in range(n,p-1,-1):
                dp[j]=(dp[j]+dp[j-p])%mod

        return dp[n]