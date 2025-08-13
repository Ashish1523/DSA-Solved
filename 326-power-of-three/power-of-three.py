class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n:
            if n%3==0:
                n=n/3
            else:
                break
        # print(n)
        return True if n==1 else False
        