class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        r=0
        l=0
        ans=0
        mapy=[0]*26
        while r<n:
            mapy[ord(s[r])-ord('A')]+=1
            if (r-l+1)-max(mapy)>k:
                mapy[ord(s[l])-ord('A')]-=1
                l+=1
            ans=max(ans,r-l+1)
            r+=1
        return ans
            
