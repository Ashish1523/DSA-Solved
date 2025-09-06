class Solution:
    def isValid(self, s: str) -> bool:
        s1=[]
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                s1.append(s[i])
            
            if s[i]==')':
                if len(s1)==0 or s1.pop()!='(':
                    return False
            if s[i]=='}':
                if len(s1)==0 or s1.pop()!='{':
                    return False
            if s[i]==']':
                if len(s1)==0 or s1.pop()!='[':
                    return False
        
        if not s1:
            return True
        return False
        