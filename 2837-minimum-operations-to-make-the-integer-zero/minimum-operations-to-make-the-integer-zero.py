class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        t=0
        while True:
            val=num1-t*num2
            if val<0:
                return -1
            if bin(val).count('1')<=t and t<=val:
                return t
            t+=1
        