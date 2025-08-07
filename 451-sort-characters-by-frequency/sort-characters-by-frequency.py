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
        for i in range(len(s),0,-1):
            for c in buckets[i]:
                res.append(c*i)
        return "".join(res)

        
        