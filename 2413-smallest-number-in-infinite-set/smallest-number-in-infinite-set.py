class SmallestInfiniteSet:

    def __init__(self):
        self.curr=1
        self.heap=[]
        self.in_heap=set()

    def popSmallest(self) -> int:
        if self.heap:
            x=heapq.heappop(self.heap)
            self.in_heap.remove(x)
            return x
        x=self.curr
        self.curr+=1
        return x
        

    def addBack(self, num: int) -> None:
        if num < self.curr and num not in self.in_heap:
            heapq.heappush(self.heap,num)
            self.in_heap.add(num)

        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)