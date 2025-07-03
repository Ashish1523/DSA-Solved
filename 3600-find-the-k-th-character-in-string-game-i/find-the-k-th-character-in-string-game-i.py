class Solution:
    def kthCharacter(self, k: int) -> str:
        word="a"
        while len(word)<k:
            ans=""
            for j in range(len(word)):
                if word[j]=="z":
                    ans+="a"
                else:
                    ans+=chr((ord(word[j])+1))
            word+=ans
        return word[k-1]