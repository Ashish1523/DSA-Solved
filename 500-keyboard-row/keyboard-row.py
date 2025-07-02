class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1="qwertyuiop"
        r2="asdfghjkl"
        r3="zxcvbnm"
        ans=[]
        for word in words:
            if word[0].lower() in r1:
                k=True
                for i in range(1,len(word)):
                    if word[i].lower() not in r1:
                        k=False
                        break
                if k:
                    ans.append(word)
                continue
            if word[0].lower() in r2:
                k=True
                for i in range(1,len(word)):
                    if word[i].lower() not in r2:
                        k=False
                        break
                if k:
                    ans.append(word)
                continue
            if word[0].lower() in r3:
                k=True
                for i in range(1,len(word)):
                    if word[i].lower() not in r3:
                        k=False
                        break
                if k:
                    ans.append(word)
        
        return ans
                
