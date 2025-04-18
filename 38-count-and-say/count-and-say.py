class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        
        ini="1"
        while(n-1):
            res=""
            ini=ini+"k"
            count=1
            for i in range(len(ini)-1):
                if ini[i]==ini[i+1]:
                    count+=1
                else:
                    res=res+str(count)+ini[i]
                    # print("res",res)
                    count=1
            ini=res
            n-=1
            # print(res)
        return ini


            