class Solution:
    def sortVowels(self, s: str) -> str:
        set1=set("AEIOUaeiuo")
        n=len(s)
        s=list(s)
        index=[]
        vowels=[]
        for i in range(n):
            if s[i] in set1:
                index.append(i)
                vowels.append(s[i])
        vowels.sort()
        
        for i in range(len(index)):
            s[index[i]]=vowels[i]
        return "".join(s)
                