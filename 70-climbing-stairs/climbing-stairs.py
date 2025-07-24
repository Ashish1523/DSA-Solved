class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[-1 for _ in range(n+1)]
        
        def stairs(n):
            if n<=1:
                return 1
            if dp[n]!=-1:
                return dp[n]
            dp[n]=stairs(n-1)+stairs(n-2)
            return dp[n]
        return stairs(n)
        # one,two=1,1

        # for i in range(n-1):
        #     temp=one
        #     one=one+two
        #     two=temp
        # return one