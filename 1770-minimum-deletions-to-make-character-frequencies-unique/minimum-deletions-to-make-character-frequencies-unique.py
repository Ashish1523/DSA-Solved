class Solution:
    def minDeletions(self, s: str) -> int:
        c=Counter(s)
        used=set()
        res=0
        for key,val in c.items():
            while val>0 and val in used:
                val-=1
                res+=1
            used.add(val)
        return res
            