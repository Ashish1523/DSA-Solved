class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = (10**9)+7
        @lru_cache(None)
        def func(idx,sums):
            nonlocal x , n
            if idx == n+1:
                return 1 if sums==0 else 0
            not_take = func(idx+1,sums)
            temp = idx**x
            take = 0
            if sums >= temp:
                take += func(idx+1,sums-temp)
            return (take+not_take)%MOD

        return func(1,n)%MOD