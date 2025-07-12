# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def Valid(root,minV,maxV):
            if root==None:
                return True
            if root.val>=maxV or root.val<=minV:
                return False
            return Valid(root.left,minV,root.val) and Valid(root.right,root.val,maxV)
        
        return Valid(root,float("-inf"),float("inf"))