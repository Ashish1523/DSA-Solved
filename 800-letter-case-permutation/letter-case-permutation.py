class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res=[]
        stack=[]
        def backtrack(i):
            if i>=len(s):
                res.append("".join(stack))
                return
            if s[i].isalpha():
                stack.append(s[i].lower())
                backtrack(i+1)
                stack.pop()

                stack.append(s[i].upper())
                backtrack(i+1)
                stack.pop()
            else:
                stack.append(s[i])
                backtrack(i+1)
                stack.pop()
        backtrack(0)
        return res
