class Solution:
    def beautySum(self, s: str) -> int:
        n=len(s)
        sum1=0
        for i in range(n):
            hashy={}
            for j in range(i,n):
                hashy[s[j]]=hashy.get(s[j],0)+1
                sum1+=max(hashy.values())-min(hashy.values())
        return sum1