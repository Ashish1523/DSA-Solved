class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count=0
        n=len(s)
        for i in range(k):
            if s[i] in ['a','e','i','o','u']:
                count+=1
        ans=count
        for i in range(n-k):
            if s[i] in ['a','e','i','o','u']:
                count-=1
            if s[i+k] in ['a','e','i','o','u']:
                count+=1
            ans=max(ans,count)
        return ans
            
            
