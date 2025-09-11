class Solution:
    def sortVowels(self, s: str) -> str:
        set1=set("AEIOUaeiuo")
        vowels=[c for c in s if c in set1]
        vowels.sort()
        result=[]
        it=iter(vowels)

        for c in s:
            result.append(next(it) if c in set1 else c)
        return ''.join(result)