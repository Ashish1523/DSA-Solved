class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        r=0
        l=0
        ans=0
        mapy=[0]*26
        maxf=0
        while r<n:
            mapy[ord(s[r])-ord('A')]+=1
            maxf=max(maxf,mapy[ord(s[r])-ord('A')])
            if (r-l+1)-maxf>k:
                mapy[ord(s[l])-ord('A')]-=1
                l+=1
            ans=max(ans,r-l+1)
            r+=1
        return ans
            
