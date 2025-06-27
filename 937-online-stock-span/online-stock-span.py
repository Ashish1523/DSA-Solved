class StockSpanner:

    def __init__(self):
        self.stack=[]
        self.c=-1
    def next(self, price: int) -> int:
        self.c+=1
        while self.stack and self.stack[-1][0]<=price:
            self.stack.pop()
        res=self.stack[-1][1] if self.stack else -1
        self.stack.append([price,self.c])
        # self.c+=1
        # print(self.stack)
        return self.c-res 


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)