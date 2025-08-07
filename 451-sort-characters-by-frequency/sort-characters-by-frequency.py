class Solution:
    def frequencySort(self, s: str) -> str:
        mapy={}
        for i in s:
            if i not in mapy:
                mapy[i]=1
            else:
                mapy[i]+=1
        
        buckets=defaultdict(list)

        for char,cnt in mapy.items():
            buckets[cnt].append(char)
        
        res=[]
        m=max(mapy.values())
        for i in range(m,0,-1):
            for c in buckets[i]:
                res.append(c*i)
        return "".join(res)

        
        