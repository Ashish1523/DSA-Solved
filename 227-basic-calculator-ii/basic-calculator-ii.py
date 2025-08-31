class Solution:
    def calculate(self, s: str) -> int:
        n=len(s)
        if n==0:
            return 0
        stack=[]
        currNumber=0
        op='+'
        for i in range(n):
            currChar=s[i]
            if currChar.isdigit():
                currNumber=(currNumber*10)+int(currChar)
            if (not currChar.isdigit() and currChar!=' ') or (i==n-1):
                if op=='-':
                    stack.append(-currNumber)
                elif op=='+':
                    stack.append(currNumber)
                elif op=='*':
                    stack.append(stack.pop()*currNumber)
                elif op=="/":
                    stack.append(int(stack.pop()/currNumber))
                op=currChar
                currNumber=0
        result=0
        while stack:
            result+=stack.pop()
        return result