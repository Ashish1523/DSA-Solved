class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        prefXOR=0
        chartoval={'a':0,'e':1,'i':2,'o':3,'u':4}
        mp={0:-1}
        ans=0
        for i in range(len(s)):
            if s[i] in chartoval:
                prefXOR^=(1<<chartoval[s[i]])
            
            if prefXOR not in mp:
                mp[prefXOR]=i
            else:
                ans=max(ans,i-mp[prefXOR])
        return ans