class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:
            return False
        def pew(n1):
            if n1==1:
                return True
            else:
                return pew(n1//2) if n1%2==0 else False
        return pew(n)
        
        