class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.n=len(nums)
        self.prefSum=[0]*self.n
        self.prefSum[0]=self.nums[0]
        for i in range(1,self.n):
            self.prefSum[i]+=(self.prefSum[i-1]+self.nums[i])
        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefSum[right]-(self.prefSum[left-1] if left!=0 else 0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)