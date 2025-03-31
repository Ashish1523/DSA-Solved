class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for i in range(n+1):
            k=str(bin(i)[2:])
            count=0
            for j in k:
                if j=='1':
                    count+=1
            res.append(count)
        return res 