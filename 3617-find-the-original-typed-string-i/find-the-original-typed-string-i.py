class Solution:
    def possibleStringCount(self, word: str) -> int:
        sum1=0
        count=1
        for i in range(1,len(word)):
            if word[i]==word[i-1]:
                count+=1
            else:
                if count>1:
                    sum1+=(count-1)
                count=1
        
        return sum1+count
        