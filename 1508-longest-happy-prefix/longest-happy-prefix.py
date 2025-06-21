class Solution:
    def longestPrefix(self, s: str) -> str:
        low=0
        high=len(s)-1
        k=0
        while(low!=len(s)-1):
            # print(s[:low+1],s[high:])
            if s[:low+1]==s[high:]:
                # print(s[:low+1],s[high:])
                k=low+1
            low+=1
            high-=1
        return s[0:k] if k else ""