class Solution:
    def beautySum(self, s: str) -> int:
        n=len(s)
        sum1=0
        def find(freq):
            maxy=0
            mini=501
            for i in freq:
                maxy=max(i,maxy)
                mini=min(mini,i) if i!=0 else mini
            return maxy-mini
        for i in range(n):
            freq=[0]*26
            for j in range(i,n):
                freq[ord(s[j])-ord('a')]+=1
                beauty=find(freq)
                sum1+=beauty
        return sum1