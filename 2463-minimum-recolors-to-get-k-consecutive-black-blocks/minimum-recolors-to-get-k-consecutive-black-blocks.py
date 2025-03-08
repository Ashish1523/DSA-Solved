class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        b=0
        for i in range(k):
            if blocks[i]=='B':
                b+=1
        if b==k:
            return 0
        min1=k-b
        i=0
        for j in range(k,len(blocks)):
            if blocks[i]=='B':
                b-=1
            i+=1
            if blocks[j]=='B':
                b+=1
            if b==k:
                return 0
            min1=min(min1,k-b)
        return min1