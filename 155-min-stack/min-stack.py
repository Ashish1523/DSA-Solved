class MinStack:

    def __init__(self):
        self.s=[]
        # self.n=len(self.s)
        self.min=float("inf")
    def push(self, val: int) -> None:
        if len(self.s)==0:
            self.min=val
            self.s.append(val)
        else:
            if val< self.min:
                self.s.append(2*val-self.min)
                self.min=val
            else:
                self.s.append(val)
        # print(self.s)

    def pop(self) -> None:
        k=self.s.pop()
        if k<self.min:
            self.min=2*self.min-k
        
        

    def top(self) -> int:
        # print(self.s)
        if self.s[len(self.s)-1]<self.min:
            return self.min
        else:
            return self.s[len(self.s)-1]


    def getMin(self) -> int:
        # print(self.s)
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()