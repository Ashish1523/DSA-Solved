class Solution:
    def largestOddNumber(self, num: str) -> str:
        # ans=""
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2==1 and num[i]!='0':
                return num[:i+1]
        return ""