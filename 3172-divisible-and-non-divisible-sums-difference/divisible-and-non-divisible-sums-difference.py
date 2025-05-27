class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        k=n//m
        k=k*m
        # print(k)
        ans=n*(n+1)//2
        # print(k//m)
        ans1=(k//m)*(2*m+((k//m)-1)*m)
        # print(ans1)
        return ans-ans1