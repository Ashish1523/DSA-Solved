class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def hasDuplicate(s1,s2):
            arr1=[0]*26
            for ch in s1:
                if arr1[ord(ch)-ord('a')]:
                    return True
                arr1[ord(ch)-ord('a')]+=1
            
            for ch in s2:
                # print(ch)
                if arr1[ord(ch)-ord('a')]:
                    return True
                arr1[ord(ch)-ord('a')]+=1
            return False

        dp={}
        def solve(i,temp):
            if i>=n:
                return len(temp)
            if (i,temp) in dp:
                return dp[(i,temp)]
            include=0
            exclude=0

            if (hasDuplicate(temp,arr[i])):
                exclude=solve(i+1,temp)
            else:
                exclude=solve(i+1,temp)
                include=solve(i+1,temp+arr[i])
            dp[(i,temp)]=max(include,exclude)
            return dp[(i,temp)]



        n=len(arr)
        temp=""
        return solve(0,temp)


