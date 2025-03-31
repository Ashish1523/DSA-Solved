class Solution:
    def countBits(self, n: int) -> List[int]:
        # res=[]
        # for i in range(n+1):
        #     k=str(bin(i)[2:])
        #     count=0
        #     for j in k:
        #         if j=='1':
        #             count+=1
        #     res.append(count)
        # return res 
        res=[0]*(n+1)
        for i in range(1,n+1):
            if i%2==0:
                res[i]=res[i//2]
            else:
                res[i]=res[i//2]+1
        return res        