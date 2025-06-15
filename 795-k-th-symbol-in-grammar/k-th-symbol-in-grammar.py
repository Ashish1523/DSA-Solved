class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # curr=0
        # left,right=1,2**(n-1)
        # for _ in range(n-1):
        #     mid=(left+right)//2
        #     if k<=mid:
        #         right=mid
        #     else:
        #         left=mid+1
        #         curr=0 if curr else 1
        # return curr
        if n == 1 and k == 1:
            return 0  # Base case
        
        mid = 2 ** (n - 2)  # Midpoint of current row
        
        if k <= mid:
            return self.kthGrammar(n - 1, k)
        else:
            return 1 - self.kthGrammar(n - 1, k - mid)