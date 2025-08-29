class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        ##sum should be odd -Alice
        ##else Bob
        XOdd=0
        for i in range(1,n+1):
            XOdd+=i&1
        XEven=n-XOdd
        YOdd=0
        for i in range(1,m+1):
            YOdd+=i&1
        YEven=m-YOdd
        # print(XOdd,XEven,YOdd,YEven)
        return XOdd*YEven+YOdd*XEven










