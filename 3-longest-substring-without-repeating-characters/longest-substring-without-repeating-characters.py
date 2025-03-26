class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length=left=0
        count=defaultdict(int)

        for right,c in enumerate(s):
            count[c]+=1
            while count[c] > 1:
                # print(s[left])
                count[s[left]]-=1
                left+=1
            max_length=max(max_length,right-left+1)
        return max_length