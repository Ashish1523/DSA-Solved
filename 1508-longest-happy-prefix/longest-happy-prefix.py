class Solution:
    def longestPrefix(self, s: str) -> str:
        # low=0
        # high=len(s)-1
        # k=0
        # pref=[]
        # suff=[]
        # while(low!=len(s)-1):
            
        #     if s[:low+1]==s[high:]:
        #         k=low+1
        #     low+=1
        #     high-=1
        # return s[0:k] if k else ""
        def compute_lps(pattern):
            lps=[0]*len(pattern)
            length=0
            
            i=1
            while i<len(pattern):
                if pattern[i]==pattern[length]:
                    length+=1
                    lps[i]=length
                    i+=1
                else:
                    if length!=0:
                        length=lps[length-1]
                    else:
                        lps[i]=0
                        i+=1
            return lps
        lps=compute_lps(s)
        return s[:lps[-1]] if lps else ""