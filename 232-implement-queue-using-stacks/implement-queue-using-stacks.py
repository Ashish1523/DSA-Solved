class MyQueue:

    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def push(self, x: int) -> None:
        self.stack1.append(x)
        # print(self.stack1)

    def pop(self) -> int:
        while(self.stack1):
            self.stack2.append(self.stack1.pop()) 
        i=self.stack2.pop()
        while(self.stack2):
            self.stack1.append(self.stack2.pop()) 
        return i

    def peek(self) -> int:
        return self.stack1[0]

    def empty(self) -> bool:
        if self.stack1==[]:
            return True
        return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()