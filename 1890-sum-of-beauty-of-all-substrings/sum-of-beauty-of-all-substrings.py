class Solution:
    def beautySum(self, s: str) -> int:
        n=len(s)
        sum1=0
        for i in range(n):
            hashy={}
            for j in range(i,n):
                hashy[s[j]]=hashy.get(s[j],0)+1
                beauty=max(hashy.values())-min(hashy.values())
                sum1+=beauty
        return sum1