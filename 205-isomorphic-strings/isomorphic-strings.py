class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ind_s={}
        ind_t={}

        for i in range(len(s)):
            if s[i] not in ind_s:
                ind_s[s[i]]=i
            if t[i] not in ind_t:
                ind_t[t[i]]=i
            if ind_s[s[i]]!=ind_t[t[i]]:
                return False
        return True