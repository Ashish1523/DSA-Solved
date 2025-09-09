class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        M=10**9+7
        memo={}
        def solve(day):
            if day==1:
                return 1
            if day in memo:
                return memo[day]
            result=0
            for prev in range(day-forget+1,day-delay+1,1):
                if prev>0:
                    result+=solve(prev)
            memo[day]=result
            return result
        total=0
        for day in range(n-forget+1,n+1):
            if day>0:
                total=(total+solve(day))%M
        return total
            
