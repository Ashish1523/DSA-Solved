class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count=0
        words=text.split()
        for word in words:
            flag=0
            for l in brokenLetters:
                if l in word:
                    flag=1
                    break
            if not flag:
                count+=1
            flag=0
        return count