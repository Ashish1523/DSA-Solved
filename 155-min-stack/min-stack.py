class MinStack:

    def __init__(self):
        self.s=[]
        # self.n=len(self.s)
        # self.min=float("inf")
    def push(self, val: int) -> None:
        if len(self.s)==0:
            self.s.append([val,val])
        else:
            self.s.append([val,min(val,self.s[len(self.s)-1][1])])
        # print(self.s)

    def pop(self) -> None:
        self.s.pop()
        

    def top(self) -> int:
        # print(self.s)
        if len(self.s)>0:
            return self.s[len(self.s)-1][0]
        else:
            return -1

    def getMin(self) -> int:
        # print(self.s)
        return self.s[len(self.s)-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()