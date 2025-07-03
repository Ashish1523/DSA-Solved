# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxy=float("-inf")
        def maxPath(node):
            nonlocal maxy
            if node==None:
                return 0
            left=max(0,maxPath(node.left))
            right=max(0,maxPath(node.right))
            maxy=max(maxy,left+right+node.val)
            return max(left,right)+node.val
        maxPath(root)
        return maxy