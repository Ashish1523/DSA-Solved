class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        arr=[]
        count=0
        for i in range(len(s)):
            if s[i]=="(":
                arr.append(s[i])
            elif s[i]==")":
                if len(arr)==0:
                    count+=1
                else:
                    arr.pop()
        count+=len(arr)
        return count