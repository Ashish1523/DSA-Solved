class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count=0
        for i in range(low,high+1):
            if len(str(i))%2!=0:
                continue
            n=len(str(i))
            s1,s2=0,0
            # print(str(i))
            for j in range(len(str(i))//2):
                # print(str(i)[j])
                s1+=int(str(i)[j])
            for j in range(len(str(i))//2,len(str(i))):
                s2+=int(str(i)[j])
            if s2==s1:
                count+=1
        return count