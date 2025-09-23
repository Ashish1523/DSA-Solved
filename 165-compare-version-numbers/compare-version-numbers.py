class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1=list(map(int,version1.split('.')))
        v2=list(map(int,version2.split('.')))
        # print(v1,v2)
        for i in range(max(len(v1),len(v2))):
            num1=v1[i] if i<len(v1) else 0
            num2=v2[i] if i<len(v2) else 0
            # print(num1,num2)
            if num1<num2:
                return -1
            elif num1>num2:
                return 1
        return 0