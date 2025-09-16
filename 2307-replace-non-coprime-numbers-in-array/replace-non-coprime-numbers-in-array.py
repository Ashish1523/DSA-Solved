class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack=[]
        # def gcd(num1,num2):
        #     if num2==0:
        #         # print("gcd",num1)
        #         return num1
        #     return gcd(num2,num1%num2)
        stack
        for num in nums:
            stack.append(num)
            while len(stack)>1:
                val=math.gcd(stack[-1],stack[-2])
                if val!=1:
                    num1=stack.pop()
                    num2=stack.pop()
                    stack.append(num1*num2//val)
                else:
                    break
        return stack