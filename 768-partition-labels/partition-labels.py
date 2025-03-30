class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_I={}

        for i,c in enumerate(s):
            last_I[c]=i

        res=[]
        size,end=0,0
        for i,c in enumerate(s):
            size+=1
            end=max(end,last_I[c])

            if i==end:
                res.append(size)
                size=0
        return res

