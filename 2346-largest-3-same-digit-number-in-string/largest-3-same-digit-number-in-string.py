class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n=len(num)
        ans=0
        count=0
        fans=-1
        for i in range(n):
            # print(num[i],count,ans)
            if count==0:
                ans=num[i]
                count+=1
            else:
                if num[i]==ans:
                    count+=1
                    if count==3:
                        fans=max(fans,int(ans))
                else:
                    count=1
                    ans=num[i]
        return str(fans)*3 if fans!=-1 else ""
