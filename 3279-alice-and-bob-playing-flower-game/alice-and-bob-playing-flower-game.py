class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        ##sum should be odd -Alice
        ##else Bob
        XOdd=0
        if n&1:
            XOdd=n//2+1
        else:
            XOdd=n//2
        XEven=n-XOdd
        YOdd=0
        if m&1:
            YOdd=m//2+1
        else:
            YOdd=m//2
        YEven=m-YOdd
        # print(XOdd,XEven,YOdd,YEven)
        return XOdd*YEven+YOdd*XEven










