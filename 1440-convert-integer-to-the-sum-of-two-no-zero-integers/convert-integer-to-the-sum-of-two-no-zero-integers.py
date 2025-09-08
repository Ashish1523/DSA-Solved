class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def checkZero(k):
            s=str(k)
            for i in s:
                if i=="0":
                    return False
            return True
        low=1
        high=n-1
        while low<=high:
            if checkZero(low) and checkZero(high):
                return [low,high]
            low+=1
            high-=1
