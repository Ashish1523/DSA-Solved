class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def is_pred(s1,s2):
            if len(s1)!=len(s2)+1:
                return False
            
            first=0
            second=0

            while first<len(s1):
                if second<len(s2) and s1[first]==s2[second]:
                    first+=1
                    second+=1
                else:
                    first+=1
            
            return first==len(s1) and second ==len(s2)

        n=len(words)
        words.sort(key=len)
        dp=[1]*n
        maxi=1

        for i in range(n):
            for prev_i in range(i):
                if is_pred(words[i],words[prev_i]) and 1+dp[prev_i]>dp[i]:
                    dp[i]=1+dp[prev_i]
            
            if dp[i]>maxi:
                maxi=dp[i]
        
        return maxi
