class Solution:
    def maxFreqSum(self, s: str) -> int:
        Vowels={"a":0,"e":0,"i":0,"o":0,"u":0}
        consonents=defaultdict(int)
        maxVowel=0
        maxConsonant=0
        for letter in s:
            if letter in Vowels:
                Vowels[letter]+=1
                maxVowel=max(maxVowel,Vowels[letter])
            else:
                consonents[letter]+=1
                maxConsonant=max(maxConsonant,consonents[letter])
        return maxVowel+maxConsonant

