class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count=0
        words=text.split()
        for word in words:
            flag=0
            for l in brokenLetters:
                if l in word:
                    count+=1
                    break
        return len(words)-count