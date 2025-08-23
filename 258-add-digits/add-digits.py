class Solution:
    def addDigits(self, num: int) -> int:
        num=str(num)
        while len(num)!=1:
            sum1=0
            for i in num:
                sum1+=int(i)
            num=str(sum1)
        return int(num)
