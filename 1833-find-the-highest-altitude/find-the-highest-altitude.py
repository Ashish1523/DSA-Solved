class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n=len(gain)
        
        ans=0
        pref=0
        for i in range(n):
            pref+=gain[i]
            ans=max(ans,pref)
        return ans