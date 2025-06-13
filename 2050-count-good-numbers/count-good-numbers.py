class Solution:
    def countGoodNumbers(self, n: int) -> int:
        modul=(10**9)+7
        def myPow(a,b):
            nn=b
            ans=1
            while nn:
                if nn%2==0:
                    a=(a*a)%modul
                    nn=nn//2
                else:
                    ans=ans*a%modul
                    nn=nn-1
            return ans
        if n==1:
            return 5
        
        if n%2==0:
            k=n//2
            return (myPow(20,k))%modul
        else:
            k=n//2
            return ((myPow(20,k))*5)%modul