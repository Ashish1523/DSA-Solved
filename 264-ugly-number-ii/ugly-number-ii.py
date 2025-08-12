class Solution:
    def nthUglyNumber(self, n: int) -> int:
        arr=[0]*(n+1)
        i1,i2,i3=1,1,1

        arr[1]=1
        for i in range(2,n+1):
            val1=arr[i1]*2
            val2=arr[i2]*3
            val3=arr[i3]*5

            ans=min(val1,val2,val3)
            arr[i]=ans

            if ans==val1:
                i1+=1
            if ans==val2:
                i2+=1
            if ans==val3:
                i3+=1
        return arr[n]