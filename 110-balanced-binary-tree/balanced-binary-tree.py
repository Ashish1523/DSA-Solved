# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balance(node):
            if node==None:
                return 0
            left=balance(node.left)
            if left==-1:return -1
            right=balance(node.right)
            if right==-1:return -1
            if abs(left-right)>1:return -1
            return max(left,right)+1
        ans=balance(root)
        print(ans)
        return ans!=-1