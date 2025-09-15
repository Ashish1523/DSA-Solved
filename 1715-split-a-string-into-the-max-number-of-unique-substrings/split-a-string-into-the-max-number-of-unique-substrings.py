class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        res=set()
        mcount=0
        n=len(s)
        def dfs(prev,i,count,res):
            # print(i)
            nonlocal mcount
            if i>=n:
                # print(count)
                mcount=max(count,mcount)
                return
            if s[prev:i+1] not in res:
                res.add(s[prev:i+1])
                dfs(i+1,i+1,count+1,res)
                res.remove(s[prev:i+1])
            dfs(prev,i+1,count,res)
            return
        dfs(0,0,0,res)
        return mcount

