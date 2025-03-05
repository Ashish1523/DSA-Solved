class Solution:
    def coloredCells(self, n: int) -> int:
        sum2=0
        n1=n*2-1-2
        while(n1>0):
            sum2+=n1
            n1-=2
        return (2*sum2)+(n*2-1)
