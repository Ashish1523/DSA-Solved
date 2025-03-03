class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less,eq,greater=[],[],[]
        for i in range(len(nums)):
            if nums[i]<pivot:
                less.append(nums[i])
            elif nums[i]==pivot:
                eq.append(nums[i])
            else:
                greater.append(nums[i])
        
        return less+eq+greater
        
        
        