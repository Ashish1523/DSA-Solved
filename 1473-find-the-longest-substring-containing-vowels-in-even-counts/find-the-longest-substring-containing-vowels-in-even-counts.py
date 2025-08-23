class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        prefXOR=0
        mp=[-1]*32
        ans=0
        for i in range(len(s)):
            if s[i]=='a':
                prefXOR^=(1)
            elif s[i]=='e':
                prefXOR^=(1<<1)
            elif s[i]=='i':
                prefXOR^=(1<<2)
            elif s[i]=='o':
                prefXOR^=(1<<3)
            elif s[i]=='u':
                prefXOR^=(1<<4)
            
            if mp[prefXOR]==-1 and prefXOR!=0:
                mp[prefXOR]=i
            ans=max(ans,i-mp[prefXOR])
        return ans