class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n==0:
            return 0
        
        F=[0]*(32)
        F[0]=1
        for i in range(1,31):
            F[i]=2*F[i-1]+1

        sign=1
        result=0
        for i in range(30,-1,-1):
            ithBit=(1<<i)&n

            if ithBit==0:
                continue
            
            if sign>0:
                result+=F[i]
            else:
                result-=F[i]
            sign*=-1
        return result
        











        return 0
        


